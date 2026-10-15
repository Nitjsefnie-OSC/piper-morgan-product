"""
Process Registry for Guided Processes.

ADR-049: Two-Tier Intent Architecture

A Guided Process is a multi-turn conversation where Piper maintains control
until completion or exit. Examples: onboarding, standup, planning, feedback.

The Process Registry tracks active guided processes per session and checks
them BEFORE intent classification to prevent derailment.

Issue #427: MUX-IMPLEMENT-CONVERSE-MODEL
Issue #687: ADR-049 Implementation
"""

import inspect
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Protocol, runtime_checkable

import structlog

logger = structlog.get_logger(__name__)


# Issue #888, #889: Escape commands recognized at registry level.
# PPM binding direction (2026-03-13): These bypass workflow handlers entirely.
# Arch guidance: Exact match on stripped+lowercased full message. Use frozenset.
#
# #888 split (Arch 2026-10-15, on #1771): the six words are two sets, generic
# across processes. The REGISTRY decides the transition from the word alone,
# before any handler runs; the handler supplies only the line for each outcome
# (``pause_message`` / ``drop_message``), never the choice. The word map is
# CXO's call (experience); each set is a one-line edit.
#
# END: terminal, through ``_close_process`` (the handler's ``close()``; no
# resume re-offer, the #1529 anti-nag).
ESCAPE_END_WORDS: frozenset = frozenset({"cancel", "quit", "exit", "never mind"})
# PAUSE: ``suspend()``, resumable. ``skip`` stays here, where it was (every
# escape word paused before the split), until CXO places it: in a guided
# interview it may mean "skip this question" (Arch 10-15, not ruled).
ESCAPE_PAUSE_WORDS: frozenset = frozenset({"stop", "skip"})
# The union, for readers that only ask "is this an escape word?" (the
# destructive-confirm decline set, the #1529 bare-exit comment, tests).
ESCAPE_COMMANDS: frozenset = ESCAPE_END_WORDS | ESCAPE_PAUSE_WORDS


def _sync_hook_line(handler: Any, hook_name: str) -> Optional[str]:
    """A SYNC no-argument copy hook's line, or None (absent, async, raising,
    or returning nothing)."""
    hook = getattr(handler, hook_name, None)
    # A sync hook only: an async attribute (an AsyncMock double, say) would
    # hand back an un-awaited coroutine, never a line. Async hooks are read by
    # ``escape_reply_for``, which can await them.
    if callable(hook) and not inspect.iscoroutinefunction(hook):
        try:
            line = hook()
        except Exception as e:  # silent-ok: logged; the generic line still exits honestly
            logger.warning(f"{hook_name}_hook_failed", error=str(e))
            line = None
        if isinstance(line, str) and line:
            return line
    return None


def pause_message_for(handler: Any) -> str:
    """The reply when an escape command pauses ``handler``'s active session.

    #1771 (Arch, on the issue 2026-10-14): the HANDLER supplies its pause
    line through an optional ``pause_message()`` method; the registry keeps
    only the generic default, so it stays the "dumb aggregator" #888 made it
    and holds no per-process copy. Optional rather than a ``GuidedProcess``
    protocol member on purpose: the protocol is ``runtime_checkable`` and
    implemented structurally, so a new member would make every existing
    implementer (and test double) fail ``register``'s isinstance check. A
    hook that raises or returns nothing falls back to the generic line.
    """
    line = _sync_hook_line(handler, "pause_message")
    if line:
        return line
    return f"No problem — I've paused {handler.process_type.value}. We can pick it up anytime."


def drop_message_for(handler: Any) -> str:
    """The reply when an END escape word closes ``handler``'s active session.

    #888 split (Arch 2026-10-15): the sibling of :func:`pause_message_for`,
    through an optional ``drop_message()`` hook, same pattern and same
    reasons. The generic default is the #1529 exit copy the generic close
    already uses, so an END word and a whole-message exit read alike.
    """
    line = _sync_hook_line(handler, "drop_message")
    if line:
        return line
    from services.process.escape import format_exit_message

    return format_exit_message(handler.process_type)


async def escape_reply_for(
    handler: Any,
    user_id: Optional[str],
    session_id: Optional[str],
    *,
    end: bool,
) -> str:
    """The line for an escape word, read BEFORE the registry's transition.

    A handler's copy hook (``drop_message`` for END, ``pause_message`` for
    PAUSE) may be ASYNC and take ``(user_id, session_id)`` so it can read its
    own conversation state to pick the copy (Arch 2026-10-15: an unstarted
    standup gets the invitation line). Copy only: the hook never transitions
    and never chooses; the word already chose. Read before the transition so
    the hook sees the state the user left from. A sync no-argument hook, a
    raising hook or a non-string answer falls back as the sync resolvers do.
    """
    hook_name = "drop_message" if end else "pause_message"
    hook = getattr(handler, hook_name, None)
    if hook is not None and inspect.iscoroutinefunction(hook):
        try:
            line = await hook(user_id, session_id)
        except Exception as e:  # silent-ok: logged; the generic line still exits honestly
            logger.warning(f"{hook_name}_hook_failed", error=str(e))
            line = None
        if isinstance(line, str) and line:
            return line
    return drop_message_for(handler) if end else pause_message_for(handler)


class ProcessType(str, Enum):
    """
    Types of guided processes.

    Current (MVP):
    - ONBOARDING: Portfolio setup for new users
    - STANDUP: Interactive standup creation
    - SLOT_FILLING: Natural multi-turn slot collection (#765)

    Future (Advanced Layer):
    - PLANNING: Structured planning sessions
    - FEEDBACK: User feedback collection
    - CLARIFICATION: Pending question resolution
    """

    ONBOARDING = "onboarding"
    STANDUP = "standup"
    SLOT_FILLING = "slot_filling"  # Issue #765 GLUE-SLOTFILL
    # Future types (Advanced Layer - see #698, #699, #700)
    PLANNING = "planning"
    FEEDBACK = "feedback"
    CLARIFICATION = "clarification"


@dataclass
class SuspendedInfo:
    """
    Lightweight info about a suspended workflow session.

    Issue #888: Arch guidance — registry discovers suspended sessions
    via has_suspended_session(), handlers own the semantics.
    """

    process_type: ProcessType
    suspended_at: Optional[datetime] = None
    description: str = ""


@dataclass
class ProcessCheckResult:
    """
    Result of checking for an active guided process.

    If handled is True, the message was handled by a guided process
    and classification should be bypassed.
    """

    handled: bool
    process_type: Optional[ProcessType] = None
    response_message: Optional[str] = None
    intent_data: Optional[Dict[str, Any]] = None
    escaped: bool = False  # True when user used an escape command

    @classmethod
    def not_handled(cls) -> "ProcessCheckResult":
        """No active process claimed the message."""
        return cls(handled=False)

    @classmethod
    def handled_by(
        cls,
        process_type: ProcessType,
        response_message: str,
        intent_data: Dict[str, Any],
    ) -> "ProcessCheckResult":
        """Message was handled by a guided process."""
        return cls(
            handled=True,
            process_type=process_type,
            response_message=response_message,
            intent_data=intent_data,
        )

    @classmethod
    def off_topic_pause(
        cls,
        process_type: ProcessType,
        pause_message: str,
    ) -> "ProcessCheckResult":
        """
        Process was paused because user sent an off-topic message.

        Issue #899: Layer C escape. Unlike escaped_from(), this returns
        handled=False so normal intent processing can answer the user's
        actual question. The pause_message is prepended by IntentService.
        """
        return cls(
            handled=False,  # Let intent processing handle the actual question
            escaped=True,
            process_type=process_type,
            response_message=pause_message,
            intent_data={
                "category": "guidance",
                "action": "off_topic_pause",
                "confidence": 1.0,
                "context": {
                    "paused_process": process_type.value,
                    "bypassed_classification": False,  # Intent processing continues
                    "off_topic_detected": True,
                },
            },
        )

    @classmethod
    def escaped_from(
        cls,
        process_type: ProcessType,
        response_message: str,
    ) -> "ProcessCheckResult":
        """User escaped from an active guided process via escape command."""
        return cls(
            handled=True,
            escaped=True,
            process_type=process_type,
            response_message=response_message,
            intent_data={
                "category": "guidance",
                "action": "workflow_escaped",
                "confidence": 1.0,
                "context": {
                    "escaped_process": process_type.value,
                    "bypassed_classification": True,
                },
            },
        )


@runtime_checkable
class GuidedProcess(Protocol):
    """
    Protocol for guided process handlers.

    Each guided process type implements this protocol to integrate
    with the process registry.

    Issue #888: Added suspend() and has_suspended_session() per
    PPM direction and Arch guidance (2026-03-13).

    Optional, not protocol members (#1771, #888 split): ``pause_message()``
    and ``drop_message()``, the lines shown when a PAUSE or an END escape word
    leaves this process; sync with no arguments, or async taking
    ``(user_id, session_id)`` to read the handler's own state (copy only).
    See :func:`pause_message_for`, :func:`drop_message_for` and
    :func:`escape_reply_for` for the generic defaults and why they are optional.
    """

    @property
    def process_type(self) -> ProcessType:
        """The type of this guided process."""
        ...

    async def check_active(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
    ) -> bool:
        """
        Check if there's an active session for this user/session.

        Returns True if an active (non-terminal) session exists.
        """
        ...

    async def handle_message(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
        message: str,
    ) -> ProcessCheckResult:
        """
        Handle a message in the context of an active session.

        Only called if check_active returned True.
        Returns ProcessCheckResult with handled=True and response.
        """
        ...

    async def suspend(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
    ) -> None:
        """
        Suspend the active session, preserving state for later resumption.

        Issue #888: Called by ProcessRegistry when user issues an escape
        command. Transitions session to SUSPENDED state. Handler owns
        the semantics of what "suspended" means for its workflow.
        """
        ...

    async def has_suspended_session(
        self,
        user_id: Optional[str],
    ) -> Optional[SuspendedInfo]:
        """
        Check if this user has a suspended session.

        Issue #888: Arch guidance — registry discovers suspended sessions
        by iterating handlers. Each handler checks its own state machine.

        Returns SuspendedInfo if a suspended session exists, None otherwise.
        """
        ...


class ProcessRegistry:
    """
    Registry of guided process handlers.

    Maintains the list of registered processes and checks them in
    priority order when processing a message.

    Design principle: Check processes in a defined priority order.
    First match wins. If no process claims the message, proceed
    with normal intent classification.
    """

    # Singleton instance
    _instance: Optional["ProcessRegistry"] = None

    def __init__(self):
        # Process handlers in priority order
        self._handlers: List[GuidedProcess] = []
        # Priority order for checking (lower = higher priority)
        self._priority_order: Dict[ProcessType, int] = {
            ProcessType.ONBOARDING: 10,  # Highest priority
            ProcessType.STANDUP: 20,
            ProcessType.SLOT_FILLING: 25,  # Issue #765 — after standup, before clarification
            ProcessType.CLARIFICATION: 30,
            ProcessType.PLANNING: 40,
            ProcessType.FEEDBACK: 50,
        }
        logger.info("ProcessRegistry initialized")

    @classmethod
    def get_instance(cls) -> "ProcessRegistry":
        """Get singleton instance of the registry."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset singleton (for testing)."""
        cls._instance = None

    def register(self, handler: GuidedProcess) -> None:
        """
        Register a guided process handler.

        Handlers are automatically sorted by priority order.
        """
        if not isinstance(handler, GuidedProcess):
            raise TypeError(f"Handler must implement GuidedProcess protocol: {handler}")

        # Check for duplicate registration
        for existing in self._handlers:
            if existing.process_type == handler.process_type:
                logger.warning(
                    "Replacing existing handler for process type",
                    process_type=handler.process_type.value,
                )
                self._handlers.remove(existing)
                break

        self._handlers.append(handler)

        # Sort by priority
        self._handlers.sort(key=lambda h: self._priority_order.get(h.process_type, 100))

        logger.info(
            "Registered guided process handler",
            process_type=handler.process_type.value,
            priority=self._priority_order.get(handler.process_type, 100),
        )

    def unregister(self, process_type: ProcessType) -> bool:
        """
        Unregister a handler by process type.

        Returns True if a handler was removed.
        """
        for handler in self._handlers:
            if handler.process_type == process_type:
                self._handlers.remove(handler)
                logger.info(
                    "Unregistered guided process handler",
                    process_type=process_type.value,
                )
                return True
        return False

    def _check_off_topic(self, message: str, process_type: ProcessType):
        """
        Check if a message is off-topic for the active process.

        Issue #899: Layer C escape — conservative off-topic detection.
        Returns OffTopicResult if detection ran, None if module unavailable.
        """
        try:
            from services.process.off_topic import OffTopicResult, detect_off_topic

            return detect_off_topic(message, process_type)
        except Exception as e:
            logger.warning(
                "Off-topic detection failed, allowing message through",
                error=str(e),
            )
            return None

    def _is_escape_command(self, message: str) -> bool:
        """
        Check if a message is an escape command.

        Issue #888: PPM binding direction — exact match on stripped+lowercased
        full message. No regex, no substring. "cancel" escapes, but
        "cancel my standup" does NOT.

        Arch guidance (2026-03-13): Use frozenset for O(1) lookup.
        """
        normalized = message.strip().lower()
        return normalized in ESCAPE_COMMANDS

    def _is_escape_end_word(self, message: str) -> bool:
        """#888 split: is this escape word an END word (else it pauses)?
        Same normalisation as ``_is_escape_command``."""
        return message.strip().lower() in ESCAPE_END_WORDS

    async def _close_process(
        self,
        handler: GuidedProcess,
        user_id: Optional[str],
        session_id: Optional[str],
    ) -> None:
        """Close a flow for good (exit/refusal — #1529).

        Prefers the handler's `close()` (terminal state: no resume re-offer,
        which is the nag loop #1529 documents) and falls back to `suspend()`
        for handlers that don't implement it. Duck-typed on purpose so the
        GuidedProcess protocol doesn't force a migration.
        """
        closer = getattr(handler, "close", None)
        try:
            if closer is not None:
                await closer(user_id, session_id)
            else:
                await handler.suspend(user_id, session_id)
        except Exception as close_err:
            logger.warning(
                "Error closing process after escape",
                process_type=handler.process_type.value,
                error=str(close_err),
            )

    async def _handler_exit_reply(
        self,
        handler: GuidedProcess,
        user_id: Optional[str],
        session_id: Optional[str],
        message: str,
    ) -> Optional[str]:
        """#1771: let the handler answer a #1529 whole-message exit itself.

        Optional async hook ``exit_reply(user_id, session_id, message)``: the
        handler performs its own transition (suspend or close) and returns
        its line, or returns None to leave the exit to the generic close.
        Duck-typed like ``close``/``release`` and ``pause_message`` (a new
        protocol member would fail ``register``'s structural isinstance
        check for every existing implementer). A hook that raises falls back
        to the generic close, so an exit never traps the user in the flow.
        """
        hook = getattr(handler, "exit_reply", None)
        if hook is None or not inspect.iscoroutinefunction(hook):
            return None
        try:
            line = await hook(user_id, session_id, message)
        except Exception as e:  # silent-ok: logged; the generic close still exits
            logger.warning(
                "exit_reply_hook_failed",
                process_type=handler.process_type.value,
                error=str(e),
            )
            return None
        return line if isinstance(line, str) and line else None

    async def _in_completion_tail(
        self,
        handler: GuidedProcess,
        user_id: Optional[str],
        session_id: Optional[str],
    ) -> bool:
        """#1617: is this flow in a post-delivery completion tail? Duck-typed
        (``in_completion_tail`` on the adapter) so the GuidedProcess protocol
        doesn't force a migration; absent/failing → False (mid-flow
        semantics, the conservative direction)."""
        checker = getattr(handler, "in_completion_tail", None)
        if checker is None:
            return False
        try:
            return bool(await checker(user_id, session_id))
        except Exception as e:
            logger.warning(
                "Completion-tail check failed, treating as mid-flow",
                process_type=handler.process_type.value,
                error=str(e),
            )
            return False

    async def _release_process(
        self,
        handler: GuidedProcess,
        user_id: Optional[str],
        session_id: Optional[str],
    ) -> None:
        """#1617: end a flow whose work is already DELIVERED (completion-tail
        release). Prefers the adapter's ``release()`` (terminal COMPLETE — the
        work happened; no resume nag) and falls back to ``_close_process``
        (terminal ABANDONED) for handlers without it. Duck-typed like close."""
        releaser = getattr(handler, "release", None)
        if releaser is None:
            await self._close_process(handler, user_id, session_id)
            return
        try:
            await releaser(user_id, session_id)
        except Exception as release_err:
            logger.warning(
                "Error releasing completed process, falling back to close",
                process_type=handler.process_type.value,
                error=str(release_err),
            )
            await self._close_process(handler, user_id, session_id)

    async def _handle_escape_signal(
        self,
        handler: GuidedProcess,
        user_id: Optional[str],
        session_id: Optional[str],
        message: str,
    ) -> Optional[ProcessCheckResult]:
        """Issue #1529: universal escape check for an active guided flow.

        Runs the flow-generic escape detection (exit / refusal / off-intent)
        and, when a signal fires, closes or pauses the flow and returns the
        appropriate ProcessCheckResult. Returns None when the message should
        proceed to the flow's handler. Detection failures never trap the user
        IN the flow silently — they log and return None (the pre-existing
        #888 exact-match escape above remains the guaranteed hatch).

        #1617 (completion-tail release): when the flow is in a post-delivery
        tail state, the off_intent tier additionally consults the
        deterministic cross-domain detectors (escape.check_escape's
        ``in_completion_tail``), and an off-intent turn RELEASES the flow
        (terminal — its work stands; nothing to resume) instead of
        suspending it, so normal processing answers the turn and every
        subsequent turn is free.
        """
        in_tail = await self._in_completion_tail(handler, user_id, session_id)
        try:
            from services.process.escape import (
                check_escape,
                format_exit_message,
                format_refusal_prefix,
                format_release_prefix,
            )

            signal = check_escape(message, handler.process_type, in_completion_tail=in_tail)
        except Exception as e:
            logger.warning(
                "Escape check failed, message proceeds to flow handler",
                process_type=handler.process_type.value,
                error=str(e),
            )
            return None

        if signal is None:
            return None

        logger.info(
            "Guided-process escape detected",
            process_type=handler.process_type.value,
            kind=signal.kind,
            matched=signal.matched[:80],
            has_residual=signal.residual is not None,
            user_id=user_id,
            session_id=session_id,
        )

        if signal.kind == "exit":
            # #1771 (CXO 10-15, Arch's constraint): the HANDLER chooses pause
            # or end for a whole-message exit ("not now" pauses a standup,
            # "cancel that" drops it). The registry holds no deferral words;
            # without the hook (or when it declines) the exit closes, as #1529
            # built it.
            line = await self._handler_exit_reply(handler, user_id, session_id, message)
            if line is None:
                await self._close_process(handler, user_id, session_id)
                line = format_exit_message(handler.process_type)
            return ProcessCheckResult.escaped_from(
                process_type=handler.process_type,
                response_message=line,
            )

        if signal.kind == "refusal":
            await self._close_process(handler, user_id, session_id)
            if signal.residual:
                # Refusal + an actual request ("… restore CoVa"): exit the
                # flow and let normal intent processing answer the request,
                # with the honest exit copy prepended (off_topic_pause shape).
                return ProcessCheckResult.off_topic_pause(
                    process_type=handler.process_type,
                    pause_message=format_refusal_prefix(handler.process_type),
                )
            return ProcessCheckResult.escaped_from(
                process_type=handler.process_type,
                response_message=format_exit_message(handler.process_type),
            )

        # off_intent — two sub-cases:
        # #1617: in a completion tail the flow's work is DELIVERED — release
        # it for good (terminal; a suspended tail would re-offer resuming a
        # standup that already exists, the resume-nag loop) and let normal
        # processing answer with the honest release prefix.
        if in_tail:
            await self._release_process(handler, user_id, session_id)
            return ProcessCheckResult.off_topic_pause(
                process_type=handler.process_type,
                pause_message=format_release_prefix(handler.process_type),
            )

        # Mid-flow — Option A UX (#899): pause (resumable) + answer.
        try:
            await handler.suspend(user_id, session_id)
        except Exception as suspend_err:
            logger.warning(
                "Error suspending process after off-intent escape",
                process_type=handler.process_type.value,
                error=str(suspend_err),
            )
        from services.process.off_topic import format_off_topic_pause_message

        return ProcessCheckResult.off_topic_pause(
            process_type=handler.process_type,
            pause_message=format_off_topic_pause_message(handler.process_type),
        )

    async def check_suspended_processes(
        self,
        user_id: Optional[str],
    ) -> Optional[SuspendedInfo]:
        """
        Check all handlers for a suspended session belonging to user_id.

        Issue #888: Arch guidance — registry is a "dumb aggregator."
        Iterates handlers, each checks its own state machine. First
        suspended session found wins (priority order).

        Returns SuspendedInfo if a suspended session exists, None otherwise.
        """
        if not user_id:
            return None

        for handler in self._handlers:
            try:
                suspended = await handler.has_suspended_session(user_id)
                if suspended is not None:
                    logger.info(
                        "Found suspended session",
                        process_type=suspended.process_type.value,
                        user_id=user_id,
                    )
                    return suspended
            except Exception as e:
                logger.warning(
                    "Error checking suspended session",
                    process_type=handler.process_type.value,
                    error=str(e),
                )
                continue

        return None

    async def check_active_processes(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
        message: str,
    ) -> ProcessCheckResult:
        """
        Check all registered processes for an active session.

        Issue #888: Escape commands are checked BEFORE routing to handler.
        PPM binding direction: "recognized by the ProcessRegistry directly,
        not passed to the workflow handler for interpretation."

        Checks in priority order. First process that has an active
        session and can handle the message wins.

        Args:
            user_id: Authenticated user ID (may be None)
            session_id: Session identifier
            message: User's message

        Returns:
            ProcessCheckResult - handled=True if a process claimed the message
        """
        for handler in self._handlers:
            try:
                # First check if there's an active session
                is_active = await handler.check_active(user_id, session_id)

                if is_active:
                    logger.debug(
                        "Found active guided process",
                        process_type=handler.process_type.value,
                        user_id=user_id,
                        session_id=session_id,
                    )

                    # Issue #888: Check for escape commands BEFORE routing to handler.
                    # This is the guaranteed escape hatch — no handler can break it.
                    if self._is_escape_command(message):
                        logger.info(
                            "Escape command intercepted by registry",
                            process_type=handler.process_type.value,
                            escape_command=message.strip().lower(),
                            user_id=user_id,
                            session_id=session_id,
                        )
                        # #888 split (Arch 2026-10-15): the WORD picks the
                        # transition, here, before any handler runs; the
                        # handler supplies only the line (read first, so its
                        # copy hook sees the state the user left from).
                        end = self._is_escape_end_word(message)
                        line = await escape_reply_for(handler, user_id, session_id, end=end)
                        if end:
                            # END: terminal (handler's close(); no re-offer)
                            await self._close_process(handler, user_id, session_id)
                        else:
                            # PAUSE: suspend (handler owns what that means)
                            try:
                                await handler.suspend(user_id, session_id)
                            except Exception as suspend_err:
                                logger.warning(
                                    "Error suspending process after escape",
                                    process_type=handler.process_type.value,
                                    error=str(suspend_err),
                                )
                        return ProcessCheckResult.escaped_from(
                            process_type=handler.process_type,
                            response_message=line,
                        )

                    # Issue #1529: universal escape check (FLOW-ESCAPE) — exits,
                    # refusals, and cross-domain actions are consumed HERE,
                    # deterministically, before the flow can transcribe them and
                    # before any classifier sees them.
                    escape_result = await self._handle_escape_signal(
                        handler, user_id, session_id, message
                    )
                    if escape_result is not None:
                        return escape_result

                    # Issue #899: Layer C — off-topic detection.
                    # Check if the message is clearly unrelated to the active process.
                    # Conservative: only clear non-sequiturs trigger auto-pause.
                    off_topic_result = self._check_off_topic(message, handler.process_type)
                    if off_topic_result is not None and off_topic_result.is_off_topic:
                        logger.info(
                            "Off-topic message detected during guided process",
                            process_type=handler.process_type.value,
                            pattern=off_topic_result.matched_pattern,
                            user_id=user_id,
                            session_id=session_id,
                        )
                        # Option A UX: auto-pause + let normal intent processing answer
                        try:
                            await handler.suspend(user_id, session_id)
                        except Exception as suspend_err:
                            logger.warning(
                                "Error suspending process after off-topic detection",
                                process_type=handler.process_type.value,
                                error=str(suspend_err),
                            )

                        from services.process.off_topic import format_off_topic_pause_message

                        pause_msg = format_off_topic_pause_message(handler.process_type)
                        return ProcessCheckResult.off_topic_pause(
                            process_type=handler.process_type,
                            pause_message=pause_msg,
                        )

                    # Let the handler process the message
                    result = await handler.handle_message(user_id, session_id, message)

                    if result.handled:
                        logger.info(
                            "Message handled by guided process",
                            process_type=handler.process_type.value,
                            user_id=user_id,
                            session_id=session_id,
                        )
                        return result

            except Exception as e:
                logger.warning(
                    "Error checking guided process",
                    process_type=handler.process_type.value,
                    error=str(e),
                )
                # Continue to next handler
                continue

        return ProcessCheckResult.not_handled()

    async def any_active(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
    ) -> bool:
        """#1625: is ANY guided process active for this session?

        Read-only probe for surfaces that must stay quiet mid-flow (the
        due-reminder mention gate: no reminder block inside an active
        gathering/interview exchange). Unlike check_active_processes it
        takes no message and never claims, suspends, or escapes anything —
        it only asks each handler's check_active (which may apply its own
        lazy housekeeping, e.g. the standup tail-timeout auto-suspend — the
        same thing the next claim check would have done). A handler error
        counts as not-active for that handler (same continue-on-error
        posture as the claim path).
        """
        for handler in self._handlers:
            try:
                if await handler.check_active(user_id, session_id):
                    return True
            except Exception as e:
                logger.warning(
                    "Error probing guided process activity",
                    process_type=handler.process_type.value,
                    error=str(e),
                )
                continue
        return False

    async def first_active_type(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
    ) -> Optional[str]:
        """#1595: WHICH guided process is active for this session, if any.

        ``any_active``'s loop returning the type instead of a bool — the
        SessionSnapshot assembly needs "standup", not just "something".
        Same probe (``check_active``), same continue-on-error posture (a
        handler error counts as not-active for that handler), same registry
        order (first active handler wins, matching the claim order in
        ``check_active_processes``).

        Accepted side effect, documented rather than pretended away
        (#1651 lane): ``check_active`` is not strictly read-only — it
        applies each handler's lazy timeout housekeeping. Concretely: the
        standup adapter auto-suspends a completion-tail conversation idle
        > STANDUP_TIMEOUT_MINUTES (``services/process/adapters.py``,
        StandupProcessAdapter.check_active, the #1623-gated tail-timeout
        block), and the onboarding adapter auto-suspends a session idle
        > ONBOARDING_TIMEOUT_MINUTES (OnboardingProcessAdapter.check_active,
        the #888 timeout block). Both are CONVERGENT housekeeping the next
        claim check would have applied identically — after one probe the
        world is in the state every subsequent probe observes, so the
        snapshot's idempotence pin (assemble twice → identical world)
        holds. There is no timeout-free probe variant to call instead;
        adding one would fork the activity definition (#1555).
        """
        for handler in self._handlers:
            try:
                if await handler.check_active(user_id, session_id):
                    return handler.process_type.value
            except Exception as e:
                logger.warning(
                    "Error probing guided process activity",
                    process_type=handler.process_type.value,
                    error=str(e),
                )
                continue
        return None

    @property
    def registered_types(self) -> List[ProcessType]:
        """List of currently registered process types."""
        return [h.process_type for h in self._handlers]


# Convenience function for getting the singleton
def get_process_registry() -> ProcessRegistry:
    """Get the singleton process registry instance."""
    return ProcessRegistry.get_instance()
