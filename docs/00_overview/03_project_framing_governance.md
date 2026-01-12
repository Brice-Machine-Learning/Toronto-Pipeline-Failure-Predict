# Phase 0 — Project Purpose & Success Criteria

## 1. Project Purpose

The **LA Pipeline Break Analytics & Risk Platform** is intended to serve as a **production-style analytics system** that enables stakeholders to understand **where, when, and why water main breaks occur** across Los Angeles using publicly available municipal data.

The platform is designed to support **infrastructure planning, risk awareness, and capital prioritization** by transforming raw break records and environmental datasets into **decision-ready analytics and dashboards**.

This project intentionally prioritizes:

- analytical rigor over novelty  
- realistic utility workflows over experimental modeling  
- maintainability and clarity over premature optimization  

The initial focus is **descriptive and diagnostic analytics**, with a clearly defined and intentional pathway toward **batch-based predictive risk modeling** in later phases.

---

## 2. In-Scope Capabilities

The platform will:

- Ingest and curate historical water main break data
- Aggregate break events to consistent **monthly and geographic units**
- Enrich break data with:
  - climate indicators (rainfall, temperature, drought)
  - soil and geotechnical characteristics
- Persist analytics-ready datasets in a relational database
- Expose clean, modeled tables and views to Power BI
- Deliver dashboards that support:
  - trend and seasonality analysis  
  - environmental correlation analysis  
  - neighborhood-level comparisons  
  - identification of historical break hotspots  

---

## 3. Target Users & Analytical Use Cases

### Primary Users

- utility analysts  
- infrastructure planners  
- engineering managers  
- consulting teams supporting public agencies  

### Core Analytical Questions

- Where do water main breaks cluster spatially and temporally?
- How do environmental conditions relate to break frequency?
- Which neighborhoods exhibit persistently higher break rates?
- How can historical trends inform future infrastructure risk discussions?

---

## 4. Success Criteria

The project will be considered successful when the following conditions are met.

### 4.1 Data & Architecture

- Curated datasets are clean, documented, and reproducible
- Data is stored in a structured relational schema suitable for analytics
- ETL pipelines are modular, auditable, and repeatable

### 4.2 Analytics & Business Intelligence

- Power BI dashboards load directly from modeled tables without manual cleanup
- Users can filter analytics by year, month, and neighborhood
- Trends, seasonality, and spatial patterns are clearly interpretable
- Environmental drivers can be evaluated alongside historical break data

### 4.3 Professional Readiness

- Repository structure mirrors real-world analytics and consulting projects
- Documentation clearly explains assumptions, limitations, and scope
- Outputs resemble deliverables a utility or infrastructure client would accept

### 4.4 Extensibility

- The platform can support batch-based ML risk scoring in later phases
- Additional data layers (e.g., asset metadata) can be incorporated without redesign

---

## 5. Explicit Success Boundaries

The project is **not required** to deliver the following capabilities to be considered successful:

- real-time data ingestion or streaming
- live or API-based inference
- asset-level failure prediction accuracy
- cloud-native or production deployment infrastructure

These capabilities are intentionally deferred to future iterations.

---

## 6. Phase Alignment

This definition establishes a phased delivery strategy:

- **Phase 0–1:** analytics foundation and governance  
- **Phase 2:** feature engineering and batch ML development  
- **Phase 3+:** risk scoring, scenario analysis, and refinement  

Each phase builds upon validated deliverables from prior stages.

---

## Phase 0 Checklist Status

- [x] Project purpose defined  
- [x] Success criteria documented  
- [x] Stakeholders and analytical use cases identified  
