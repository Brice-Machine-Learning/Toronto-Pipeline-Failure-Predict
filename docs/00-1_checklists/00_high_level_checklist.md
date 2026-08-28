# High-Level Project Checklist (Phased) — Toronto Pipeline Failure Predict

This checklist defines major project phases and identifies which phases are included in the **MVP**.

**MVP scope selected:** Analytics-only MVP (ETL + SQLite + baseline model outputs + simple BI/report output).

---

## Phase 0 — Foundation and Alignment (**MVP**)

- [ ] Confirm project scope, success criteria, and non-goals.
- [ ] Finalize architecture baseline and module ownership.
- [ ] Align all documentation on SQLite as the target database.
- [ ] Confirm coding standards, linting, testing, and CI baseline.

---

## Phase 1 — Data Acquisition and Contracts (**MVP**)

- [ ] Finalize source inventory (breaks, climate, soil, GIS) and access approach.
- [ ] Implement reliable ingestion entry points for core data sources.
- [ ] Define and document high-level data contracts for raw/interim/processed layers.
- [ ] Establish data quality gates and failure handling at ingestion boundaries.

---

## Phase 2 — Analytical Storage and Data Model (**MVP**)

- [ ] Implement SQLite database setup and connection layer.
- [ ] Create and apply initial schema/migrations for curated analytical tables.
- [ ] Implement high-level load patterns from processed datasets into SQLite.
- [ ] Validate core table readiness for downstream feature generation and reporting.

---

## Phase 3 — Core ETL and Curated Dataset Build (**MVP**)

- [ ] Implement core transform pipelines for water main breaks + priority enrichment sources.
- [ ] Produce curated, analysis-ready tables at agreed temporal/spatial grain.
- [ ] Add pipeline-level validation and reproducibility checkpoints.
- [ ] Run end-to-end ETL flow from source to SQLite curated tables.

---

## Phase 4 — Baseline Modeling and Scoring Outputs (**MVP**)

- [ ] Implement baseline supervised modeling workflow with time-aware evaluation.
- [ ] Generate baseline risk scores at the agreed unit of analysis.
- [ ] Persist prediction outputs and model metadata into SQLite.
- [ ] Establish minimum model evaluation/reporting artifacts for decision use.

---

## Phase 5 — MVP Delivery: Analytics Consumption (**MVP**)

- [ ] Publish a simple stakeholder-facing output (Power BI starter dataset/report or equivalent).
- [ ] Validate end-to-end traceability from raw data to reported risk outputs.
- [ ] Complete MVP documentation for runbook, assumptions, and known limitations.
- [ ] Freeze MVP baseline and tag release milestone.

---

## Phase 6 — Post-MVP Hardening and Expansion

- [ ] Expand test coverage (integration/data contracts/regression).
- [ ] Improve ETL robustness, observability, and recovery workflows.
- [ ] Strengthen schema/version governance and backfill strategy.
- [ ] Add performance tuning for larger data volumes.

---

## Phase 7 — Post-MVP Advanced Modeling and Risk Framework

- [ ] Add model candidates beyond baseline and compare performance.
- [ ] Introduce advanced feature engineering and explainability workflows.
- [ ] Formalize risk tiering/threshold governance with stakeholder calibration.
- [ ] Add scenario/sensitivity analysis modules (including Monte Carlo where applicable).

---

## Phase 8 — Post-MVP Productization and Operationalization

- [ ] Add scheduled batch orchestration for recurring runs.
- [ ] Implement deployment-grade configuration and environment strategy.
- [ ] Expand BI/reporting products for different stakeholder groups.
- [ ] Prepare operational handoff artifacts and long-term maintenance plan.

---

## MVP Boundary Summary

Phases included in MVP:

- **Phase 0**
- **Phase 1**
- **Phase 2**
- **Phase 3**
- **Phase 4**
- **Phase 5**

Post-MVP starts at:

- **Phase 6**
