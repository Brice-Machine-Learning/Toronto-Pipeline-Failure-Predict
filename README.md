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

### Phase 1 — Scaffolding & EDA

- [x] Repository structure
- [x] Architecture documentation
- [ ] Data ingestion
- [ ] Initial EDA

### Phase 2 — Feature Engineering

- [ ] Environmental + asset features
- [ ] Geospatial joins
- [ ] Climate integration

### Phase 3 — Modeling

- [ ] Baseline models
- [ ] Gradient boosting
- [ ] Interpretability (SHAP)

### Phase 4 — Risk Framework

- [ ] Risk tiers
- [ ] Ranking logic
- [ ] Reporting outputs

### Phase 5 — Dashboards & Deployment

- [ ] Power BI datasets
- [ ] Dashboards
- [ ] Scheduled batch runs

---

## 📬 Project Status

**Status:** Active scaffolding and documentation phase  
**Full development:** Begins December 2025  

The project is being built with **senior-level structure and documentation standards**, emphasizing clarity, reproducibility, and realistic deployment patterns.

---

## 📚 Documentation

All design decisions, architecture diagrams, data flow explanations, and operational considerations live in the `/docs` directory.

👉 **Start here:** `docs/00_overview/00_project_overview.md`
