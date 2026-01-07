# DuckDB ↔ Turso Database Switch Procedure

This document defines the **standard procedure for switching database backends** between **DuckDB (local development)** and **Turso (deployed environment)** without code changes or analytical drift.

The procedure ensures that ETL pipelines, ML workflows, and Power BI dashboards remain **functionally identical** across environments.

---

## 🎯 Purpose

This procedure exists to:

- prevent schema or data drift between environments  
- ensure ML pipelines remain reproducible  
- guarantee Power BI dashboards continue to refresh correctly  
- allow seamless promotion from local development to deployment  

The database backend is treated as a **replaceable dependency**, not a structural component of the system.

---

## 🧠 Core Principle

> **The only difference between DuckDB and Turso is the connection string.**

All schemas, queries, and application logic must remain unchanged.

---

## 1️⃣ Pre-Switch Requirements

Before switching environments, confirm the following:

- [ ] DuckDB schema matches Turso schema exactly  
- [ ] All SQL queries live in `/src/db/queries/`  
- [ ] Feature generation logic runs in Python (not DB-specific SQL)  
- [ ] Parity checklist has been reviewed  
- [ ] `.env.example` contains all required DB variables  

---

## 2️⃣ Environment Configuration

### Local Development (DuckDB)

```env
DB_BACKEND=duckdb
DUCKDB_PATH=./data/local/analytics.duckdb
```

Characteristics:

- embedded file-based DB
- fast iteration
- used for EDA, feature development, and testing

---

### Deployed / Shared Environment (Turso)

```env
DB_BACKEND=turso
TURSO_DATABASE_URL=libsql://<db-name>.turso.io
TURSO_AUTH_TOKEN=<secure-token>
```

Characteristics:

- network-accessible
- persistent
- Power BI–connected
- system of record

---

## 3️⃣ Switching Procedure

### Step 1 — Update Environment Variables

Modify **only** the environment configuration:

- set `DB_BACKEND`
- update connection credentials
- do **not** change code

---

### Step 2 — Initialize Database Connection

Ensure `connection.py` selects the backend based on configuration:

```python
if DB_BACKEND == "duckdb":
    connect_duckdb()
elif DB_BACKEND == "turso":
    connect_turso()
```

No other logic should branch on environment.

---

### Step 3 — Apply Schema (If Needed)

If switching to a fresh database:

- apply `CREATE TABLE` scripts  
- verify schema against `schemas/*.yaml`  
- confirm table existence  

---

### Step 4 — Load or Sync Data

Run ETL scripts to populate or sync data:
Depending on context:

- initial deployment → load curated datasets  
- redeploy → validate existing tables  
- re-scoring → only update prediction tables  

---

### Step 5 — Validation Checks

Run the following validations:

- row counts match expected values  
- aggregate metrics (sum, mean) align with DuckDB results  
- sample joins return identical outputs  
- ML predictions fall within expected tolerance  

---

### Step 6 — Power BI Refresh Test

In Power BI Desktop, switch the data source to the new database backend.
Confirm:

- dataset refresh succeeds  
- relationships remain intact  
- measures do not error  
- visuals render correctly  

---

## 4️⃣ Rollback Strategy

If issues are detected:

1. revert environment variables  
2. switch back to DuckDB  
3. diagnose schema or data mismatch  
4. correct issues before redeploying  

No data should be modified until validation passes.

---

## 5️⃣ Common Failure Modes (Avoid These)

- ❌ DB-specific SQL logic  
- ❌ feature computation inside SQL  
- ❌ environment-specific table names  
- ❌ Power BI logic tied to backend quirks  
- ❌ silent schema changes  

If any of these appear, **stop the switch** and correct them.

---

## 🏁 Summary

This procedure ensures that DuckDB and Turso remain **interchangeable execution environments**.

DuckDB supports rapid local development.  
Turso supports deployed, persistent analytics.

Following this procedure guarantees that **ETL, ML, and BI behave identically**, preserving trust in analytical outputs and preventing deployment regressions.
