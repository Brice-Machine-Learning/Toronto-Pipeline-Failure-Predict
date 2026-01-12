# Phase 0 — Explicit Non-Goals

## Purpose of This Document

This document defines **explicit non-goals** for the LA Pipeline Break Analytics & Risk Platform.  
Its purpose is to **prevent scope creep**, clarify delivery boundaries, and ensure that the project remains aligned with its intended **analytics-first** objectives.

The exclusions below are **intentional design decisions**, not technical limitations.

---

## 1. Real-Time or Streaming Analytics

The platform will **not** support:

- real-time data ingestion
- streaming pipelines (e.g., Kafka, Kinesis)
- live dashboards reflecting near-real-time events

**Rationale:**  
Water main break data is reported with significant latency and is analyzed at **monthly or longer intervals** in real utility workflows. Real-time analytics would add complexity without improving decision quality.

---

## 2. Live or API-Based Model Inference

The platform will **not** include:

- REST or GraphQL prediction APIs
- real-time inference endpoints
- user-triggered prediction services

**Rationale:**  
Predictive components, if introduced, will operate as **batch-based scoring processes** designed for analytics and planning—not operational dispatch.

---

## 3. Asset-Level Failure Prediction

The platform will **not** attempt to:

- predict failures for individual pipe segments
- guarantee predictive accuracy at the asset level
- replace engineering inspections or condition assessments

**Rationale:**  
Publicly available datasets lack the asset-level metadata (material, install year, pressure history) required for defensible pipe-level predictions. The project instead focuses on **area-level risk patterns**.

---

## 4. Operational Decision Automation

The platform will **not**:

- trigger maintenance actions
- generate work orders
- recommend specific construction or repair schedules
- integrate with CMMS or asset management systems

**Rationale:**  
The platform is an **analytical decision-support tool**, not an operational control system.

---

## 5. Cloud-Native Production Deployment

The platform will **not** require:

- cloud-native orchestration (Kubernetes, Airflow)
- auto-scaling infrastructure
- high-availability or SLA guarantees

**Rationale:**  
The system is designed to be **locally deployable and reproducible**, with cloud deployment considered optional and out of scope for initial versions.

---

## 6. Exhaustive Data Completeness

The platform will **not** guarantee:

- complete historical coverage for all years
- perfectly aligned datasets across all sources
- absence of reporting bias or data gaps

**Rationale:**  
Public infrastructure datasets are inherently incomplete. The project emphasizes **transparent assumptions and limitations**, not artificial completeness.

---

## 7. Advanced ML Techniques in Early Phases

Early project phases will **not** include:

- deep learning models
- real-time anomaly detection
- automated feature discovery
- model explainability frameworks beyond basic diagnostics

**Rationale:**  
Initial phases prioritize **interpretable, explainable analytics** over complex modeling approaches.

---

## 8. Policy, Legal, or Financial Decision Authority

The platform will **not**:

- establish regulatory compliance
- determine funding eligibility
- replace professional engineering judgment
- serve as a legal or financial decision system

**Rationale:**  
The platform provides **insight**, not authority.

---

## 9. Scope Expansion Without Phase Approval

The project will **not**:

- add new data domains without documented justification
- introduce new delivery mechanisms mid-phase
- change core objectives without Phase 0 revision

**Rationale:**  
All scope changes must be aligned with the documented phase roadmap and explicitly approved through documentation updates.

---

## Summary

These non-goals ensure the project remains:

- focused on analytics value
- aligned with real-world utility workflows
- defensible in scope and design
- extensible without premature complexity

Anything outside these boundaries is considered **future work**, not a current deficiency.

---

## Phase 0 Checklist Status

- [x] Explicit non-goals documented  
- [x] Scope boundaries enforced  
- [x] Future expansion clearly deferred  
