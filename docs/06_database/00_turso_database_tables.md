# 📦 Recommended Turso Database Tables

This document defines the recommended **v1 database schema** for the **Toronto Water Main Break Analytics & Risk Platform**.  
The schema is designed to support **analytics-first workflows**, **batch ML execution**, and **Power BI consumption**.

---

## 🎯 Design Principles

The database is intended to:

- act as the **system of record** for analytics and ML outputs  
- store **curated data**, not raw CSVs  
- support **batch ML**, not real-time inference  
- be directly consumable by **Power BI**  

---

## ✅ Core Analytics Tables

### 1️⃣ `pipe_breaks_clean`

Canonical fact table for historical water main breaks.

```sql
pipe_breaks_clean (
    break_id            INTEGER PRIMARY KEY,
    break_date          DATE,
    year                INTEGER,
    month               INTEGER,
    neighborhood        TEXT,
    break_count         INTEGER,
    latitude            REAL,
    longitude           REAL,
    source              TEXT,
    ingestion_timestamp TIMESTAMP
)
```

---

### 2️⃣ `climate_monthly`

Monthly environmental indicators.

```sql
climate_monthly (
    year            INTEGER,
    month           INTEGER,
    rainfall_mm     REAL,
    mean_temp_c     REAL,
    drought_index   REAL,
    source          TEXT
)
```

---

### 3️⃣ `soil_zones`

Geotechnical and corrosivity reference data.

```sql
soil_zones (
    zone_id             INTEGER PRIMARY KEY,
    neighborhood        TEXT,
    zone_code           TEXT,
    description         TEXT,
    corrosivity_index   REAL
)
```

---

### 4️⃣ `neighborhoods` (Optional)

Lookup and spatial context table.

```sql
neighborhoods (
    neighborhood_id INTEGER PRIMARY KEY,
    name            TEXT,
    region          TEXT,
    geometry_wkt    TEXT
)
```

---

## 🔑 Machine Learning Tables

### 5️⃣ `pipe_features_monthly`

Analytics-ready feature table used for training and scoring.

```sql
pipe_features_monthly (
    year                    INTEGER,
    month                   INTEGER,
    neighborhood            TEXT,
    break_count_rolling_12  REAL,
    avg_rainfall_6mo        REAL,
    avg_temp_6mo            REAL,
    soil_corrosivity        REAL,
    prior_break_rate        REAL,
    feature_version         TEXT,
    generated_at            TIMESTAMP
)
```

---

### 6️⃣ `pipe_break_risk_scores`

Persisted ML predictions for BI consumption.

```sql
pipe_break_risk_scores (
    year                INTEGER,
    month               INTEGER,
    neighborhood         TEXT,
    risk_score           REAL,
    risk_class           TEXT,
    model_version        TEXT,
    prediction_timestamp TIMESTAMP
)
```

---

## 📦 Metadata & Governance (Optional)

### 7️⃣ `model_metadata`

Tracks model versions and training context.

```sql
model_metadata (
    model_version       TEXT PRIMARY KEY,
    model_type          TEXT,
    training_start_date DATE,
    training_end_date   DATE,
    features_version    TEXT,
    metrics_json        TEXT
)
```

---

### 8️⃣ `etl_runs`

Operational visibility into ETL executions.

```sql
etl_runs (
    run_id              INTEGER PRIMARY KEY,
    pipeline_name       TEXT,
    run_timestamp       TIMESTAMP,
    status              TEXT,
    row_count           INTEGER,
    notes               TEXT
)
```

---

## 📊 Power BI Consumption

Power BI should primarily connect to:

- `pipe_breaks_clean`
- `pipe_break_risk_scores`
- `climate_monthly`
- `soil_zones`

Optional convenience view:

```sql
CREATE VIEW joined_risk_view AS
SELECT
    r.year,
    r.month,
    r.neighborhood,
    r.risk_score,
    r.risk_class,
    c.rainfall_mm,
    c.mean_temp_c,
    s.corrosivity_index
FROM pipe_break_risk_scores r
JOIN climate_monthly c USING (year, month)
JOIN soil_zones s USING (neighborhood);
```

---

## 🏁 Summary

This schema provides:

- a deployable analytics datastore  
- clean separation between ETL, ML, and BI  
- reproducible, auditable ML workflows  
- zero overengineering  

It represents a realistic **v1 production schema** suitable for Turso deployment.
