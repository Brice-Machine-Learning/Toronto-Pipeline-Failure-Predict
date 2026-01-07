# 🚰 Pipeline Break Prediction — Los Angeles Water

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

This project builds a **machine-learning–driven pipeline break risk platform** for the Los Angeles water distribution system using real, open municipal data.

It combines **civil engineering domain knowledge**, **geospatial analytics**, and **modern data science** to model pipeline failure risk and deliver **actionable insights** for infrastructure planning, asset management, and capital prioritization.

The system is designed as a **realistic analytics platform**, not a toy ML notebook — featuring batch ETL, persistent analytical storage, feature engineering pipelines, optional ML prediction, and BI-ready outputs.

---

## 🧠 Why This Project Matters

Urban water utilities face increasing pressure from:

- aging buried infrastructure  
- corrosive soils and geotechnical conditions  
- climate-driven stress (rainfall, drought, temperature swings)  
- deferred maintenance and constrained capital budgets  

Machine learning can help utilities:

- prioritize high-risk assets  
- reduce break frequency and service disruptions  
- justify capital investment decisions  
- transition from reactive to proactive maintenance  

This project demonstrates **how ML can be applied responsibly and defensibly** in infrastructure risk contexts — aligned with how utilities and consultants actually work.

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

- LADWP water main break datasets  
- Climate data (NOAA, PRISM)  
- Soil & corrosivity layers (USDA SSURGO, CA Geological Survey)  
- Neighborhood and census geographies  
- Automated ingestion and validation pipelines  

---

### 2️⃣ Exploratory Data Analysis (EDA)

- break frequency distributions  
- temporal seasonality  
- spatial patterns and clustering  
- environmental factor correlations
- temporal break trends  
- spatial clustering and hotspots  
- environmental correlations  
- data quality checks and anomaly detection  

---

### 3️⃣ Feature Engineering

A hybrid civil engineering + data science approach:

| Category | Example Features |
| ------- | ---------------- |
| Pipe Attributes | age, diameter, material |
| Environmental | rainfall, drought index, temperature |
| Geotechnical | soil corrosivity, shrink–swell |
| Spatial | neighborhood, proximity indicators |
| Temporal | seasonality, lagged break history |

---

### 4️⃣ Machine Learning (Batch)

- Supervised learning (classification / regression)  
- Time-aware train/test splits  
- Gradient boosting + baselines  
- SHAP-based interpretability  
- Batch scoring (not real-time inference)  

Outputs:

- break probability  
- risk score  
- feature importance  

---

### 5️⃣ Risk Scoring & Reporting

- utility-style risk tiers  
- ranked high-risk segments  
- monthly / annual scoring runs  
- BI-ready outputs  

---

### 6️⃣ Dashboards & Analytics (Power BI)

Planned dashboards include:

- breaks over time  
- environmental drivers  
- geographic risk heatmaps  
- neighborhood drilldowns  
- ML-based risk ranking  

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

Versions may evolve as data availability and scope mature, but architectural stability is maintained across releases.

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
