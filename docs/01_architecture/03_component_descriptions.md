# Component Responsibilities

This document defines the **responsibilities, inputs, and outputs** of each major component in the **LA Water Main Break Analytics & Risk Platform**.  
The goal is to make ownership and boundaries explicit, preventing overlap between ETL, ML, database, and BI layers.

---

## System Component Responsibility Table

| Component | Location | Primary Responsibility | Inputs | Outputs |
| --------- | ------- | ---------------------- | ------ | ------- |
| **Raw Data Sources** | External | Provide original municipal and environmental datasets | CSV, GeoJSON, shapefiles | Raw files |
| **Data Ingestion (ETL)** | `src/.../etl/` | Ingest, clean, normalize, and validate raw data | Raw datasets | Curated analytics tables |
| **Analytical Database** | DuckDB / Turso | Persist analytics-ready data, features, and predictions | Curated data, features, predictions | Queryable tables and views |
| **Schema Definitions** | `/schemas/` | Define data contracts across system layers | Data design specifications | Enforced structure consistency |
| **Database Migrations** | `src/.../db/migrations/` | Create and evolve database schema | SQL migration scripts | Versioned database structure |
| **DB Access Layer** | `src/.../db/` | Manage database connections and query execution | Connection config, SQL files | DataFrames / query results |
| **Feature Engineering** | `src/.../features/` | Generate ML-ready features from curated data | Curated database tables | Feature tables |
| **Feature Storage** | `pipe_features_monthly` | Persist engineered features for reuse | Feature DataFrames | Stored feature records |
| **Machine Learning – Training** | `src/.../models/train_model.py` | Train models using historical features | Feature tables | Trained model artifacts |
| **Machine Learning – Scoring** | `src/.../models/predict_model.py` | Generate batch risk predictions | Features, trained models | Risk score tables |
| **Model Evaluation** | `src/.../models/evaluate_model.py` | Assess model performance and metrics | Predictions, ground truth | Evaluation reports |
| **Model Registry** | `/models/model_registry.json` | Track model versions and metadata | Training outputs | Versioned model metadata |
| **Visualization (Python)** | `src/.../visualization/` | Generate EDA and diagnostic plots | Curated data, features | Static figures |
| **Power BI Datasets** | `/powerbi/datasets/` | Define SQL-based datasets for BI | Database tables/views | BI-ready datasets |
| **Power BI Semantic Model** | `/powerbi/model/` | Define relationships and measures | BI datasets | Semantic layer |
| **Power BI Reports** | `/powerbi/reports/` | Deliver stakeholder-facing dashboards | Semantic model | Interactive dashboards |
| **Configuration** | `src/.../config/` | Centralize environment and runtime settings | `.env` variables | Runtime configuration |
| **Logging** | `src/.../log/` | Capture pipeline and execution logs | Runtime events | Log records |
| **Documentation** | `/docs/` | Describe architecture, data flow, and operations | System knowledge | Shared understanding |

---

## Responsibility Boundaries (Key Rules)

The following rules are enforced across the system:

- **ETL does not perform ML**
- **ML does not clean raw data**
- **The database does not execute ML logic**
- **Power BI does not transform raw data**
- **Feature logic lives in Python, not SQL**
- **Schemas define contracts, not implementations**

These boundaries ensure components remain loosely coupled and independently evolvable.

---

## Ownership Model

Each layer owns a distinct concern:

- **ETL** owns data correctness  
- **Database** owns persistence and accessibility  
- **Feature engineering** owns feature definitions  
- **ML workflows** own prediction logic  
- **Power BI** owns presentation and interaction  

No component bypasses another layer’s responsibility.

---

## Summary

This responsibility model ensures the platform remains:

- maintainable  
- auditable  
- scalable  
- deployable  

Clear ownership boundaries prevent analytical drift, simplify debugging, and enable safe evolution of the system over time.
