# 📊 Los Angeles Pipe Break ML Project — Data Sources (Curated List)

Building a realistic pipe-break prediction model for Los Angeles means gathering **event data**, **pipe-asset metadata**, and **environmental/spatial layers**.  
Below is a curated, **high-quality** set of datasets — with descriptions, direct links, and notes on how you’d use each one in your ML pipeline.

---

## 🧩 1. Water Main Breaks — Monthly Events (LA DWP)

**Source:** City of Los Angeles LADWP via Data.gov  
**Format:** CSV, JSON, XML  

**Link:**

- <https://catalog.data.gov/dataset/water-main-breaks-in-the-city-of-los-angeles-each-month>

**What it contains:**  

- Monthly counts of water main breaks across the City of LA.  
- Historical time series (multi-year).  
- Useful if you're modelling *break volume* or doing temporal forecasting.

**Use in ML:**  

- Primary *target variable* for supervised learning.
- Target variable foundation: break likelihood by area + month.  
- Combine with asset features for supervised learning.

---

## 🧩 2. Water System Layers — Pipelines, Valves, Treatment  

**Source:** County of Los Angeles Open Data (GIS layers)  

**Link:**  

- [Water System Layers - LA County Open Data](https://data.lacounty.gov)
- (search “water”, “pipeline”, “distribution”, “hydrology”)

**What it contains:**  

- GeoJSON / shapefile layers for water distribution features.  
- Includes pipe alignments, zones, service boundaries, etc.

**Use in ML:**  

- Core *asset* features:  
  - Pipe geometry  
  - Region/neighborhood  
  - Length, alignment, depth (if available)  
  - Pressure zones  
- Enables **spatial joins** with soil, seismic, and sociodemographic layers.

---

## 🧩 3. Soil & Groundwater Data (Geotechnical & Corrosivity Indicators)

**Source:** USDA NRCS + California Geologic Survey  

**Links:**  

- [USDA SSURGO soils database](https://sdmdataaccess.sc.egov.usda.gov)  
- [CA Geologic Survey (geologic layers)](https://maps.conservation.ca.gov)  

**What it contains:**  

- Soil type, corrosivity, moisture, shrink/swell index.  
- Groundwater depth, geomorphology, seismic overlays.

**Use in ML:**  

- Key environmental features:
- Soil corrosivity → **top predictor** in real pipe-failure studies.  
- Flooding risk, liquefaction, soil movement → environmental stressors.  
- Join via spatial intersection on pipe geometry.

---

## 🧩 4. LA Neighborhood, Census, and Socio-Infrastructure Data  

**Source:** LA GeoHub + Census TIGER + LA City Planning  

**Links:**  

- [LA GeoHub](https://geohub.lacity.org)  
- [Census TIGER/ACS](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)  

**What it contains:**  

- ZIP codes, neighborhood boundaries, street maps.  
- Demographics, land use, transportation layers.

**Use in ML:**  

- Create contextual features:  
  - Road class → overburden & vibration stress  
  - Land use → industrial vs residential load  
  - Age of development → proxy for pipe age if no asset metadata

---

## 🧩 5. Climate, Rainfall, Temperature, Drought Indicators  

**Source:** NOAA + PRISM Climate Group  

**Links:**  

- [NOAA Climate Data](https://www.ncei.noaa.gov)  
- [PRISM (high-res LA climate data)](https://prism.oregonstate.edu)

**What it contains:**  

- Daily/Monthly rainfall, temperature, freeze-thaw cycles.  
- Multi-decadal climate normals.

**Use in ML:**  

- Environmental stress predictors:
- Temperature swings → pipe material fatigue.  
- Rainfall → infiltration → soil corrosivity acceleration.  
- Seasonal predictors for break spikes.

---

## 🏗️ Recommended Feature Matrix (What Your Model Will Need)

| Category | Example Variables | Source |
|---------|-------------------|--------|
| **Pipe Physical Attributes** | Material, diameter, age, install year, length | LA Open Data (if available) |
| **Environmental Stress** | Soil corrosivity, shrink/swell, groundwater | SSURGO / CGS |
| **Climate** | Rainfall, drought severity, freeze range | NOAA / PRISM |
| **Spatial Context** | Road class, traffic load, land use | LA GeoHub |
| **Break History** | Annual/monthly failures, cluster patterns | LADWP monthly break dataset |

If LA doesn’t release asset-level pipe metadata (common for utilities), you can:  

- Reconstruct approximate “pipe age” using parcel development age  
- Infer material by decade (common in water industry: cast iron <1970, PVC >1980)  
- Use spatial patterns to approximate pressure zones  
This still produces a credible, publishable, resume-worthy ML project.

---
