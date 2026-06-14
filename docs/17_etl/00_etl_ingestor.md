# ETL Ingestor Layer: Toronto Open Data

## Purpose

This document describes the **ETL Ingestor Layer** responsible for acquiring, validating, transforming, and loading datasets used throughout the Toronto Pipeline Failure Prediction project.

The ETL layer serves as the bridge between raw external data sources and downstream analytics, feature engineering, machine learning, and reporting workflows.

Unlike the API layer, which is responsible only for dataset discovery and metadata retrieval, the ETL layer manages the complete lifecycle of each dataset after discovery.

---

## Role in the Pipeline

```text
Toronto Open Data Portal
        ↓
TorontoOpenDataClient (api/)
        ↓
ETL Ingestor Layer (etl/)
        ↓
data/raw/
        ↓
data/interim/
        ↓
data/processed/
        ↓
Database / Feature Engineering
        ↓
Machine Learning
        ↓
Monte Carlo Simulation
        ↓
Power BI
```

The ETL layer is responsible for ensuring that datasets are reproducible, validated, traceable, and ready for analytical use.

---

# Design Philosophy

The ingestion framework is designed around the following principles:

### Dataset Ownership

Each dataset should have its own dedicated ingestor class.

This keeps dataset-specific logic isolated and maintainable.

### Validation First

Data quality is treated as a first-class concern.

Validation occurs throughout the pipeline rather than after loading.

### Reproducibility

All intermediate outputs should be reproducible and persisted to disk.

### Explicit Data Lineage

The progression from raw data to analytical datasets should be transparent and auditable.

### Separation of Concerns

The API layer discovers data.

The ETL layer manages data.

The analytics layer consumes data.

---

# ETL Package Structure

```plaintext
etl/
├── __init__.py
│
├── base_ingestor.py
│
├── watermain_breaks_ingestor.py
├── distribution_mains_ingestor.py
├── transmission_mains_ingestor.py
├── neighborhoods_ingestor.py
├── climate_ingestor.py
└── soils_ingestor.py
```

Each ingestor is responsible for a single dataset family.

---

# Dataset Ingestors

## WatermainBreaksIngestor

Responsible for:

* downloading watermain break records
* validating source schema
* standardizing date fields
* removing duplicates
* persisting curated break records

---

## DistributionMainsIngestor

Responsible for:

* downloading distribution main GIS data
* validating geometries
* standardizing attributes
* calculating derived spatial properties

---

## TransmissionMainsIngestor

Responsible for:

* downloading transmission main GIS data
* validating network features
* preparing transmission assets for spatial analysis

---

## NeighborhoodsIngestor

Responsible for:

* downloading neighborhood boundaries
* validating polygon geometries
* preparing administrative boundaries for spatial joins

---

## ClimateIngestor

Responsible for:

* downloading climate datasets
* aggregating temporal measurements
* preparing monthly climate indicators

---

## SoilsIngestor

Responsible for:

* downloading soil datasets
* validating geospatial layers
* preparing soil characteristics for feature engineering

---

# Base Ingestor Contract

All dataset ingestors should inherit from a common base class.

```python
class BaseIngestor:

    def extract(self):
        ...

    def validate_raw(self):
        ...

    def persist_raw(self):
        ...

    def transform(self):
        ...

    def validate_processed(self):
        ...

    def persist_processed(self):
        ...

    def load_to_database(self):
        ...

    def validate_loaded(self):
        ...
```

This establishes a consistent ingestion workflow across all datasets.

---

# Standard Ingestion Workflow

Each dataset should follow the same lifecycle:

```text
Extract
    ↓
Validate Raw
    ↓
Persist Raw
    ↓
Transform
    ↓
Validate Processed
    ↓
Persist Processed
    ↓
Load to Database
    ↓
Validate Loaded
```

Validation is intentionally performed multiple times throughout the pipeline.

---

# Stage Responsibilities

## 1. Extract

Responsibilities:

* discover resource URLs
* download source files
* retrieve raw datasets
* capture metadata

Output:

```plaintext
data/raw/
```

---

## 2. Validate Raw

Responsibilities:

* verify required columns exist
* validate source schema
* verify data types
* detect corrupt records
* verify geometry columns

Failures should stop processing immediately.

---

## 3. Persist Raw

Responsibilities:

* store downloaded source files
* preserve original datasets
* maintain audit trail

Output:

```plaintext
data/raw/
```

---

## 4. Transform

Responsibilities:

* clean records
* standardize field names
* convert data types
* calculate derived attributes
* perform spatial joins
* aggregate temporal data

Output:

```plaintext
data/interim/
```

or

```plaintext
data/processed/
```

depending on the stage.

---

## 5. Validate Processed

Responsibilities:

* verify transformed schema
* validate business rules
* verify coordinate systems
* verify spatial joins
* detect duplicate records

Examples:

* no duplicate asset IDs
* valid Toronto coordinates
* valid date ranges
* non-null required fields

---

## 6. Persist Processed

Responsibilities:

* save curated analytical datasets
* create reproducible intermediate outputs

Output:

```plaintext
data/processed/
```

Preferred format:

```plaintext
Parquet
```

unless another format is justified.

---

## 7. Load to Database

Responsibilities:

* load processed datasets into downstream storage
* prepare data for analytics consumption

Examples:

* Turso
* PostgreSQL
* analytical feature stores

---

## 8. Validate Loaded

Responsibilities:

* verify row counts
* verify key uniqueness
* verify load success
* verify referential integrity

Examples:

* source rows = destination rows
* no missing primary keys
* no unexpected null values

---

# Validation Framework

This project should use standardized schema validation.

Recommended libraries:

* Pandera
* Pydantic

---

## Schema Location

```plaintext
schemas/
├── watermain_breaks_schema.yaml
├── distribution_mains_schema.yaml
├── transmission_mains_schema.yaml
├── climate_schema.yaml
├── soils_schema.yaml
└── neighborhoods_schema.yaml
```

---

## Example Schema

```python
class WatermainBreakSchema(pa.SchemaModel):
    break_id: Series[int]
    break_date: Series[pd.Timestamp]
    latitude: Series[float]
    longitude: Series[float]
```

---

## Validation Requirements

Raw data should be validated before transformation.

Processed data should be validated before loading.

Loaded data should be validated after ingestion.

Validation failures should stop pipeline execution.

---

# Data Storage Structure

```plaintext
data/
├── raw/
│
├── interim/
│
└── processed/
```

---

## Raw

Contains source files exactly as received.

```plaintext
data/raw/
```

Examples:

```plaintext
watermain_breaks.csv
distribution_mains.geojson
```

---

## Interim

Contains partially transformed datasets.

```plaintext
data/interim/
```

Used for debugging and pipeline development.

---

## Processed

Contains analytics-ready datasets.

```plaintext
data/processed/
```

These datasets should be suitable for:

* feature engineering
* machine learning
* Monte Carlo simulation
* Power BI reporting

---

# Error Handling

Pipeline failures should:

* fail fast
* log detailed errors
* preserve prior successful outputs
* avoid partial writes
* surface actionable diagnostics

Silent failures are prohibited.

---

# Why This Layer Exists

The ETL layer provides:

* reproducible ingestion workflows
* data quality enforcement
* clear dataset ownership
* auditability
* maintainable architecture

It prevents business logic, analytics logic, and API discovery logic from becoming tightly coupled.

---

# Summary

The ETL Ingestor Layer is responsible for:

* extracting datasets
* validating raw inputs
* persisting source data
* transforming records
* validating processed outputs
* loading analytical datasets
* validating downstream storage

Each dataset receives its own dedicated ingestor implementation.

The result is a scalable, testable, and production-oriented ingestion framework suitable for infrastructure analytics, machine learning, and decision-support applications.
