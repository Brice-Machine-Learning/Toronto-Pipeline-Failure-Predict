# 🚰 Municipal Pipeline Break Analytics & Risk Platform  

## High-Level Project Checklist (Phased)

This checklist defines a **production-style delivery plan** for building an
end-to-end analytics and risk modeling platform for Toronto water pipeline
breaks. The phases are intentionally ordered to reflect **real-world data
engineering and analytics workflows**, not notebook-driven experimentation.

---

## Phase 0 — Project Framing & Governance

**Objective:**  
Establish scope, guardrails, and delivery expectations before writing code.

### Documentation & Governance

- [x] Define project purpose and success criteria (`03_project_framing_governance.md`)
- [x] Explicitly document non-goals (e.g., real-time inference) (`04_non_goals.md`)
- [x] Identify primary stakeholders and analytical use cases (`05_stakeholders_and_use_cases.md`)
- [x] Document target users: utility analysts, infrastructure planners, engineering managers
- [x] Define core analytical questions the platform must answer
- [x] Define success criteria for data, architecture, analytics, and extensibility

### Architecture & System Design

- [x] Document architecture introduction and objectives (`01_architecture/00_introduction.md`)
- [x] Define high-level architecture layers (ETL, database, ML, BI)
- [x] Document database strategy (DuckDB for local, Turso for deployment)
- [x] Establish batch-oriented ML execution model (no real-time inference)
- [x] Document separation of concerns across components (`03_component_descriptions.md`)
- [x] Define component responsibility boundaries and ownership model
- [x] Document data flow architecture end-to-end (`02_data_flow.md`)

### Repository & Code Structure

- [x] Define versioning strategy (v0.x analytics → v1.x risk modeling) (`06_versioning_strategy.md`)
- [x] Finalize repository structure (code, data, docs separation) (`01_structure.md`)
- [x] Create project directory structure with placeholders
- [x] Set up Python package structure (`src/municipal_pipeline_failure_predict/`)
- [x] Configure project dependencies (`pyproject.toml`)
- [x] Draft initial README (problem, architecture, roadmap)

### Configuration & Development Setup

- [x] Create configuration management system (`config/settings.py`)
- [x] Set up logging infrastructure (`log/logger.py`)
- [x] Create `.env.example` template for environment variables
- [x] Document configuration approach

### API Client Foundation

- [x] Build Toronto Open Data CKAN API client (`api/municipal_client.py`)
- [x] Document API client design and usage (`16_api/00_toronto_open_data_client.md`)
- [x] Implement dataset search and metadata retrieval
- [x] Implement resource discovery by format
- [x] Add domain-specific helper: `get_water_main_breaks_metadata()`
- [x] Write smoke tests for API client (`tests/test_smoke.py`)

_**Deliverables**_

- ✅ README (v0.1)
- ✅ `/docs/00_overview/` (6 documents)
- ✅ `/docs/01_architecture/` (4 documents)
- ✅ `/docs/16_api/` (API client documentation)
- ✅ Clear scope and assumptions
- ✅ Working API client with documentation
- ✅ Configuration and logging infrastructure
- ✅ Project structure and development environment

---

## Phase 1 — Data Acquisition & Inventory

**Objective:**  
Identify authoritative datasets, validate coverage, download data, and document limitations early.

### 1.1 Data Source Research & Documentation

- [ ] Research and document water main break datasets (`02_data_sources/01_pipe_break_data_sources.md`)
- [ ] Identify Toronto Open Data portal endpoints for breaks dataset
- [ ] Document expected schema, fields, and data types
- [ ] Research climate data sources (NOAA/PRISM or Canadian equivalents)
- [ ] Document climate data temporal coverage and spatial resolution
- [ ] Research soil and geotechnical data (Ontario Geological Survey, NRCan)
- [ ] Document soil data spatial resolution and classification system
- [ ] Research GIS layers (neighborhoods, water zones, watersheds)
- [ ] Document coordinate systems and spatial reference systems
- [ ] Research water infrastructure asset metadata (age, material, diameter)

### 1.2 Data Source Validation

- [ ] Verify water main break data temporal coverage (start year → present)
- [ ] Validate break data spatial precision (lat/lon or address quality)
- [ ] Assess climate data temporal alignment with break records
- [ ] Validate climate data spatial coverage for Toronto region
- [ ] Verify soil data spatial alignment with Toronto neighborhoods
- [ ] Assess GIS boundary data currency and accuracy
- [ ] Document update cadence for each data source
- [ ] Identify data quality issues, gaps, and missing fields
- [ ] Document known limitations and assumptions for each dataset
- [ ] Create data source inventory table (source, format, coverage, update cadence)

### 1.3 Data Download & Storage

- [ ] Create raw data directory structure:
  - `/data/raw/municipal/` (water main breaks)
  - `/data/raw/climate/`
  - `/data/raw/soils/`
  - `/data/raw/gis/`
- [ ] Test API client with water main breaks dataset
- [ ] Download and snapshot water main break records (full historical)
- [ ] Download climate data (monthly aggregations for Toronto region)
- [ ] Download soil/geotechnical reference layers
- [ ] Download neighborhood boundary GIS files
- [ ] Download water system zone boundaries (if available)
- [ ] Verify file integrity (checksums or manual inspection)
- [ ] Document download date and data version for each file
- [ ] Create `data/raw/README.md` documenting all raw data sources

### 1.4 Initial Data Exploration (Read-Only)

- [ ] Load water main breaks data and inspect schema
- [ ] Count total break records and temporal range
- [ ] Identify spatial coverage (neighborhoods represented)
- [ ] Load climate data and verify temporal alignment
- [ ] Load soil data and verify spatial coverage
- [ ] Load GIS boundaries and verify coordinate systems match
- [ ] Document initial observations about data quality
- [ ] Identify fields requiring cleaning or normalization
- [ ] Document inferred fields (fields not explicitly present)
- [ ] Create initial data quality assessment summary

### 1.5 Data Dictionary & Schema Planning

- [ ] Create data dictionary for water main breaks (field definitions)
- [ ] Create data dictionary for climate indicators
- [ ] Create data dictionary for soil zones
- [ ] Create data dictionary for GIS boundaries
- [ ] Document expected join keys across datasets
- [ ] Identify geographic standardization strategy (neighborhood names/IDs)
- [ ] Document temporal standardization strategy (YYYY-MM format)
- [ ] Plan spatial join approach (point-in-polygon for breaks → neighborhoods)

_**Deliverables**_

- `/data/raw/` — all source datasets downloaded and versioned
- `/data/raw/README.md` — data source inventory
- `/docs/02_data_sources/` — comprehensive data source documentation
- Data dictionaries for all major datasets
- Data quality assessment report
- Documented data assumptions and known limitations

---

## Phase 2 — Database Design & Platform Setup

**Objective:**  
Define the **data contracts** before cleaning or transforming data. Establish both local (DuckDB) and deployment (Turso) database environments.

### 2.1 Schema Design — Core Analytics Tables

- [ ] Design `pipe_breaks_clean` table schema:
  - Primary key strategy
  - Date fields (break_date, year, month)
  - Geographic fields (neighborhood, lat, lon)
  - Metadata fields (source, ingestion_timestamp)
- [ ] Design `climate_monthly` table schema:
  - Composite key (year, month)
  - Climate indicators (rainfall_mm, mean_temp_c, drought_index)
  - Source tracking
- [ ] Design `soil_zones` table schema:
  - Zone identification
  - Neighborhood mapping
  - Corrosivity indicators
- [ ] Design `neighborhoods` lookup table (optional):
  - Neighborhood ID and name
  - Region groupings
  - Geometry (WKT format)
- [ ] Document design rationale for each table
- [ ] Create `/schemas/data_schema.yaml` with table definitions

### 2.2 Schema Design — ML Feature & Prediction Tables

- [ ] Design `pipe_features_monthly` table schema:
  - Temporal-spatial composite key (year, month, neighborhood)
  - Rolling break rate features
  - Lagged climate features (6-month averages)
  - Soil and geotechnical joins
  - Feature version tracking
  - Generation timestamp
- [ ] Design `pipe_break_risk_scores` table schema:
  - Temporal-spatial composite key
  - Risk score (continuous)
  - Risk class (categorical)
  - Model version tracking
  - Prediction timestamp
- [ ] Create `/schemas/features_schema.yaml`
- [ ] Create `/schemas/model_schema.yaml`

### 2.3 Schema Design — Metadata & Governance Tables

- [ ] Design `model_metadata` table schema:
  - Model version (primary key)
  - Model type
  - Training date range
  - Features version
  - Metrics (stored as JSON)
- [ ] Design `etl_runs` table schema:
  - Run ID, pipeline name
  - Timestamp, status
  - Row counts
  - Notes/logs
- [ ] Document metadata schema purpose and usage

### 2.4 Database Migrations — Local (DuckDB)

- [ ] Create `src/.../db/migrations/` directory
- [ ] Write `01_create_core_tables.sql` (breaks, climate, soil, neighborhoods)
- [ ] Write `02_create_feature_tables.sql` (features_monthly)
- [ ] Write `03_create_prediction_tables.sql` (risk_scores)
- [ ] Write `04_create_metadata_tables.sql` (model_metadata, etl_runs)
- [ ] Write `05_add_indexes.sql`:
  - Time-based indexes (year, month)
  - Geographic indexes (neighborhood)
  - Composite indexes for join optimization
- [ ] Test migrations against local DuckDB instance
- [ ] Document migration execution order

### 2.5 Database Connection Layer

- [ ] Implement `src/.../db/connection.py`:
  - DuckDB connection factory
  - Turso connection factory
  - Environment-based connection selection
- [ ] Implement connection pooling (if needed)
- [ ] Add connection health checks
- [ ] Write unit tests for connection management
- [ ] Document connection configuration requirements

### 2.6 Turso Setup & Deployment

- [ ] Create Turso account and database instance
- [ ] Configure Turso connection credentials
- [ ] Store Turso credentials in `.env` (document in `.env.example`)
- [ ] Deploy schema to Turso using migration scripts
- [ ] Verify empty schema created successfully
- [ ] Test connection from local environment to Turso
- [ ] Document Turso setup procedure

### 2.7 Database Utility Queries

- [ ] Create `/src/.../db/queries/` directory
- [ ] Write `validate_schema.sql` — schema inspection queries
- [ ] Write `row_counts.sql` — table population checks
- [ ] Write `data_quality_checks.sql` — null checks, duplicate detection
- [ ] Document query usage and purpose

### 2.8 Schema Documentation

- [ ] Document complete v1 schema in `/docs/06_database/00_turso_database_tables.md`
- [ ] Document table purposes and relationships
- [ ] Create entity-relationship diagram (ERD) or Mermaid diagram
- [ ] Document naming conventions and constraints
- [ ] Document DuckDB ↔ Turso parity checklist (`01_duckdb_turso_parity_checklist.md`)
- [ ] Document database switching procedure (`02_db_switch_procedure.md`)
- [ ] Document Power BI consumption patterns

### 2.9 Database Testing & Validation

- [ ] Write integration tests for database migrations
- [ ] Test schema creation in DuckDB
- [ ] Test schema creation in Turso
- [ ] Verify schema parity between DuckDB and Turso
- [ ] Test connection switching logic
- [ ] Document test results

_**Deliverables**_

- Database schema v1 (documented and deployed)
- SQL migration files (5+ migration scripts)
- Schema definition files (YAML): `data_schema.yaml`, `features_schema.yaml`, `model_schema.yaml`
- Database connection layer (`db/connection.py`)
- Empty schemas deployed to both DuckDB (local) and Turso (deployment)
- Database documentation in `/docs/06_database/` (3+ documents)
- Database parity checklist and switching procedure
- Integration tests for database setup

---

## Phase 3 — ETL & Data Cleaning (Schema-Driven)

**Objective:**  
Clean and transform data **to satisfy database contracts**, not ad-hoc analysis. Build production-ready ETL pipelines for all data sources.

### 3.1 ETL Architecture & Utilities

- [ ] Create `/src/.../etl/` directory structure:
  - `download_raw.py` — file download utilities
  - `validate_raw.py` — data quality checks
  - `transform/` — transformation modules per data source
  - `load.py` — database loading utilities
- [ ] Document ETL design principles (`17_etl/00_etl_downloader.md`)
- [ ] Implement `download_file()` utility in `utils/`:
  - Streaming download support
  - Progress tracking
  - Retry logic
  - Checksum verification
- [ ] Implement schema validation utilities:
  - Compare DataFrame to expected schema
  - Type checking
  - Required field validation
  - Value range validation

### 3.2 Water Main Breaks — ETL Pipeline

- [ ] Implement `etl/transform/breaks_pipeline.py`:
  - Load raw water main breaks CSV/GeoJSON
  - Parse and validate date fields
  - Extract year and month
  - Validate/clean geographic coordinates
  - Perform spatial join to neighborhoods (point-in-polygon)
  - Standardize neighborhood names
  - Add source and ingestion timestamp
  - Validate against `pipe_breaks_clean` schema
- [ ] Implement aggregation to monthly × neighborhood:
  - Group by (year, month, neighborhood)
  - Calculate break_count
  - Preserve spatial representativeness
- [ ] Write unit tests for breaks transformation logic
- [ ] Write integration test: raw CSV → database
- [ ] Document breaks ETL assumptions and limitations

### 3.3 Climate Data — ETL Pipeline

- [ ] Implement `etl/transform/climate_pipeline.py`:
  - Load raw climate data (NOAA/PRISM or EC equivalent)
  - Aggregate to monthly resolution
  - Calculate rainfall_mm (monthly total)
  - Calculate mean_temp_c (monthly average)
  - Calculate drought index (if data available)
  - Normalize to Toronto region (spatial aggregation if needed)
  - Add source tracking
  - Validate against `climate_monthly` schema
- [ ] Handle missing climate data (interpolation strategy)
- [ ] Write unit tests for climate transformation logic
- [ ] Write integration test: raw climate data → database
- [ ] Document climate data processing methodology

### 3.4 Soil/Geotechnical Data — ETL Pipeline

- [ ] Implement `etl/transform/soil_pipeline.py`:
  - Load raw soil/geotechnical shapefiles or CSV
  - Parse soil classification and properties
  - Map soil zones to neighborhoods (spatial join)
  - Calculate or assign corrosivity_index
  - Standardize zone codes and descriptions
  - Validate against `soil_zones` schema
- [ ] Document soil corrosivity calculation methodology
- [ ] Write unit tests for soil transformation logic
- [ ] Write integration test: raw GIS → database
- [ ] Document soil data assumptions

### 3.5 GIS Neighborhood Boundaries — ETL Pipeline

- [ ] Implement `etl/transform/gis_pipeline.py`:
  - Load neighborhood boundary shapefiles/GeoJSON
  - Validate geometry (topology checks)
  - Extract neighborhood names and IDs
  - Simplify geometry if needed (preserve accuracy)
  - Convert geometry to WKT format
  - Validate against `neighborhoods` schema (if using)
- [ ] Create neighborhood lookup reference
- [ ] Write tests for GIS processing
- [ ] Document coordinate system and projection handling

### 3.6 Data Validation Framework

- [ ] Implement `etl/validate_raw.py`:
  - Schema conformance checks
  - Null value detection
  - Duplicate record detection
  - Value range validation
  - Referential integrity checks (foreign keys)
  - Temporal consistency checks (year/month valid)
- [ ] Implement validation reporting:
  - Generate validation summary
  - Flag critical vs. warning issues
  - Write validation results to logs
- [ ] Integrate validation into each ETL pipeline
- [ ] Document validation rules and thresholds

### 3.7 Database Loading Module

- [ ] Implement `etl/load.py`:
  - Batch insert functionality
  - Upsert logic (update if exists, insert if new)
  - Transaction management
  - Error handling and rollback
  - Row count verification
  - Performance optimization (bulk inserts)
- [ ] Test loading to DuckDB
- [ ] Test loading to Turso
- [ ] Document loading patterns and best practices

### 3.8 ETL Orchestration & Execution

- [ ] Create `etl/run_full_pipeline.py`:
  - Orchestrate execution order
  - Execute breaks pipeline → load
  - Execute climate pipeline → load
  - Execute soil pipeline → load
  - Execute GIS pipeline → load
  - Log ETL run details to `etl_runs` table
- [ ] Implement idempotency (safe to re-run)
- [ ] Implement incremental refresh strategy (future):
  - Detect new records
  - Append vs. full reload
- [ ] Add command-line interface for pipeline execution
- [ ] Document pipeline execution procedure

### 3.9 ETL Testing & Quality Assurance

- [ ] Write unit tests for each transformation function
- [ ] Write integration tests for full pipelines
- [ ] Test with sample data subsets
- [ ] Test with full data
- [ ] Verify row counts match expectations
- [ ] Verify data types in database match schema
- [ ] Check for data loss during transformations
- [ ] Validate geographic joins (neighborhood assignments)
- [ ] Validate temporal joins (climate data alignment)
- [ ] Document test coverage and results

### 3.10 ETL Logging, Monitoring & Documentation

- [ ] Integrate logging into all ETL modules
- [ ] Log pipeline start and completion times
- [ ] Log row counts at each stage (extracted, transformed, loaded)
- [ ] Log validation failures and data quality issues
- [ ] Create ETL execution dashboard (simple text report/CSV)
- [ ] Document ETL run logs location and format
- [ ] Create `/docs/17_etl/01_pipeline_execution_guide.md`
- [ ] Document troubleshooting common ETL issues
- [ ] Document data refresh procedures

### 3.11 Data Quality Verification (Post-ETL)

- [ ] Query loaded data and verify completeness:
  - Check expected row counts
  - Verify temporal coverage (all expected months present)
  - Verify spatial coverage (all neighborhoods represented)
- [ ] Run data quality SQL checks:
  - Null percentage in key fields
  - Duplicate detection
  - Referential integrity (joins work)
- [ ] Generate post-ETL data quality report
- [ ] Compare loaded data against raw data (spot checks)
- [ ] Document known data quality issues

_**Deliverables**_

- Complete ETL pipelines for all data sources:
  - `pipe_breaks_clean` (loaded)
  - `climate_monthly` (loaded)
  - `soil_zones` (loaded)
  - `neighborhoods` (loaded, optional)
- Reproducible ETL scripts in `/src/.../etl/`
- Data validation framework and utilities
- Database loading module with transaction support
- ETL orchestration script (`run_full_pipeline.py`)
- Comprehensive ETL tests (unit + integration)
- ETL run logs persisted to `etl_runs` table
- ETL documentation in `/docs/17_etl/` (2+ documents)
- Post-ETL data quality report
- Populated database (DuckDB and/or Turso) ready for analytics

---

## Phase 4 — Analytics Modeling & Database Views

**Objective:**  
Make the database analytics- and BI-ready.

_**Checklist**

- [ ] Create analytics views for common joins
- [ ] Build descriptive `joined_risk_view` (non-ML)
- [ ] Optimize queries for BI performance
- [ ] Validate joins, row counts, and data integrity

_**Deliverables**

- Analytics views
- BI-ready query layer
- Validated database relationships

---

## Phase 5 — Power BI Semantic Model

**Objective:**  
Create a stable semantic layer for dashboards and analysis.

_**Checklist**

- [ ] Build Power BI dataset model
- [ ] Add proper Date table
- [ ] Define star schema relationships
- [ ] Create core DAX measures:
  - total breaks
  - rolling 12-month trends
  - neighborhood comparisons
- [ ] Validate filters, slicers, and performance

_**Deliverables**

- Power BI `.pbit` template
- Documented DAX measures
- Dataset requirements locked

---

## Phase 6 — Descriptive & Diagnostic Dashboards

**Objective:**  
Answer **what happened, where, and what correlates with it**.

_**Checklist**

- [ ] Time-series trend dashboards
- [ ] Seasonality analysis
- [ ] Environmental correlation views
- [ ] Geographic hotspot maps
- [ ] Drill-downs by neighborhood
- [ ] Clear annotations and executive-safe labeling

_**Deliverables**

- Power BI dashboards (v0.1)
- Screenshot assets for README
- Stakeholder-style narrative

---

## Phase 7 — Feature Engineering for Risk Modeling

**Objective:**  
Prepare interpretable, defensible features for ML.

_**Checklist**

- [ ] Rolling break-rate features
- [ ] Lagged climate indicators
- [ ] Soil/geotechnical joins
- [ ] Prior failure indicators
- [ ] Feature versioning
- [ ] Feature schema validation

_**Deliverables**

- `pipe_features_monthly`
- Feature schema files
- Feature documentation

---

## Phase 8 — Machine Learning (Batch Risk Scoring)

**Objective:**  
Produce explainable, batch-based risk scores.

_**Checklist**

- [ ] Select baseline, interpretable models
- [ ] Train using time-aware splits
- [ ] Evaluate performance and stability
- [ ] Generate neighborhood-level risk scores
- [ ] Persist predictions to database
- [ ] Store model metadata and metrics

_**Deliverables**

- Trained models
- `pipe_break_risk_scores`
- Model evaluation report

---

## Phase 9 — Risk Visualization & Interpretation

**Objective:**  
Translate risk outputs into planning insights.

_**Checklist**

- [ ] Risk ranking dashboards
- [ ] High-risk neighborhood summaries
- [ ] Predicted vs historical comparisons
- [ ] Visual explanation of drivers
- [ ] Plain-language interpretation notes

_**Deliverables**

- Risk dashboards (v1.0)
- Executive-ready visuals
- Interpretation documentation

---

## Phase 10 — Polish, Versioning & Portfolio Prep

**Objective:**  
Finalize the project for presentation and review.

_**Checklist**

- [ ] Finalize versioned README
- [ ] Document limitations and future work
- [ ] Write Medium / whitepaper draft
- [ ] Clean commit history
- [ ] Tag v1.0 release

_**Deliverables**

- v1.0 release
- Portfolio-ready project
- Interview-ready talking points

---
