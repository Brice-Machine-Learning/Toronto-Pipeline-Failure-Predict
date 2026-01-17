# 📊 LA Water Main Break Analytics & Risk Platform  

## **Power BI + PostgreSQL + Python ETL**

This project creates an analytics and visualization platform for **water main break trends** in Toronto, using **Power BI**, **PostgreSQL**, and **Python ETL pipelines**. It blends civil engineering domain knowledge with backend engineering and data analytics — aligned with how utilities manage infrastructure risk in practice.

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
        Public Datasets
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

### **Water Main Breaks**

<https://www.toronto.ca/city-government/data-research-maps/open-data/>

### **Infrastructure Age & Material**

<https://www.toronto.ca/city-government/data-research-maps/open-data/>

### **Hydrology & Watersheds**

<https://www.toronto.ca/city-government/data-research-maps/open-data/>

### **Toronto City Maps**

<https://www.toronto.ca/city-government/data-research-maps/maps/>

### **GIS Water System Layers**

<https://www.toronto.ca/city-government/data-research-maps/open-data/learning-resources/>

### **Neighborhood Boundaries**

<https://www.toronto.ca/city-government/data-research-maps/open-data/>
<https://www.toronto.ca/city-government/data-research-maps/neighbourhoods-communities/neighbourhood-profiles/find-your-neighbourhood/#location=&lat=&lng=&zoom=>

### **Soil & Geotechnical**

<https://www.ontario.ca/page/soil-data>
<https://library.torontomu.ca/gmdc/old-gmdc/geo-data/search-2/>
<https://data.ontario.ca/dataset/ontario-geological-survey-geological-maps-and-digital-data-index>
<https://www.geologyontario.mndm.gov.on.ca/ogsearth.html>

### **Soil Corrosivity**

<https://www.nrcan.gc.ca/our-natural-resources/earth-sciences/geomatics/geospatial-products-services/soil-information/10985>
<https://open.canada.ca/data/en/dataset/3c6f4f5e-2d17-4f10-8f10-5a2b2f2c6f3e>
<https://data.ontario.ca/dataset/soil-survey-database-of-ontario>
<https://www.ontario.ca/page/ontario-geological-survey>
<https://natural-resources.canada.ca/>

### **Climate**

<https://en.climate-data.org/north-america/canada/ontario/toronto-53/>  
<https://www.weather-atlas.com/en/canada/toronto-climate>
<https://www.timeanddate.com/weather/canada/toronto/climate>
<https://weatherandclimate.com/canada/ontario/toronto>  
<https://climate.weather.gc.ca/>  
<https://climatedata.ca/>
<https://lamps.math.yorku.ca/OntarioClimate/>

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
