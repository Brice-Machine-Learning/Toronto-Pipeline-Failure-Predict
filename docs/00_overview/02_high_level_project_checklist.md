# 🚰 LA Pipeline Break Analytics & Risk Platform  

## High-Level Project Checklist (Phased)

This checklist defines a **production-style delivery plan** for building an
end-to-end analytics and risk modeling platform for Los Angeles water pipeline
breaks. The phases are intentionally ordered to reflect **real-world data
engineering and analytics workflows**, not notebook-driven experimentation.

---

## Phase 0 — Project Framing & Governance

**Objective:**  
Establish scope, guardrails, and delivery expectations before writing code.

_**Checklist**

- [ ] Define project purpose and success criteria
- [ ] Explicitly document non-goals (e.g., real-time inference)
- [ ] Identify primary stakeholders and analytical use cases
- [ ] Define versioning strategy (v0.x analytics → v1.x risk modeling)
- [ ] Finalize repository structure (code, data, docs separation)
- [ ] Draft initial README (problem, architecture, roadmap)

_**Deliverables**

- README (v0.1)
- `/docs/00_overview/`
- Clear scope and assumptions

---

## Phase 1 — Data Acquisition & Inventory

**Objective:**  
Identify authoritative datasets and document limitations early.

_**Checklist**

- [ ] Inventory all source datasets (breaks, climate, soil, GIS)
- [ ] Validate time coverage, spatial resolution, and update cadence
- [ ] Download and snapshot raw datasets
- [ ] Record known data gaps and inferred fields
- [ ] Store raw data as read-only inputs

_**Deliverables**

- `/data/raw/`
- `/docs/02_data_sources/`
- Documented data assumptions

---

## Phase 2 — Database Design & Platform Setup (Turso)

**Objective:**  
Define the **data contracts** before cleaning or transforming data.

_**Checklist**

- [ ] Select Turso as the analytics system of record
- [ ] Define v1 database schema:
  - core analytics tables
  - environmental dimensions
  - ML feature and prediction tables
- [ ] Write SQL migrations for table creation
- [ ] Add indexes for time and geography
- [ ] Define naming conventions and constraints
- [ ] Deploy empty schema to Turso
- [ ] Document schema and table intent

_**Deliverables**

- Database schema v1 (live, empty)
- SQL migration files
- Schema documentation

---

## Phase 3 — ETL & Data Cleaning (Schema-Driven)

**Objective:**  
Clean and transform data **to satisfy database contracts**, not ad-hoc analysis.

_**Checklist**

- [ ] Build ingestion pipelines for each data source
- [ ] Validate raw data against schema requirements
- [ ] Normalize dates to year/month
- [ ] Standardize geographic keys (neighborhoods/zones)
- [ ] Aggregate breaks to monthly × neighborhood
- [ ] Enrich records with metadata (source, timestamps)
- [ ] Load cleaned data directly into Turso
- [ ] Track ETL runs and row counts

_**Deliverables**

- `pipe_breaks_clean`
- `climate_monthly`
- `soil_zones`
- Reproducible ETL scripts
- ETL run logs

---

## Phase 4 — Analytics Modeling & Database Views

**Objective:**  
Make the database analytics- and BI-ready.

_**Checklist**

- [ ] Create analytics views for common joins
- [ ] Build descriptive `joined_risk_view` (non-ML)
- [ ] Optimize queries for BI performance
- [ ] Validate joins, row counts, and data integrity

_**Deliverables**

- Analytics views
- BI-ready query layer
- Validated database relationships

---

## Phase 5 — Power BI Semantic Model

**Objective:**  
Create a stable semantic layer for dashboards and analysis.

_**Checklist**

- [ ] Build Power BI dataset model
- [ ] Add proper Date table
- [ ] Define star schema relationships
- [ ] Create core DAX measures:
  - total breaks
  - rolling 12-month trends
  - neighborhood comparisons
- [ ] Validate filters, slicers, and performance

_**Deliverables**

- Power BI `.pbit` template
- Documented DAX measures
- Dataset requirements locked

---

## Phase 6 — Descriptive & Diagnostic Dashboards

**Objective:**  
Answer **what happened, where, and what correlates with it**.

_**Checklist**

- [ ] Time-series trend dashboards
- [ ] Seasonality analysis
- [ ] Environmental correlation views
- [ ] Geographic hotspot maps
- [ ] Drill-downs by neighborhood
- [ ] Clear annotations and executive-safe labeling

_**Deliverables**

- Power BI dashboards (v0.1)
- Screenshot assets for README
- Stakeholder-style narrative

---

## Phase 7 — Feature Engineering for Risk Modeling

**Objective:**  
Prepare interpretable, defensible features for ML.

_**Checklist**

- [ ] Rolling break-rate features
- [ ] Lagged climate indicators
- [ ] Soil/geotechnical joins
- [ ] Prior failure indicators
- [ ] Feature versioning
- [ ] Feature schema validation

_**Deliverables**

- `pipe_features_monthly`
- Feature schema files
- Feature documentation

---

## Phase 8 — Machine Learning (Batch Risk Scoring)

**Objective:**  
Produce explainable, batch-based risk scores.

_**Checklist**

- [ ] Select baseline, interpretable models
- [ ] Train using time-aware splits
- [ ] Evaluate performance and stability
- [ ] Generate neighborhood-level risk scores
- [ ] Persist predictions to database
- [ ] Store model metadata and metrics

_**Deliverables**

- Trained models
- `pipe_break_risk_scores`
- Model evaluation report

---

## Phase 9 — Risk Visualization & Interpretation

**Objective:**  
Translate risk outputs into planning insights.

_**Checklist**

- [ ] Risk ranking dashboards
- [ ] High-risk neighborhood summaries
- [ ] Predicted vs historical comparisons
- [ ] Visual explanation of drivers
- [ ] Plain-language interpretation notes

_**Deliverables**

- Risk dashboards (v1.0)
- Executive-ready visuals
- Interpretation documentation

---

## Phase 10 — Polish, Versioning & Portfolio Prep

**Objective:**  
Finalize the project for presentation and review.

_**Checklist**

- [ ] Finalize versioned README
- [ ] Document limitations and future work
- [ ] Write Medium / whitepaper draft
- [ ] Clean commit history
- [ ] Tag v1.0 release

_**Deliverables**

- v1.0 release
- Portfolio-ready project
- Interview-ready talking points

---
