"""Event detection engine — divergence detection from episode data."""

from psystack.pipeline.events.config import EventDetectionConfig
from psystack.pipeline.events.detection import detect_events

__all__ = ["EventDetectionConfig", "detect_events"]
