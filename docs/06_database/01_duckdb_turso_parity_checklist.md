# DuckDB ↔ Turso Parity Checklist

This document defines a **parity checklist** to ensure that local development (DuckDB) and deployed storage (Turso / libSQL) remain **schema-compatible, behaviorally consistent, and analytics-safe** throughout the lifecycle of the project.

The goal is to prevent silent drift between environments that can break ML pipelines, Power BI models, or deployment workflows.

---

## 🎯 Parity Goals

DuckDB and Turso must remain aligned across:

- table structure and column definitions
- data types and nullability
- primary keys and uniqueness assumptions
- feature and prediction semantics
- query behavior used by ETL, ML, and BI

DuckDB is treated as the **local analytical engine**.  
Turso is treated as the **deployed system of record**.

---

## 1️⃣ Schema Parity (Must Match Exactly)

### ✅ Table Names

- [ ] All table names are identical in DuckDB and Turso
- [ ] No environment-specific table aliases exist
- [ ] Views use the same names (or are explicitly documented)

---

### ✅ Column Names & Order

- [ ] Column names match exactly (case-insensitive, snake_case)
- [ ] Column order is consistent for analytics tables
- [ ] No “local-only” debug columns exist

---

### ✅ Data Types

- [ ] DuckDB types map cleanly to Turso (SQLite) types  
- [ ] Numeric precision is preserved (REAL vs INTEGER vs TEXT)
- [ ] Dates and timestamps use compatible formats
- [ ] JSON fields (if any) are stored as TEXT consistently

> ⚠️ Avoid relying on DuckDB-only types or functions that do not exist in SQLite.

---

### ✅ Nullability & Defaults

- [ ] NULL / NOT NULL constraints are consistent
- [ ] Default values are explicitly defined where required
- [ ] No implicit defaults exist in only one environment

---

## 2️⃣ Primary Keys & Uniqueness

- [ ] Primary keys are defined consistently
- [ ] Composite keys (if used) are identical
- [ ] Auto-increment behavior is not relied on for analytics logic
- [ ] ML and BI do not depend on surrogate keys where natural keys exist

---

## 3️⃣ Feature Table Parity (Critical for ML)

### `pipe_features_monthly`

- [ ] Feature column names are identical
- [ ] Feature definitions are environment-independent
- [ ] Rolling/window calculations are computed in Python, not SQL
- [ ] Feature versioning is stored explicitly (`feature_version`)
- [ ] Feature generation timestamps are included and consistent

> ⚠️ Feature logic must live in Python, not database-specific SQL.

---

## 4️⃣ Prediction Table Parity

### `pipe_break_risk_scores`

- [ ] Prediction schema is identical
- [ ] Risk score scale is consistent (e.g., 0–1)
- [ ] Risk class thresholds are documented and fixed
- [ ] Model version is always recorded
- [ ] Prediction timestamps use UTC consistently

---

## 5️⃣ SQL Query Parity

### Stored SQL Files

- [ ] All SQL used by the application lives in `/src/db/queries/`
- [ ] No inline SQL differs by environment
- [ ] Queries avoid DuckDB-only functions
- [ ] Queries avoid SQLite-only quirks where possible

---

### Views

- [ ] Views created in DuckDB are recreated in Turso
- [ ] Views are treated as **read-only**
- [ ] Power BI only consumes documented tables or views

---

## 6️⃣ Power BI Compatibility Checks

- [ ] Power BI connects successfully to both environments
- [ ] Column data types are interpreted identically
- [ ] Relationships do not rely on implicit casting
- [ ] Measures do not break when switching DB backends

> ⚠️ Power BI should never require environment-specific logic.

---

## 7️⃣ Data Volume & Performance Expectations

- [ ] DuckDB used for fast local iteration
- [ ] Turso used for deployed persistence
- [ ] Table sizes remain within Turso performance expectations
- [ ] Heavy aggregations are precomputed in ETL or ML steps

---

## 8️⃣ Environment Configuration

- [ ] Connection strings differ by environment only
- [ ] No hardcoded DB paths exist
- [ ] `.env` controls all DB configuration
- [ ] Switching environments requires no code changes

---

## 9️⃣ Validation Checklist (Run Before Deployment)

Before promoting data or models from DuckDB → Turso:

- [ ] Row counts match for all core tables
- [ ] Aggregates (sum, mean, min, max) match
- [ ] Sample joins produce identical results
- [ ] ML predictions are numerically equivalent (within tolerance)
- [ ] Power BI dashboards refresh successfully

---

## 10️⃣ What This Checklist Prevents

This checklist explicitly prevents:

- silent schema drift
- broken Power BI dashboards
- invalid ML retraining runs
- environment-specific bugs
- unreproducible analytics results

---

## 🏁 Summary

DuckDB and Turso serve different roles, but **must behave as one system**.

DuckDB enables rapid local development.  
Turso enables deployable, persistent analytics.

This checklist ensures that both environments remain **functionally interchangeable**, preserving trust in analytics, ML outputs, and downstream dashboards.
