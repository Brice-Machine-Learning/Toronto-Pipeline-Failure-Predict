# 🚰 Pipeline Break Prediction (Los Angeles Water)  

## **Infrastructure Risk Modeling • Machine Learning • Geospatial Analytics**

**Status:** 🟡 *Scaffolding initialized — anticipated start December 2025.*

This project builds a **machine-learning–powered risk model** to predict pipeline break probability across Los Angeles using real open municipal datasets. The goal is to combine **civil engineering expertise**, **geospatial analysis**, and **modern data science** to demonstrate how ML can support urban water infrastructure planning and asset management.

---

## 🎯 Project Objectives

- Predict break likelihood for water distribution pipelines  
- Identify spatial and temporal break patterns  
- Integrate environmental + geotechnical features  
- Produce risk scores for proactive maintenance planning  
- Deliver actionable visualizations for utilities and decision-makers  

---

## 🧠 Why This Project Matters

Water utilities face increasing challenges from:

- aging buried infrastructure  
- corrosive soils  
- climate stress  
- deferred maintenance  
- pressure zone dynamics  

Machine learning can help utilities:

- prioritize capital replacement  
- target high-risk segments  
- justify funding  
- reduce breaks and service disruptions  

This project shows **how AI can support real infrastructure decisions** — with the kind of practical, defensible approach utilities require.

---

## 📦 Planned Project Components

### **1. Data Acquisition**

- Gather curated datasets from:
- LADWP water main break datasets  
- Climate data (NOAA, PRISM)  
- Soil & corrosivity layers (USDA SSURGO, California Geologic Survey)  
- Neighborhood + census geography (LA GeoHub)  
- Optional: elevation, seismicity, road load, land use  

---

### **2. Exploratory Data Analysis (EDA)**

- Summary statistics
- Breaks over time  
- Spatial clustering  
- Correlations with rainfall, temperature, drought  
- Neighborhood-level patterns  
- Data cleaning + anomaly checks  

---

### **3. Feature Engineering**

A blend of civil engineering + DS techniques:

| Category | Examples |
|---------|----------|
| **Pipe Attributes** | age, diameter, material, length |
| **Environmental** | rainfall, soil corrosivity, shrink-swell index |
| **Geospatial** | neighborhood, pressure zone proxy, road classification |
| **Temporal** | seasonality, year/month, lag features |

---

### **4. Geospatial Processing**

Techniques to derive spatial features:

- Spatial joins  
- Choropleths + kernel density maps  
- Neighborhood risk overlays  
- Environmental layer integration  
- Optional: point-to-line distance features  

---

### **5. Predictive Modeling**

Modeling approach:

- Supervised learning (classification/regression)
- Target: monthly break occurrence/count per segment
- Evaluation metrics: ROC-AUC, PR-AUC, RMSE
- Train/test split with temporal holdout  
- Cross-validation strategy (time-aware)

Candidate models:

- Gradient boosting (XGBoost, LightGBM, CatBoost)  
- Logistic regression (baseline)  
- Random forest  
- Time-aware CV + walk-forward validation  

Output:

- Probability of break (0–1)  
- Risk score  
- Feature importance + SHAP interpretability  

---

### **6. Risk Scoring Framework**

Define actionable risk tiers based on predicted probabilities.
Deliverables:

- Utility-style risk tiers (Low / Medium / High / Critical)  
- Ranking tables  
- Monthly or yearly predictions  
- Sensitivity analysis  

---

### **7. Dashboards & Reporting**

(Power BI integration planned)

- Breaks over time  
- Environmental drivers  
- Heatmaps / hotspot maps  
- Predicted risk ranking  
- Neighborhood drilldowns  

---

## 🏗️ Technical Stack

### **Languages & Tools**

- Python (pandas, numpy, matplotlib, scikit-learn, geopandas, shapely, xgboost/lightgbm)
- PostgreSQL + PostGIS  
- Power BI  
- Jupyter Notebooks / VS Code  
- GitHub project management  

---

## 📁 Project Structure

```plaintext
la-pipeline-break-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_risk_scoring.ipynb
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── visualization/
│
├── powerbi/
│   ├── model/
│   └── reports/
│
├── docs/
│   ├── overview.md
│   ├── data_sources.md
│   ├── powerbi_data_model.md
│   ├── feature_engineering_plan.md
│   └── risk_framework.md
│
└── README.md
```

---

## 🚀 Roadmap

### **Phase 1 — Setup & EDA (Starting Dec 2025)**  

- [x] Repo scaffold  
- [ ] Data acquisition  
- [ ] Initial EDA  

### **Phase 2 — Feature Engineering**  

- [ ] Asset + environmental feature build  
- [ ] Geospatial joins  
- [ ] Climate integration  

### **Phase 3 — Modeling**  

- [ ] Baseline models  
- [ ] Gradient boosting models  
- [ ] SHAP interpretability  

### **Phase 4 — Risk Framework**  

- [ ] Scoring system  
- [ ] High-risk segment identification  
- [ ] Reporting templates  

### **Phase 5 — Dashboards**  

- [ ] Power BI dataset build  
- [ ] Interactive visuals  
- [ ] Publishing  

---

## 📬 Status & Notes

Full development begins **December 2025** once the current Kaggle competition is complete.  
The project is being set up to follow a **clean, senior-level structure** with clear documentation, modular code, and reproducible workflows.
