# 📊 Toronto Water Main Break ML Project — Data Sources (Curated List)

Building a realistic pipe-break prediction model for the **City of Toronto** requires integrating **failure event data**, **asset-level infrastructure attributes**, and **environmental + geospatial context**.

Toronto’s open data ecosystem is unusually strong for infrastructure analytics, making it well-suited for a **defensible, publishable ML project** rather than a toy demo.

Below is a curated, **high-quality** set of datasets — with descriptions, direct links, and notes on how each feeds your analytics and ML pipeline.

---

## 🧩 1. Water Main Breaks — Historical Events (City of Toronto)

**Source:** City of Toronto Open Data Portal  
**Format:** CSV, GeoJSON  

**Link:**  
<https://www.toronto.ca/city-government/data-research-maps/open-data/>

**What it contains:**

- Detailed historical water main break records  
- Event-level data (location, date, break type where available)  
- Multi-decade coverage  
- Spatially precise (GIS-ready)

**Use in ML:**

- **Primary target variable** for supervised learning  
- Supports:
  - event-level modeling  
  - aggregation to monthly / neighborhood units  
- Enables:
  - time-series features  
  - rolling failure rates  
  - spatial clustering analysis  

---

## 🧩 2. Water Infrastructure Assets — Age, Material, Diameter

**Source:** City of Toronto Open Data Portal  
**Format:** GIS (shapefiles / GeoJSON), tabular  

**Link:**  
<https://www.toronto.ca/city-government/data-research-maps/open-data/>

**What it contains:**

- Water main alignments  
- Installation year  
- Pipe material  
- Diameter  
- Asset ownership and system classification  

**Use in ML:**

- **Core asset features**:
  - Pipe age  
  - Material (CI, DI, PVC, etc.)  
  - Diameter  
- Eliminates decade-based inference used in many U.S. datasets  
- Enables **true asset-level risk modeling**

---

## 🧩 3. GIS Water System & Hydrology Layers

**Source:** City of Toronto Open Data + Toronto Maps  
**Format:** GIS  

**Links:**  
<https://www.toronto.ca/city-government/data-research-maps/maps/>  
<https://www.toronto.ca/city-government/data-research-maps/open-data/learning-resources/>

**What it contains:**

- Water distribution zones  
- Watersheds and drainage areas  
- Surface hydrology  
- Elevation-related spatial context  

**Use in ML:**

- Spatial context features:
  - watershed influence  
  - drainage patterns  
  - hydraulic context  
- Enables spatial joins with:
  - soil  
  - climate  
  - break history  

---

## 🧩 4. Neighborhood Boundaries & Urban Context

**Source:** City of Toronto Open Data + Neighbourhood Profiles  
**Format:** GIS + tabular  

**Links:**  
<https://www.toronto.ca/city-government/data-research-maps/open-data/>  
<https://www.toronto.ca/city-government/data-research-maps/neighbourhoods-communities/neighbourhood-profiles/>

**What it contains:**

- Official neighborhood boundaries  
- Community profiles  
- Land use and development characteristics  

**Use in ML:**

- Aggregation units for:
  - monthly failure rates  
  - risk scoring  
- Contextual features:
  - development era  
  - density  
  - road network stress proxies  

---

## 🧩 5. Soil, Geotechnical & Geological Data (Ontario)

**Source:**  

- Ontario Geological Survey  
- Natural Resources Canada  
- Ontario Soil Survey  

**Links:**  
<https://www.ontario.ca/page/soil-data>  
<https://data.ontario.ca/dataset/soil-survey-database-of-ontario>  
<https://www.geologyontario.mndm.gov.on.ca/ogsearth.html>  
<https://natural-resources.canada.ca/>

**What it contains:**

- Soil classification  
- Geologic units  
- Ground conditions  
- Moisture and material properties  

**Use in ML:**

- Environmental stress features:
  - soil type  
  - geologic conditions  
  - ground movement susceptibility  
- Joined spatially to pipe geometry  

---

## 🧩 6. Soil Corrosivity Indicators

**Source:** Natural Resources Canada + Ontario datasets  

**Links:**  
<https://www.nrcan.gc.ca/our-natural-resources/earth-sciences/geomatics/geospatial-products-services/soil-information/10985>  
<https://open.canada.ca/data/en/dataset/3c6f4f5e-2d17-4f10-8f10-5a2b2f2c6f3e>  

**What it contains:**

- Corrosion-related soil properties  
- Chemical and moisture indicators  
- Regional soil behavior data  

**Use in ML:**

- **One of the strongest predictors** of pipe failure  
- Enables:
  - material-specific degradation modeling  
  - interaction features (material × soil)  

---

## 🧩 7. Climate & Freeze–Thaw Indicators (Toronto)

**Source:** Environment and Climate Change Canada + academic datasets  

**Links:**  
<https://climate.weather.gc.ca/>  
<https://climatedata.ca/>  
<https://lamps.math.yorku.ca/OntarioClimate/>  
<https://www.timeanddate.com/weather/canada/toronto/climate/>  

**What it contains:**

- Daily and monthly temperature  
- Freeze–thaw cycles  
- Snowfall and precipitation  
- Long-term climate normals  

**Use in ML:**

- Seasonal stress predictors:
  - freeze–thaw frequency  
  - extreme cold events  
- Particularly valuable for:
  - cast iron  
  - older metallic mains  

---

## 🏗️ Recommended Feature Matrix (Toronto-Specific)

| Category | Example Variables | Source |
| -------- | ------------------ | -------- |
| **Pipe Physical Attributes** | Material, diameter, install year, age | Toronto Open Data |
| **Failure History** | Prior breaks, rolling failure rates | Toronto Break Dataset |
| **Environmental Stress** | Soil corrosivity, geology | OGS / NRCan |
| **Climate** | Freeze–thaw cycles, temperature range | ECCC |
| **Spatial Context** | Neighborhood, watershed | Toronto GIS |

---

## 📌 Why Toronto Strengthens This Project

Unlike many U.S. cities:

- Asset metadata is available and consistent  
- Soil and geological datasets are accessible  
- Climate stressors are meaningful  
- Neighborhood boundaries are stable and well-defined  

This allows the project to move beyond spatial clustering and toward **causal, defensible infrastructure risk modeling**.

Toronto enables a model that explains **why failures occur**, not just **where they cluster** — aligning the work with how utilities and infrastructure analytics teams actually operate.
