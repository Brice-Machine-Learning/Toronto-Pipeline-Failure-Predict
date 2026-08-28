# 🚰 Pipeline Break Prediction — Toronto Water

## Infrastructure Risk Modeling • Machine Learning • Geospatial Analytics

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-active%20scaffolding-yellow)
![Version](https://img.shields.io/badge/version-v0.1.0-blue)
![ML](https://img.shields.io/badge/machine%20learning-batch%20risk%20modeling-green)
![DB](https://img.shields.io/badge/database-Turso%20%7C%20DuckDB-lightgrey)
![BI](https://img.shields.io/badge/BI-Power%20BI-orange)

**Current Version:** `v0.1.0` — *Architecture & documentation baseline*

---

## 📌 Project Overview

This project builds a **machine-learning–driven pipeline break risk platform** for the **City of Toronto water distribution system** using real, open municipal data.

It combines **civil engineering domain knowledge**, **geospatial analytics**, and **modern data science** to model pipeline failure risk and deliver **actionable insights** for infrastructure planning, asset management, and capital prioritization.

The system is designed as a **realistic analytics platform**, not a toy ML notebook. This project features batch ETL pipelines, persistent analytical storage, feature engineering workflows, ML prediction, and Power BI-ready outputs aligned with how utilities and consultants actually operate.

---

## 🧠 Why This Project Matters

Urban water utilities face increasing pressure from:

- aging buried infrastructure  
- corrosive soils and geotechnical conditions  
- climate-driven stress (freeze–thaw cycles, precipitation variability, temperature extremes)  
- deferred maintenance and constrained capital budgets  

Applied machine learning can help utilities:

- prioritize high-risk assets  
- reduce break frequency and service disruptions  
- justify capital investment decisions  
- transition from reactive to proactive maintenance  

This project demonstrates **how ML can be applied responsibly and defensibly** in infrastructure risk contexts, grounded in real data availability, realistic workflows, and explainable outputs.

---

## 🎯 Project Objectives

- Predict pipeline break likelihood over time  
- Identify spatial and temporal break patterns  
- Integrate environmental and geotechnical drivers  
- Generate interpretable risk scores  
- Support planning, reporting, and decision-making workflows  

---

## 🏗️ System Scope & Design Philosophy

This is a **large, multi-layer project** that includes:

- exploratory notebooks  
- modular Python source code  
- database-backed analytics  
- batch ML workflows  
- Power BI dashboards  
- forward-looking API integration (FastAPI planned)  

Because of this scope, the project structure is **intentionally documented**, not visualized inline.

👉 **See `/docs` for full architecture, data flow, and component documentation.**

---

## 🧩 Planned Project Components

### 1️⃣ Data Acquisition & ETL

- City of Toronto water main break datasets  
- Water infrastructure asset metadata (age, material, diameter)  
- Climate data (Environment and Climate Change Canada)  
- Soil, geology, and corrosivity layers (Ontario Geological Survey, NRCan)  
- Neighborhood and municipal geographies  
- Automated ingestion, validation, and versioned ETL pipelines  

---

### 2️⃣ Exploratory Data Analysis (EDA)

- break frequency distributions  
- temporal seasonality (monthly / annual)  
- spatial patterns and clustering  
- environmental and geotechnical correlations  
- data quality checks and anomaly detection  

---

### 3️⃣ Feature Engineering

A hybrid civil engineering + data science approach:

| Category | Example Features |
| ------- | ---------------- |
| Pipe Attributes | age, diameter, material |
| Environmental | precipitation, temperature, freeze–thaw frequency |
| Geotechnical | soil corrosivity, geological units |
| Spatial | neighborhood, watershed context |
| Temporal | seasonality, lagged break history |

---

### 4️⃣ Machine Learning (Batch)

- Supervised learning (classification / regression)  
- Time-aware train/test splits  
- Baseline models + gradient boosting  
- SHAP-based interpretability  
- Batch scoring (not real-time inference)  

Outputs:

- break probability  
- risk score  
- feature importance  

---

### 5️⃣ Risk Scoring & Reporting

- utility-style risk tiers  
- ranked high-risk segments or zones  
- monthly / annual scoring runs  
- BI-ready analytical outputs  

---

### 6️⃣ Dashboards & Analytics (Power BI)

Planned dashboards include:

- breaks over time  
- environmental drivers  
- geographic risk heatmaps  
- neighborhood-level drilldowns  
- ML-based risk ranking and comparison  

---

## 🧱 Technical Stack

### Core Technologies

- **Python** (pandas, numpy, scikit-learn, geopandas, shapely)
- **DuckDB** (local analytical compute)
- **Turso (libSQL)** (persistent analytical storage)
- **Power BI** (dashboards and reporting)
- **Jupyter Notebooks**
- **Git & GitHub**

Planned:

- **FastAPI** for API-based access and future extensions

---

## 📁 Project Structure

This repository contains **multiple subsystems** (ETL, ML, DB, BI, docs).  
To keep the README readable, the full structure is documented separately.

👉 **See:**  
📂 `docs/01_architecture/01_structure.md`  
📂 `docs/01_architecture/02_data_flow.md`  
📂 `docs/01_architecture/03_component_descriptions.md`

---

## 🚀 Versioning

This project follows **semantic versioning**, with each release representing a stable milestone.

### ✅ Released

- **v0.1.0** — Architecture, data flow, database strategy, and operational documentation

### 🔜 Planned Versions

| Version | Focus |
| ------ | ------ |
| **v0.2.0** | Data ingestion pipelines + initial EDA |
| **v0.3.0** | Feature engineering + geospatial enrichment |
| **v0.4.0** | Baseline and boosted ML models |
| **v0.5.0** | Risk scoring framework + Power BI dashboards |
| **v1.0.0** | End-to-end deployed analytics platform |

Architectural stability is maintained across versions even as features and datasets expand.

---

## 🚀 Roadmap

### Phase 0 — Foundation and Alignment (MVP)

- [ ] Confirm project scope, success criteria, and non-goals
- [ ] Finalize architecture baseline and module ownership
- [ ] Align all documentation on SQLite as the target database
- [ ] Confirm coding standards, linting, testing, and CI baseline

### Phase 1 — Data Acquisition and Contracts (MVP)

- [ ] Finalize source inventory (breaks, climate, soil, GIS) and access approach
- [ ] Implement reliable ingestion entry points for core data sources
- [ ] Define and document high-level data contracts for raw/interim/processed layers
- [ ] Establish data quality gates and failure handling at ingestion boundaries

### Phase 2 — Analytical Storage and Data Model (MVP)

- [ ] Implement SQLite database setup and connection layer
- [ ] Create and apply initial schema/migrations for curated analytical tables
- [ ] Implement high-level load patterns from processed datasets into SQLite
- [ ] Validate core table readiness for downstream feature generation and reporting

### Phase 3 — Core ETL and Curated Dataset Build (MVP)

- [ ] Implement core transform pipelines for water main breaks and priority enrichment sources
- [ ] Produce curated, analysis-ready tables at agreed temporal/spatial grain
- [ ] Add pipeline-level validation and reproducibility checkpoints
- [ ] Run end-to-end ETL flow from source to SQLite curated tables

### Phase 4 — Baseline Modeling and Scoring Outputs (MVP)

- [ ] Implement baseline supervised modeling workflow with time-aware evaluation
- [ ] Generate baseline risk scores at the agreed unit of analysis
- [ ] Persist prediction outputs and model metadata into SQLite
- [ ] Establish minimum model evaluation/reporting artifacts for decision use

### Phase 5 — MVP Delivery: Analytics Consumption (MVP)

- [ ] Publish a simple stakeholder-facing output (Power BI starter dataset/report or equivalent)
- [ ] Validate end-to-end traceability from raw data to reported risk outputs
- [ ] Complete MVP documentation for runbook, assumptions, and known limitations
- [ ] Freeze MVP baseline and tag release milestone

### Phase 6 — Post-MVP Hardening and Expansion

- [ ] Expand test coverage (integration/data contracts/regression)
- [ ] Improve ETL robustness, observability, and recovery workflows
- [ ] Strengthen schema/version governance and backfill strategy
- [ ] Add performance tuning for larger data volumes

### Phase 7 — Post-MVP Advanced Modeling and Risk Framework

- [ ] Add model candidates beyond baseline and compare performance
- [ ] Introduce advanced feature engineering and explainability workflows
- [ ] Formalize risk tiering/threshold governance with stakeholder calibration
- [ ] Add scenario and sensitivity analysis modules

### Phase 8 — Post-MVP Productization and Operationalization

- [ ] Add scheduled batch orchestration for recurring runs
- [ ] Implement deployment-grade configuration and environment strategy
- [ ] Expand BI/reporting products for different stakeholder groups
- [ ] Prepare operational handoff artifacts and long-term maintenance plan

**MVP included:** Phases 0–5  
**Post-MVP starts:** Phase 6

---

## 📬 Project Status

**Status:** Active scaffolding and documentation phase  
**Full development:** Begins December 2025  

The project is being built with **senior-level structure and documentation standards**, emphasizing clarity, reproducibility, and realistic deployment patterns.

---

## 📚 Documentation

All design decisions, architecture diagrams, data flow explanations, and operational considerations live in the `/docs` directory.

👉 **Start here:** `docs/00-0_overview/00_project_overview.md`
