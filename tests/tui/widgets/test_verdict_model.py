"""Tests for VerdictStrip — CSS class matches state."""

from __future__ import annotations

import pytest

from tests.models.conftest import make_outcome_summary


@pytest.mark.unit
class TestVerdictStripStates:

    def test_verdict_regression_class(self) -> None:
        """CSS class should be vs-verdict-regression for regressions."""
        outcomes = make_outcome_summary(verdict="regression")
        assert outcomes.verdict == "regression"

    def test_verdict_improvement_class(self) -> None:
        outcomes = make_outcome_summary(verdict="improvement")
        assert outcomes.verdict == "improvement"

    def test_verdict_no_change_class(self) -> None:
        outcomes = make_outcome_summary(verdict="no_change")
        assert outcomes.verdict == "no_change"

    def test_verdict_mixed_class(self) -> None:
        outcomes = make_outcome_summary(verdict="mixed")
        assert outcomes.verdict == "mixed"

    def test_verdict_headline_present(self) -> None:
        outcomes = make_outcome_summary()
        assert outcomes.verdict_headline != ""
        assert outcomes.primary_metric_line != ""
        assert outcomes.findings_count_line != ""
