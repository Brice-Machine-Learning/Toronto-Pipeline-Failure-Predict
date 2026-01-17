# Phase 0 — Stakeholders & Analytical Use Cases

## Purpose of This Document

This document identifies the **primary stakeholders** for the LA Pipeline Break Analytics & Risk Platform and defines the **analytical use cases** the platform is intended to support.

The goal is to ensure that all analytics, data modeling, and visualization decisions are traceable to **real user needs**, rather than abstract technical objectives.

---

## 1. Primary Stakeholders

### 1.1 Utility Analysts

**Role:**  
Internal analysts responsible for reviewing historical infrastructure performance and preparing reports for management.

**Needs:**

- Clean, reliable datasets
- Consistent time-series aggregation
- Ability to filter and compare across years and locations
- Clear visualization of trends and anomalies

**How the Platform Supports Them:**

- Modeled fact and dimension tables
- Power BI dashboards with time-based slicing
- Standardized metrics and definitions

---

### 1.2 Infrastructure Planners & Engineers

**Role:**  
Engineering staff involved in long-term capital planning and infrastructure assessment.

**Needs:**

- Understanding where failures are concentrated
- Insight into environmental and geotechnical drivers
- Context for prioritizing further investigation or studies

**How the Platform Supports Them:**

- Geographic hotspot analysis
- Environmental correlation views
- Neighborhood-level comparisons over time

---

### 1.3 Engineering & Operations Management

**Role:**  
Managers responsible for overseeing system performance and communicating risk to leadership.

**Needs:**

- High-level summaries
- Defensible, data-backed narratives
- Clear visuals suitable for presentations

**How the Platform Supports Them:**

- Executive-ready dashboards
- Aggregated KPIs and trend summaries
- Visual storytelling through maps and charts

_**KPI Definition and Characteristics**

A **KPI (Key Performance Indicator)** is a measurable value that demonstrates how effectively an organization is achieving key business objectives. KPIs are used to evaluate success at reaching targets.

Five Characteristics of a Good KPI:

1. **Specific**: Clearly defined and focused on a particular aspect of performance, leaving no room for ambiguity about what is being measured.

2. **Measurable**: Quantifiable with concrete data, allowing for objective tracking and comparison over time.

3. **Achievable**: Realistic and attainable given available resources and constraints, while still challenging enough to drive improvement.

4. **Relevant**: Directly aligned with strategic business objectives and provides actionable insights that matter to stakeholders.

5. **Time-bound**: Associated with a specific timeframe for achievement, enabling progress tracking and accountability.

---

### 1.4 Consulting & Advisory Teams

**Role:**  
External or internal consultants supporting utilities with analytics, planning, or reporting.

**Needs:**

- Transparent assumptions
- Reproducible workflows
- Well-documented data pipelines and models

**How the Platform Supports Them:**

- Modular ETL pipelines
- Documented schemas and transformations
- Clear separation between raw, processed, and modeled data

---

## 2. Core Analytical Use Cases

### 2.1 Historical Trend Analysis

**Question:**  
How have water main break frequencies changed over time?

**Supported Analysis:**

- Monthly and annual break trends
- Year-over-year comparisons
- Rolling averages to smooth variability

---

### 2.2 Seasonality & Temporal Patterns

**Question:**  
Are breaks more common during specific months or seasons?

**Supported Analysis:**

- Monthly distributions
- Seasonal overlays
- Comparison of different years under similar conditions

---

### 2.3 Geographic Hotspot Identification

**Question:**  
Where are breaks concentrated spatially?

**Supported Analysis:**

- Neighborhood-level aggregation
- Heatmaps and spatial comparisons
- Persistent vs transient hotspot identification

---

### 2.4 Environmental Driver Correlation

**Question:**  
How do climate and soil conditions relate to break frequency?

**Supported Analysis:**

- Rainfall vs break frequency comparisons
- Temperature trends vs failure rates
- Soil corrosivity overlays by neighborhood

---

### 2.5 Comparative Neighborhood Analysis

**Question:**  
Which neighborhoods consistently experience higher break rates?

**Supported Analysis:**

- Normalized break rates
- Cross-neighborhood comparisons
- Identification of outliers for further investigation

---

## 3. Explicitly Out-of-Scope Use Cases

The platform does **not** support:

- real-time operational monitoring
- dispatch or maintenance scheduling
- asset-level failure prediction
- automated decision-making

These exclusions are intentional and documented in the Phase 0 Non-Goals.

---

## 4. Design Implications

These stakeholders and use cases directly inform:

- data aggregation level (monthly, neighborhood-scale)
- schema design and relationships
- Power BI model structure
- dashboard layout and filtering options

Any future expansion of scope must demonstrate alignment with these documented user needs.

---

## Phase 0 Checklist Status

- [x] Primary stakeholders identified  
- [x] Core analytical use cases defined  
- [x] Out-of-scope use cases acknowledged  
