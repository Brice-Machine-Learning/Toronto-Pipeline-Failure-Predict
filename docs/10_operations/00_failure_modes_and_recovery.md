# Failure Modes and Recovery

This document describes the **expected failure modes** within the **LA Water Main Break Analytics & Risk Platform**, along with **detection signals, impact, and recovery procedures**.

The goal is not to eliminate all failures, but to ensure failures are:

- detectable  
- contained  
- recoverable  
- non-destructive  

The system is designed so that **no single failure corrupts analytics, ML outputs, or dashboards silently**.

---

## Guiding Principles

- Failures should be **visible**, not hidden  
- Partial failure should not cascade across layers  
- Data correctness is prioritized over freshness  
- Recovery should not require code changes  
- Dashboards should degrade gracefully  

---

## Failure Mode Summary Table

| Failure Type | Component | Detection | Impact | Recovery |
| ------------- | ---------- | ----------- | -------- | ---------- |
| Raw data unavailable | Data sources | ETL logs | ETL run skipped | Retry ingestion |
| ETL data validation failure | ETL | Validation checks | No DB writes | Fix data + rerun |
| Database unavailable | DuckDB / Turso | Connection error | ETL/ML paused | Restore DB / retry |
| Schema drift | DB / schemas | Parity checks | ML/BI blocked | Apply migrations |
| Feature generation failure | Features | Exception logs | ML skipped | Fix logic + rerun |
| ML training failure | Models | Training logs | Old model retained | Debug + retrain |
| Prediction job failure | Models | Missing predictions | BI shows prior data | Rerun scoring |
| Power BI refresh failure | Power BI | Refresh error | Stale dashboards | Fix query / retry |
| Partial data load | ETL | Row count mismatch | Analytics incomplete | Rollback load |
| Environment misconfig | Config | Startup failure | Pipeline aborts | Fix `.env` |

---

## Component-Level Failure Details

### 1️⃣ Raw Data Source Failures

_**Description**

- Public datasets unavailable
- Source schema changes
- Incomplete downloads

_**Detection**

- Missing files
- HTTP errors
- Row count anomalies

_**Impact**

- ETL does not proceed
- No downstream updates

_**Recovery**

- Log failure
- Skip ingestion
- Retry on next run
- Update ingestion logic if schema changed

---

### 2️⃣ ETL Failures

_**Description**

- Data validation errors
- Parsing issues
- Unexpected nulls

_**Detection**

- Validation assertions
- Schema mismatches
- Exception logs

_**Impact**

- Curated tables not updated
- ML and BI continue using last valid data

_**Recovery**

- Correct ETL logic or source assumptions
- Rerun ETL
- Validate row counts before promotion

---

### 3️⃣ Database Failures (DuckDB / Turso)

_**Description**

- Connection failures
- Permission issues
- Storage outages

_**Detection**

- Connection exceptions
- Timeout errors

_**Impact**

- ETL, ML, and BI paused
- No data corruption

_**Recovery**

- Restore connectivity
- Validate schema integrity
- Resume pipelines

---

### 4️⃣ Schema Drift

_**Description**

- Table structure differs between environments
- Columns added/removed without migration

_**Detection**

- Parity checklist
- Migration mismatch
- Power BI refresh errors

_**Impact**

- ML pipelines blocked
- BI datasets fail to refresh

_**Recovery**

- Apply missing migrations
- Re-run parity checks
- Validate schema against `schemas/*.yaml`

---

### 5️⃣ Feature Engineering Failures

_**Description**

- Logic errors
- Divide-by-zero
- Unexpected distributions

_**Detection**

- Python exceptions
- Feature sanity checks

_**Impact**

- ML training and scoring skipped
- Prior predictions remain active

_**Recovery**

- Fix feature logic
- Regenerate features
- Re-run ML pipeline

---

### 6️⃣ ML Training Failures

_**Description**

- Model convergence failures
- Convergence issues
- Insufficient data
- Library incompatibilities

_**Detection**

- Training logs
- Missing model artifacts

_**Impact**

- Existing model remains active
- No production impact

_**Recovery**

- Debug training
- Adjust parameters
- Retrain and register new model

---

### 7️⃣ ML Scoring Failures

_**Description**

- Prediction job fails
- Feature/model mismatch

_**Detection**

- Missing prediction rows
- Timestamp gaps

_**Impact**

- Dashboards show last valid scores

_**Recovery**

- Rerun scoring job
- Validate outputs
- Update prediction table

---

### 8️⃣ Power BI Failures

_**Description**

- Dataset refresh failures
- SQL query errors
- Relationship breaks

_**Detection**

- Power BI refresh logs
- Visual errors

_**Impact**

- Dashboards become stale
- No data corruption

_**Recovery**

- Fix query or schema
- Refresh dataset
- Validate visuals

---

## Failure Containment Strategy

The system enforces **containment boundaries**:

- ETL failure → does not corrupt DB  
- Feature failure → does not retrain ML  
- ML failure → does not affect BI stability  
- BI failure → does not affect data correctness  

Failures stop at the layer where they occur.

---

## Rollback and Safe State

- No destructive updates without validation
- Old data and predictions remain available
- Re-runs overwrite data only after checks pass
- No partial writes promoted to BI

---

## Summary

Failures are expected and planned for.

The platform is designed so that:

- analytics remain trustworthy
- ML does not destabilize BI
- recovery is procedural, not ad hoc
- no silent corruption occurs

This approach mirrors **real-world analytics and infrastructure risk systems**, where correctness and stability are prioritized over immediacy.
