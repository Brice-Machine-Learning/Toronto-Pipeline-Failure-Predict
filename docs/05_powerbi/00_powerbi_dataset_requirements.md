# 📦 Power BI Dataset Requirements  

>*LA Pipe Break Analytics Project*

This document defines the **fields, structure, relationships, refresh expectations, and model constraints** needed for Power BI to properly visualize pipeline break trends and environmental drivers.

---

## 1. 🎯 Core Goals of the Dataset

Power BI must be able to:

1. Visualize monthly break trends  
2. Compare environmental factors vs break frequency  
3. Map break hotspots geographically  
4. Allow filtering by:  
   - Year  
   - Month  
   - Neighborhood  
   - Soil Zone  
   - Climate conditions  
5. Optionally integrate ML risk scores  

To support that, the dataset needs **clean, joined, time-aligned tables**.

---

## 2. 📁 Required Tables

### **2.1 `pipe_breaks` (Fact Table)**

| Column       | Type    | Required | Description              |
| ------------ | ------- | -------- | ------------------------ |
| id           | integer | ✓        | Unique identifier        |
| break_date   | date    | ✓        | Actual break date        |
| year         | integer | ✓        | Extracted via ETL        |
| month        | integer | ✓        | Extracted via ETL        |
| neighborhood | text    | ✓        | Mapped location          |
| break_count  | int     | ✓        | Monthly aggregated count |

---

### **2.2 `climate_monthly` (Dimension Table)**

| Column        | Type  | Required |
| ------------- | ----- | -------- |
| year          | int   | ✓        |
| month         | int   | ✓        |
| rainfall_mm   | float | ✓        |
| mean_temp_c   | float | ✓        |
| drought_index | float | optional |

---

### **2.3 `soil_zones` (Dimension Table)**

| Column            | Type  | Required |
| ----------------- | ----- | -------- |
| zone_code         | text  | ✓        |
| neighborhood      | text  | ✓        |
| corrosivity_index | float | ✓        |

---

### **2.4 `joined_risk_view` (Optional Fact Table)**

| Column               | Type  | Required |
| -------------------- | ----- | -------- |
| year                 | int   | ✓        |
| month                | int   | ✓        |
| predicted_break_prob | float | optional |
| risk_class           | text  | optional |

---

## 3. 🔗 Required Relationships

```plaintext
pipe_breaks
 ├── year/month → climate_monthly
 ├── neighborhood → soil_zones
 └── (optional) year/month → joined_risk_view
```

Relationship model type: **Star Schema**

---

## 4. 🗂 Required Calculated Columns (Power BI DAX)

### **MonthName**

```plaintext
MonthName = FORMAT('pipe_breaks'[break_date], "MMMM")
```

### **YearMonth**

```plaintext
YearMonth = FORMAT('pipe_breaks'[break_date], "YYYY-MM")
```

### **Rolling 12-Month Breaks**

```plaintext
Rolling12Breaks =
CALCULATE(
    SUM('pipe_breaks'[break_count]),
    DATESINPERIOD('Date'[Date], LASTDATE('Date'[Date]), -12, MONTH)
)
```

**Requirement:** Add a proper **Date** table.

---

## 5. 🧼 Data Quality Requirements

| Requirement                                 | Why                             |
| ------------------------------------------- | ------------------------------- |
| No null month/year values                   | Breaks date hierarchy           |
| Standardized neighborhood names             | Required for joins              |
| No duplicate months per neighborhood        | Ensures trend accuracy          |
| Climate data aligned to monthly granularity | Prevents incorrect correlations |
| Soil zones mapped                           | Enables environmental slicing   |

---

## 6. 🔄 Refresh & Performance Expectations

### Refresh

- Local: manual  
- Service: daily recommended  
- Climate: monthly updates  
- Soil/geotech: rarely changes  

### Performance

- Dataset < 1M rows  
- Fact tables numeric & clean  
- Dimension tables small (<20 cols)

---

## 7. 📌 Required DAX Measures

### Total Breaks

```plaintext
TotalBreaks = SUM('pipe_breaks'[break_count])
```

### Breaks vs Rainfall

```plaintext
BreaksPerInchRain =
DIVIDE([TotalBreaks], SUM('climate_monthly'[rainfall_mm]))
```

### ML Risk (optional)

```plaintext
AverageRisk = AVERAGE('joined_risk_view'[predicted_break_prob])
```

---

## 8. ✔️ Required Capabilities

### Must Support

- Filtering by neighborhood, year, month  
- Line charts for break trends  
- Maps/heatmaps  
- Environmental comparisons  

### Optional

- ML risk integration  
- Risk ranking  
- Drilldowns by zone

---

## 9. 📥 Required Input Files (from ETL)

```plaintext
pipe_breaks.csv
climate_monthly.csv
soil_zones.csv
joined_risk_view.csv (optional)
```

Format:

- `YYYY-MM-DD` dates  
- lowercase snake_case  
- consistent column names  
