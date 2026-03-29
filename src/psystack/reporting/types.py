"""Canonical reporting models — ReportBundle is the single reporting contract."""

from __future__ import annotations

from pydantic import BaseModel, Field

from psystack.models import RunManifest
from psystack.models.comparison import ComparisonReport
from psystack.models.isolation import AttributionTable, IsolationResultBundle


class ArtifactRef(BaseModel):
    kind: str
    label: str
    path: str


class ReportSummary(BaseModel):
    total_metrics: int
    regressions: int
    improvements: int
    no_change: int


class ReportBundle(BaseModel):
    workspace: str
    baseline_manifest: RunManifest
    candidate_manifest: RunManifest
    summary: ReportSummary
    compare: ComparisonReport
    isolation: IsolationResultBundle | None = None
    attribution: list[AttributionTable] = Field(default_factory=list)
    artifacts: list[ArtifactRef] = Field(default_factory=list)
