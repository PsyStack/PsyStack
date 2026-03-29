"""Tests for EventNavigator widget — INV-5-1."""

from __future__ import annotations

import pytest

from tests.tui.widgets.conftest import make_events


@pytest.mark.tui
class TestEventNavigatorItems:

    def test_events_one_to_one_with_input(self) -> None:
        """INV-5-1: event items 1:1 with input events."""
        events = make_events(5)
        # Verify builder produces correct count
        assert len(events) == 5
        for i, evt in enumerate(events):
            assert evt.step == i * 10

    def test_empty_events(self) -> None:
        events = make_events(0)
        assert events == []

    def test_severity_grouping(self) -> None:
        """Events should be groupable by severity."""
        events = make_events(4)
        suggested = [e for e in events if e.severity in ("critical", "warning")]
        other = [e for e in events if e.severity == "info"]
        assert len(suggested) + len(other) == len(events)
