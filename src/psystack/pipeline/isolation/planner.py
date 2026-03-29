from __future__ import annotations

from psystack.models.isolation import IsolationPlan
from psystack.pipeline.isolation.designs import screening_v1


def build_isolation_plan(design: str = "screening_v1") -> IsolationPlan:
    if design == "screening_v1":
        return screening_v1()
    raise ValueError(f"Unknown isolation design: {design}")
