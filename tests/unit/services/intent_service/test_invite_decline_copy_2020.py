"""#2020 (CXO ruling, 2026-10-14): the interview invitation's decline copy.

Web's served run on 5e5f3366c4: after the EMPTY lead ("I don't have anything to
build your standup from yet…"), declining said "your quick report stays exactly
as it is" — a report that the previous turn said did not exist. Ruled:

- no report (INVITE_EMPTY_LEAD) → "No problem. I won't ask again in this chat.
  Say 'my standup interview' any time to try the guided version."
- report rendered (INVITE_AFTER_REPORT) → the "stays exactly as it is" copy.
- the word is "this chat": the suppression is ``vi.was_declined(session_id, …)``,
  keyed by the session, which is one chat; "this session" was the old word.

The carrier chooses the copy from the ``question`` it is told it renders
(#1665: the caller passes the lead it is about to surface).
"""

from services.intent_service import standup_preferences as sp
from services.intent_service import verified_inference as vi

_USER = "user-2020"


def test_empty_lead_decline_claims_no_report():
    sid = "sess-2020-empty"
    rec = sp.build_interview_invitation(_USER, sid, question=sp.INVITE_EMPTY_LEAD)
    assert rec is not None
    assert rec["decline_message"] == sp.INVITE_DECLINE_MESSAGE_NO_REPORT
    assert "quick report" not in rec["decline_message"]
    assert rec["decline_message"] == (
        "No problem. I won't ask again in this chat. Say 'my standup interview' "
        "any time to try the guided version."
    )


def test_after_report_decline_keeps_the_report_copy():
    sid = "sess-2020-report"
    rec = sp.build_interview_invitation(_USER, sid, question=sp.INVITE_AFTER_REPORT)
    assert rec is not None
    assert rec["decline_message"] == sp.INVITE_DECLINE_MESSAGE
    assert rec["decline_message"] == (
        "No problem — your quick report stays exactly as it is, and I won't ask "
        "again in this chat. Say 'my standup interview' any time to try the "
        "guided version."
    )


def test_the_word_is_this_chat_on_both_and_the_suppression_is_per_session():
    for text in (sp.INVITE_DECLINE_MESSAGE, sp.INVITE_DECLINE_MESSAGE_NO_REPORT):
        assert "in this chat" in text
        assert "this session" not in text
    # The claim "I won't ask again in this chat" is the per-session decline
    # memory: declined in one session, the builder refuses to re-arm there and
    # still arms in another session.
    sid_a, sid_b = "sess-2020-a", "sess-2020-b"
    vi.mark_declined(sid_a, sp.INVITE_DECLINE_KEY)
    assert sp.build_interview_invitation(_USER, sid_a, question=sp.INVITE_EMPTY_LEAD) is None
    assert sp.build_interview_invitation(_USER, sid_b, question=sp.INVITE_EMPTY_LEAD) is not None
