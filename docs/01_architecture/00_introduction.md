# Architecture Introduction

This document introduces the **architecture of the Toronto Water Main Break Analytics & Risk Platform** and explains the design decisions that govern how data moves through the system — from raw municipal datasets to analytics-ready dashboards and risk scores.

The architecture is intentionally designed to reflect **real-world utility analytics environments**, where data engineering, analytics, and business intelligence are tightly integrated, while machine learning is typically executed in **batch workflows**, not real-time services.

---

## Architectural Objectives

The primary objectives of the system architecture are to:

- support **repeatable, auditable data pipelines**
- provide a **persistent analytical datastore** for BI and ML
- enable **analytics-first data modeling** optimized for Power BI
- separate **ingestion, transformation, modeling, and consumption**
- allow incremental expansion into **predictive risk scoring**
- remain understandable, lightweight, and maintainable over time  

Rather than optimizing for real-time inference or streaming architectures, the system prioritizes **clarity, reproducibility, and stakeholder-facing analytics**, which better align with infrastructure risk analysis use cases.

---

## High-Level Architecture Overview

At a high level, the platform consists of four primary layers:

1. **Data ingestion and transformation (Python ETL)**
2. **Analytical storage (database layer)**
3. **Modeling and risk scoring (batch ML)**
4. **Business intelligence and visualization (Power BI)**

Each layer has a clearly defined responsibility and communicates through well-defined data contracts.

---

## Database Strategy

### Purpose of the Database Layer

The database serves as the **system of record** for the platform.  
It does **not** execute machine learning models directly. Instead, it:

- stores curated, analytics-ready datasets
- persists engineered features
- stores model outputs and risk scores
- provides a stable interface for Power BI consumption

This design ensures that analytics and ML outputs are **reproducible, inspectable, and deployable**, even though models are trained and executed in Python.

---

### Local Development vs Deployed Storage

The platform intentionally distinguishes between **local development workflows** and **deployed analytics storage**.

#### DuckDB (Local Development)

DuckDB is used during development for:

- exploratory data analysis (EDA)
- rapid feature engineering iteration
- local experimentation and validation

DuckDB acts as a **local analytical engine**, optimized for fast iteration, but it is not treated as a deployed system of record.

---

#### Turso (Deployed Database)

For deployment, the platform uses **Turso (libSQL)** as a lightweight, hosted database.

Turso is used to:

- persist curated datasets and feature tables
- store model predictions and metadata
- serve as the data source for Power BI dashboards
- support scheduled or on-demand batch ML workflows

This approach provides a **deployable, network-accessible datastore** without introducing unnecessary infrastructure complexity.

---

## Machine Learning Execution Model

Machine learning in this platform follows a **batch-oriented execution model**, which is standard for infrastructure analytics.

Key characteristics:

- models are trained offline using historical data
- feature tables are read from the database
- predictions are generated on a schedule or on demand
- results are written back to the database
- Power BI consumes predictions directly from stored tables

Real-time inference services are intentionally avoided, as infrastructure risk analysis prioritizes **explainability, auditability, and trend analysis** over low-latency prediction.

---

## Design Principles

The architecture follows several guiding principles:

### 1. Separation of Concerns

Each layer of the system has a clearly defined role:

- **ETL pipelines** handle ingestion and transformation  
- **Database storage** persists analytical and modeling data  
- **ML workflows** generate features and predictions  
- **BI models** deliver insights to end users  

This separation allows individual components to evolve independently without cascading changes.

---

### 2. Contract-Driven Data Flow

Schemas act as **explicit contracts** between layers of the system.  
They ensure that:

- upstream changes do not silently break downstream analytics
- Power BI models receive consistent, predictable datasets
- feature definitions remain stable as modeling evolves

Schemas are treated as first-class artifacts alongside code and dashboards.

---

### 3. BI-First Architecture

Power BI is treated as a **primary delivery surface**, not an afterthought.  
The data model is shaped to support:

- star-schema-friendly tables
- clear relationships and measures
- performant filtering and slicing

This ensures the platform aligns with how stakeholders actually consume insights.

---

### 4. Incremental Complexity

The system is designed to support **progressive enhancement**:

- initial focus on descriptive and diagnostic analytics
- structured pathways toward predictive risk scoring
- optional integration of more advanced ML techniques without architectural rework

This avoids premature complexity while preserving extensibility.

---

## How to Read the Architecture Documentation

The remaining architecture documents build on this foundation:

- **Structure** — repository layout and responsibility boundaries  
- **Data Flow** — how data moves from ingestion to BI consumption  
- **Component Descriptions** — detailed responsibilities of each module  

Together, these documents provide a complete view of how the platform is organized and why it is designed this way.

---

## Summary

This architecture is designed to be **practical, production-aligned, and transparent**.  
It reflects how utilities and engineering consultants typically deploy analytics and risk modeling systems — emphasizing **data quality, persistence, and decision support** rather than real-time inference.

The result is an architecture that is **deployable, auditable, and extensible**, without unnecessary operational complexity.
