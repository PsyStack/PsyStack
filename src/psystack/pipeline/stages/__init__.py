from psystack.pipeline.stages.attribute import AttributeStage
from psystack.pipeline.stages.compare import CompareStage
from psystack.pipeline.stages.events import EventStage
from psystack.pipeline.stages.isolate import IsolateStage
from psystack.pipeline.stages.report import ReportStage

DEFAULT_PIPELINE = (
    CompareStage(),
    EventStage(),
    IsolateStage(),
    AttributeStage(),
    ReportStage(),
)

__all__ = [
    "CompareStage",
    "EventStage",
    "IsolateStage",
    "AttributeStage",
    "ReportStage",
    "DEFAULT_PIPELINE",
]
