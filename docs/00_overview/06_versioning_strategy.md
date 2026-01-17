# Phase 0 — Versioning Strategy

## Purpose of This Document

This document defines the **versioning strategy** for the LA Pipeline Break Analytics & Risk Platform.  
Its goal is to clearly communicate how the project evolves over time, what each version represents, and how capabilities are introduced in a **controlled, intentional manner**.

Versioning is used to:

- manage scope and expectations
- separate analytics maturity levels
- document capability progression
- prevent premature feature creep

---

## 1. Versioning Philosophy

The project follows a **capability-based versioning model**, not strict semantic versioning tied to APIs.

Each major version represents a **meaningful shift in analytical capability**, data maturity, or delivery expectations.

High-level progression:

- `v0.x` → analytics foundation
- `v1.x` → risk modeling
- `v2.x` → expanded modeling & scenario analysis

---

## 2. Version 0.x — Analytics Foundation

### Definition

Version 0.x represents a **descriptive and diagnostic analytics platform** focused on understanding historical water main break behavior.

This is the **minimum viable professional analytics system**.

### Version 0.x Core Capabilities

- Curated historical break datasets
- Monthly and neighborhood-level aggregation
- Environmental enrichment (climate, soil)
- Relational database optimized for analytics
- Power BI dashboards supporting:
  - trends
  - seasonality
  - geographic hotspots
  - environmental correlations

### Explicit Exclusions

Version 0.x does **not** include:

- predictive modeling
- ML-generated risk scores
- real-time analytics
- operational decision automation

### Success Criteria

Version 0.x is complete when:

- dashboards load from modeled tables without manual intervention
- analytical questions defined in Phase 0 are answerable
- documentation clearly explains assumptions and limitations

---

## 3. Version 1.x — Risk Modeling & Scoring

### Version 1.x Definition

Version 1.x introduces **batch-based predictive modeling** to estimate **relative break risk** at an aggregated geographic level.

### Version 1.x Core Capabilities

- Feature engineering pipelines
- Trainable ML models using historical data
- Persisted batch risk scores
- Model versioning and metadata tracking
- Power BI integration of risk outputs

### Design Constraints

- Predictions are **relative risk indicators**, not absolute failure probabilities
- Models operate in **offline batch mode**
- Outputs are designed for **planning and prioritization**, not operations

---

## 4. Version 2.x — Advanced Analytics & Scenario Analysis (Future)

### Version 2.x Definition

Version 2.x expands analytical depth and exploratory capability.

### Potential Capabilities

- scenario-based risk comparison
- sensitivity analysis for environmental drivers
- expanded feature sets (if new data becomes available)
- improved model diagnostics and validation

### Notes

All Version 2.x features are **explicitly out of scope** until prior versions are completed and validated.

---

## 5. Backward Compatibility & Stability

- Historical analytics outputs remain valid across versions
- New features do not invalidate prior dashboards
- Schema changes are additive whenever possible
- Breaking changes require documentation updates

---

## 6. Version Labeling Conventions

- `v0.x.y` — analytics refinements, dashboard improvements
- `v1.x.y` — modeling improvements, feature updates
- `v2.x.y` — experimental or advanced analytics additions

---

## 7. Governance & Change Control

- Version changes must be documented
- Scope additions require alignment with Phase definitions
- Features introduced ahead of version maturity are considered violations of governance

---

## Phase 0 Checklist Status

- [x] Versioning strategy defined  
- [x] Capability progression documented  
- [x] Governance boundaries established  
