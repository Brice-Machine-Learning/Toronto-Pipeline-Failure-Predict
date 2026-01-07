# Data Flow Architecture

This document describes how data moves through the **LA Water Main Break Analytics & Risk Platform**, from raw public datasets to analytics-ready dashboards and ML-driven risk scores.

The data flow is intentionally **batch-oriented**, **database-centered**, and **BI-first**, reflecting how infrastructure analytics systems are implemented in real utility environments.

---

## High-Level Data Flow Diagram

```mermaid
flowchart LR
    A[Public Data Sources\n(CSV / GeoJSON)] --> B[Python ETL Pipelines]
    B --> C[(Analytical Database\nDuckDB or Turso)]
    C --> D[Feature Engineering\n(Python)]
    D --> C
    C --> E[Batch ML Training / Scoring]
    E --> C
    C --> F[Power BI Datasets]
    F --> G[Dashboards & Reports]
```

---

## End-to-End Data Flow

This section describes the complete lifecycle of data as it moves through the system, from raw source files to analytics-ready dashboards and machine learning risk scores.

---

### 1️⃣ Data Ingestion (Raw → Curated)

_**Source Data**

- Los Angeles water main break records (public datasets)
- Climate data (NOAA / PRISM)
- Soil and geotechnical reference layers

_**Process**

- Python ETL scripts ingest raw CSV and geospatial files
- Data is cleaned, normalized, and validated
- Temporal fields (year, month) are derived
- Spatial joins and lookups are applied where required
- Data quality checks are performed prior to persistence

**Output**
Curated analytical tables written to the database, including:

- `pipe_breaks_clean`
- `climate_monthly`
- `soil_zones`

At this stage, data is **analytics-ready** but not yet transformed into ML features.

---

### 2️⃣ Analytical Storage Layer

All curated data is persisted in a single **analytical database**, which acts as the **system of record** for the platform.

- **DuckDB** is used during local development for rapid iteration
- **Turso (libSQL)** is used for deployed, shared analytics

The database is responsible for:

- storing curated fact and dimension tables
- persisting engineered features
- persisting ML predictions and metadata
- serving data to Power BI

The database does **not** execute machine learning models.  
It provides stable, queryable storage for downstream consumers.

---

### 3️⃣ Feature Engineering (Curated → Features)

_**Input**

- Curated analytical tables stored in the database

_**Process**

- Feature engineering is performed in Python
- Rolling aggregates, lag features, and environmental summaries are computed
- All feature logic resides in code, not database-specific SQL
- Feature definitions are versioned and timestamped

_**Output**

- Feature tables written back to the database:
  - `pipe_features_monthly`

This separation allows features to be reused, audited, and regenerated independently of model training.

---

### 4️⃣ Machine Learning (Batch Execution)

Machine learning workflows are executed as **batch processes**, consistent with infrastructure analytics practices.

_**Process**

- Models read input data from `pipe_features_monthly`
- Training is performed offline using historical data
- Prediction runs occur on a schedule or on demand
- No real-time or request-based inference is used

_**Output**

- Prediction results written back to the database:
  - `pipe_break_risk_scores`
- Model version and metadata recorded separately

Power BI never triggers model execution directly; it only consumes persisted results.

---

### 5️⃣ Business Intelligence Consumption

_**Input**

- Curated analytics tables
- Feature tables (optional)
- ML prediction tables

_**Process**

- Power BI connects directly to the analytical database
- Semantic models, relationships, and measures are defined within Power BI
- Optional database views simplify joins for reporting
- Dataset refreshes occur independently of ML execution

**Output**
Dashboards and reports including:

- break trends and seasonality
- environmental and geotechnical drivers
- geographic hotspot analysis
- ML-based risk rankings

This design ensures dashboards remain stable even as upstream models evolve.

---

## DuckDB ↔ Turso Switching

The end-to-end data flow remains **identical** regardless of database backend.

- DuckDB supports fast local development and experimentation
- Turso provides deployable, persistent analytics storage

The only difference between environments is the **database connection configuration**.

All schemas, SQL queries, ETL logic, ML code, and Power BI datasets remain unchanged.

Refer to:

- `docs/06_database/01_duckdb_turso_parity_checklist.md`
- `docs/06_database/02_db_switch_procedure.md`

---

## Key Architectural Guarantees

This data flow design ensures:

- repeatable ETL and ML execution  
- no dependency on real-time model inference  
- stable Power BI dashboards  
- auditable and reproducible analytics outputs  
- safe promotion from local development to deployed environments  

---

## Summary

The platform follows a clear, layered data flow:

_**Raw Data → ETL → Database → Features → ML → Database → Power BI**

This approach prioritizes **clarity, reproducibility, and real-world deployability**, making it well suited for infrastructure analytics and asset risk modeling.
