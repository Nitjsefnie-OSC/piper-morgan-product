"""Tests for learning/preference consciousness wrapper. Issue #636."""

import pytest


class TestLearningConsciousness:
    """Test consciousness wrapper for learning feedback."""

    def test_patterns_learned_has_identity(self):
        """Learning feedback must have identity voice."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        patterns = [
            {"description": "Morning standup preference", "occurrences": 5, "confidence": 0.85},
        ]
        output = format_patterns_learned_conscious(patterns, 10)
        assert "I" in output or "I'" in output, "Should have identity"

    def test_patterns_learned_explains_what(self):
        """Learning feedback should explain what was learned."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        patterns = [
            {"description": "Prefers concise updates", "occurrences": 3, "confidence": 0.9},
        ]
        output = format_patterns_learned_conscious(patterns, 5)
        assert "concise" in output.lower() or "pattern" in output.lower()

    def test_patterns_learned_invites_correction_without_an_offer(self):
        """Learning feedback invites correction as a statement (#2011, CXO
        2026-10-14): no unbuilt "should I look at the data differently?"."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        patterns = [{"description": "test", "occurrences": 2, "confidence": 0.7}]
        output = format_patterns_learned_conscious(patterns, 3)
        assert "Tell me if this doesn't match what you see." in output
        assert "should I" not in output

    def test_no_patterns_has_identity(self):
        """No patterns message should have identity."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        output = format_patterns_learned_conscious([], 5)
        assert "I" in output or "I'" in output


class TestLearningConsciousnessEdgeCases:
    """Test edge cases for learning consciousness."""

    def test_patterns_with_high_confidence(self):
        """High confidence patterns should express more certainty."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        patterns = [
            {"description": "Prefers morning meetings", "occurrences": 10, "confidence": 0.95},
        ]
        output = format_patterns_learned_conscious(patterns, 15)
        # Should express confidence
        assert "confident" in output.lower() or "pretty" in output.lower()

    def test_patterns_with_low_confidence(self):
        """Low confidence patterns should express uncertainty."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        patterns = [
            {"description": "Might prefer brief updates", "occurrences": 2, "confidence": 0.4},
        ]
        output = format_patterns_learned_conscious(patterns, 10)
        # Should express uncertainty
        assert "think" in output.lower() or "seem" in output.lower()

    def test_multiple_patterns_formatted(self):
        """Multiple patterns should all be mentioned."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        patterns = [
            {"description": "Morning preference", "occurrences": 5, "confidence": 0.8},
            {"description": "Concise style", "occurrences": 3, "confidence": 0.7},
            {"description": "Weekly reviews", "occurrences": 2, "confidence": 0.6},
        ]
        output = format_patterns_learned_conscious(patterns, 20)
        # Should mention all patterns or at least the top ones
        assert "morning" in output.lower() or "concise" in output.lower()

    def test_no_patterns_mentions_future_learning(self):
        """No patterns message should express willingness to learn."""
        from services.consciousness.learning_consciousness import format_patterns_learned_conscious

        output = format_patterns_learned_conscious([], 3)
        # Should express willingness to continue learning
        assert "learn" in output.lower() or "better" in output.lower() or "work" in output.lower()
