"""Inflion: Observability and influence tracing infrastructure for multi-agent AI systems."""

from importlib.metadata import version as _get_version

from inflion.capabilities import CapabilityRegistry
from inflion.metrics import (
    compute_accumulated_influence,
    compute_attack_surface,
    compute_drift_l2,
    compute_IQx,
    compute_propagation_risk,
    compute_RWI,
    compute_z_score,
)
from inflion.models import (
    AgentCapabilities,
    InteractionEvent,
    PropagationRiskResult,
    ScoreResult,
    SummaryReport,
    TrackerConfig,
)
from inflion.policy import PolicyEngine
from inflion.risk import (
    RiskResult,
    RiskThresholds,
    assign_risk_level,
    calibrate_thresholds,
    compute_risk_score,
)
from inflion.schema import InflionEvent, compute_state_quality
from inflion.tracker import InfluenceTracker
from inflion.validity import ValidityResult, check_validity

__version__ = _get_version("inflion")

__all__ = [
    # Core classes
    "InfluenceTracker",
    "CapabilityRegistry",
    # Models
    "InteractionEvent",
    "ScoreResult",
    "SummaryReport",
    "TrackerConfig",
    "AgentCapabilities",
    "PropagationRiskResult",
    # Extended schema (v0.4.0)
    "InflionEvent",
    "compute_state_quality",
    # Validity (v0.4.0)
    "ValidityResult",
    "check_validity",
    # Risk scoring (v0.4.0)
    "RiskResult",
    "RiskThresholds",
    "compute_risk_score",
    "calibrate_thresholds",
    "assign_risk_level",
    # Policy (v0.4.0)
    "PolicyEngine",
    # Metrics functions
    "compute_drift_l2",
    "compute_IQx",
    "compute_accumulated_influence",
    "compute_propagation_risk",
    "compute_attack_surface",
    "compute_RWI",
    "compute_z_score",
    # Version
    "__version__",
]
