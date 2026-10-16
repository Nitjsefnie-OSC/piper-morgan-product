"""
Intent classification caching layer.

Reduces redundant classifications for repeated queries.
Implements in-memory cache with TTL-based expiration.

Created: October 5, 2025
Issue: #206 (CORE-GREAT-4B Phase 3)
"""

import copy
import hashlib
import logging

# 2026-10-13 (PM: "keep only fingerprints of logs"): the cache lines carry
# the text's sha256 by default, the text only under the opt-in knob.
from services.utils.utterance_log import log_full_utterance, utterance_sha256


def _text_ref(text: str) -> str:
    """What the cache lines say about the text: its sha256 by default, the
    old 50-char prefix only under the opt-in knob (stdlib logger — no fields)."""
    return f"{text[:50]}..." if log_full_utterance() else f"sha256={utterance_sha256(text)}"


import time
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class IntentCache:
    """
    In-memory cache for intent classification results.

    Holds CLASSIFICATION only (#2054, Arch 2026-10-16; ADR-080 D3): what the
    classifier produced for the text (category, action, confidence, entities,
    learning signals, and the classifier-built context). ``set`` stores a deep
    copy and ``get`` returns a deep copy, so no two turns ever share a mutable
    object and nothing a turn writes after classification (the principal, the
    routing keys) can reach another turn through the cache. The principal is
    stamped from the request on every turn by IntentService, never inherited.

    Uses text hash as key to handle case variations and whitespace.
    Implements TTL-based expiration for cache entries.

    Performance Target:
    - Hit rate >60% for production workload
    - Latency reduction: ~1ms → <0.1ms for cache hits
    """

    def __init__(self, ttl: int = 3600):
        """
        Initialize cache.

        Args:
            ttl: Time-to-live in seconds (default 1 hour)
        """
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl = ttl
        self.hits = 0
        self.misses = 0
        logger.info(f"IntentCache initialized with TTL={ttl}s")

    def get(self, text: str) -> Optional[Dict[str, Any]]:
        """
        Get cached intent result if exists and not expired.

        Args:
            text: User input text

        Returns:
            Cached intent dict or None if miss/expired
        """
        key = self._hash_text(text)

        if key in self.cache:
            entry = self.cache[key]

            # Check expiration
            if time.time() < entry["expires_at"]:
                self.hits += 1
                logger.debug("Cache HIT for: %s", _text_ref(text))
                # #2054 (Arch, 2026-10-16): every hit gets its OWN copy. The
                # caller builds an Intent around this dict and IntentService
                # then writes per-turn state (the principal, routing keys)
                # into its context; handing out the stored object would
                # share that state with every later hit, from any user.
                return copy.deepcopy(entry["intent"])
            else:
                # Expired - remove
                del self.cache[key]
                logger.debug("Cache EXPIRED for: %s", _text_ref(text))

        self.misses += 1
        logger.debug("Cache MISS for: %s", _text_ref(text))
        return None

    def set(self, text: str, intent: Dict[str, Any]) -> None:
        """
        Cache intent classification result.

        Args:
            text: User input text
            intent: Classification result to cache
        """
        key = self._hash_text(text)

        # #2054 (Arch, 2026-10-16): store a SNAPSHOT of the classification,
        # never the caller's objects. On a miss the classifier caches the dict
        # the returned Intent still holds as its context; storing it by
        # reference let the turn's later writes (user_id, secondary_intents,
        # armed_offer_rail, ...) land in the cache entry itself.
        self.cache[key] = {
            "intent": copy.deepcopy(intent),
            "expires_at": time.time() + self.ttl,
            "cached_at": time.time(),
        }

        logger.debug("Cache SET for: %s", _text_ref(text))

    def invalidate(self, text: str) -> bool:
        """
        Remove specific entry from cache.

        Args:
            text: User input text to invalidate

        Returns:
            True if entry was removed, False if not found
        """
        key = self._hash_text(text)
        if key in self.cache:
            del self.cache[key]
            logger.debug("Cache INVALIDATED for: %s", _text_ref(text))
            return True
        return False

    def clear(self) -> None:
        """Clear entire cache and reset metrics."""
        count = len(self.cache)
        self.cache.clear()
        self.hits = 0
        self.misses = 0
        logger.info(f"Cache CLEARED ({count} entries removed)")

    def get_metrics(self) -> Dict[str, Any]:
        """
        Return cache performance metrics.

        Returns:
            Dict with hits, misses, hit_rate, size, ttl
        """
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0

        return {
            "hits": self.hits,
            "misses": self.misses,
            "total_requests": total,
            "hit_rate_percent": round(hit_rate, 2),
            "cache_size": len(self.cache),
            "ttl_seconds": self.ttl,
        }

    def _hash_text(self, text: str) -> str:
        """
        Create cache key from text.

        Normalizes text (lowercase, strip) before hashing to handle
        case variations and whitespace differences.

        Args:
            text: User input text

        Returns:
            MD5 hash of normalized text
        """
        normalized = text.lower().strip()
        return hashlib.md5(normalized.encode()).hexdigest()
