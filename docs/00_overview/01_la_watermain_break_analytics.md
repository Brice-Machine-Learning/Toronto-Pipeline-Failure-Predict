# 📊 LA Water Main Break Analytics & Risk Platform  

## **Power BI + PostgreSQL + Python ETL**

This project creates an analytics and visualization platform for **water main break trends** in Los Angeles, using **Power BI**, **PostgreSQL**, and **Python ETL pipelines**. It blends civil engineering domain knowledge with backend engineering and data analytics — aligned with how utilities manage infrastructure risk in practice.

---

## ⭐ Why This Project Works So Well

### **1. Real municipal infrastructure data**

Water main breaks have:

- spatial patterns  
- seasonal patterns  
- environmental drivers (soil, climate, infrastructure age)  

This makes the problem *inherently visual*, *predictive*, and *business-critical* — perfect for dashboards and analytics.

### **2. Strong Power BI use case**

Utilities and public agencies heavily rely on:

- Power BI  
- SQL Server / PostgreSQL  
- Geospatial layers (GeoJSON, shapefiles)  

A dashboard summarizing water main breaks is something many city departments would actually deploy.

### **3. Hybrid skill demonstration**

This project highlights:

- Database design  
- Python ETL  
- Spatial joins  
- Power BI data modeling  
- Civil engineering domain knowledge  
- Optional ML (pipe break risk prediction)  

You end up with a multi-layer portfolio piece.

---

## 🛠️ Recommended Architecture

```pgsql
        LA Public Datasets
            | (CSV/GeoJSON)
            ▼
        Python ETL Scripts
            ▼
       PostgreSQL Database (local or RDS)
            ▼
     Power BI Desktop → Publish to PowerBI Service
            ▼
       Dashboards, KPIs, Heatmaps
```

This mirrors a real infrastructure analytics pipeline used by utilities.

---

## 🧱 Proposed Database Schema

Schema: `pipe_risk`

### **1. `pipe_breaks`**

Break event data from LADWP.

| column       | type   | notes                |
|--------------|--------|----------------------|
| id           | serial | pk                   |
| break_date   | date   |                      |
| month        | int    | derived              |
| year         | int    | derived              |
| neighborhood | text   | from dataset/join    |
| break_count  | int    | from source dataset  |

### **2. `climate_monthly`**

Monthly PRISM/NOAA rainfall + temperature.

| column        | type   |
|---------------|--------|
| id            | serial |
| year          | int    |
| month         | int    |
| rainfall_mm   | float  |
| mean_temp_c   | float  |
| drought_index | float  |

### **3. `soil_zones`**

Corrosivity and geotechnical indicators.

| column            | type   |
|-------------------|--------|
| id                | serial |
| zone_code         | text   |
| description       | text   |
| corrosivity_index | float  |

### **4. `joined_risk_view`**

Materialized view used by Power BI.

Contains:

- month, year  
- break_count  
- rainfall, temperature  
- soil corrosivity  
- The initial focus is descriptive and diagnostic analytics, with predictive modeling introduced incrementally risk score  

---

## 📊 Power BI Dashboard Concepts

### **1. Breaks Over Time Dashboard**

- Line chart: monthly breaks  
- Rolling 12-month trend  
- Year-over-year seasonality  

### **2. Environmental Drivers Dashboard**

- Rainfall vs breaks  
- Temperature vs breaks  
- Soil corrosivity comparison  

### **3. Geographic Hotspots Dashboard**

- Neighborhood map  
- Break frequency heatmap  
- Historical clusters  

### **4. Predictive Risk Dashboard (Optional)**

- Probability of break (ML model)  
- Ranking of highest-risk zones  
- Interactive filters (year, soil zone, climate)  

---

## 🧩 Data Sources

### **Water Main Breaks (LADWP)**

<https://catalog.data.gov/dataset/water-main-breaks-in-the-city-of-los-angeles-each-month>

### **GIS Water System Layers**

<https://data.lacounty.gov>

### **Soil & Geotechnical**

<https://sdmdataaccess.sc.egov.usda.gov>
<https://maps.conservation.ca.gov>

### **Climate (NOAA + PRISM)**

<https://www.ncei.noaa.gov>  
<https://prism.oregonstate.edu>

---

## 📁 Suggested Repo Structure

See the [architecture docs](../01_architecture/01_structure.md) for a full breakdown of the project structure.

---

## 🎯 A Strategic Power BI Analytics Project

This project:

- uses **real data**  
- uses **a real database**  
- requires **ETL and schema design**  
- builds **real-world dashboards**  
- incorporates **environmental + engineering** features  
- can expand into **ML prediction**  
- similar in scope to analytics dashboards utilities often procure from external consultants

>The perfect bridge between civil engineering background and backend/data/ML.
