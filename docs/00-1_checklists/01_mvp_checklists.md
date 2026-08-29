# MVP Detailed Checklists (Phases 0–5)

This is a task-level implementation checklist for the MVP.

**MVP definition:** analytics-only delivery with reproducible ETL, SQLite analytical storage, baseline risk outputs, and one simple stakeholder-facing analytics output.

> **Status note (verified 2026-08-28, corrected to use `uv`):** Reviewed the live codebase and marked items below `[x]` only where verified present/passing, `[~]` where partially done or done differently than specified. This project uses `uv` (not `pip`) for dependency management — verified via `uv sync` + `uv run pytest -q` (currently **fails** — see 0.4 `[build-system]` finding) and `uv run ruff check .` (**passes**).

### Overall Progress Snapshot

| Phase | Status |
|---|---|
| 0 — Foundation and Alignment | **Partially started.** Checklist docs exist; baseline `Settings`, working API client, an existing `04_non_goals.md` doc, and passing `uv run ruff check .` are all pre-existing/verified. **`uv run pytest -q` currently fails** because `pyproject.toml` has no `[build-system]` table, so `uv sync` doesn't install the local package (a real, verified gap — not previously caught). The acceptance-criteria doc (`03_mvp_acceptance_criteria.md`) is now **done** (2026-08-29). New MVP-specific config fields, `.env.example`, decision log, and the broken CI import name are still outstanding. |
| 1 — Data Acquisition and Contracts | **Not started**, except that `TorontoOpenDataClient.search_datasets/get_dataset/get_resource_urls` already exist and work, and raw data folders already exist (with different naming than proposed here). |
| 2 — Analytical Storage (SQLite) | **Not started.** No `db/` package, connection, migrations, or query layer exist in `src/`. |
| 3 — Core ETL and Curated Dataset Build | **Not started.** `etl/ingest_breaks.py` is a docstring-only stub; no transform modules exist. |
| 4 — Baseline Modeling and Scoring | **Not started.** `features/` and `models/` packages exist but are empty (`__init__.py` only). |
| 5 — MVP Delivery: Analytics Consumption | **Not started.** No reporting/BI artifact exists yet. |

---

## Phase 0 — Foundation and Alignment (Detailed)

### 0.1 Scope, Decisions, and Control Documents

- [x] `docs/00-1_checklists/00_high_level_checklist.md` — **exists** (created in prior session step).
- [x] `docs/00-1_checklists/01_mvp_checklists.md` — **exists** (this file).
- [x] Create `docs/00-1_checklists/03_mvp_acceptance_criteria.md` containing, per phase, a table with columns: `Criterion | Measurement Method | Pass Threshold`. — **created 2026-08-29.** Covers all 6 MVP phases (0–5) plus a "Cross-Phase Standing Criteria" table. Note: created as `03_` (not `02_`) per the task instruction; no `02_`-prefixed doc exists in `docs/00-1_checklists/`, so that number is currently unused. Example rows below were all included verbatim except where noted:
  - [x] Phase 1: "Raw ingestion success rate" | "count(files written)/count(datasets attempted)" | "= 100% for 4 MVP datasets"
  - [x] Phase 2: "Migration idempotency" | "run migrate.py twice, diff schema_version table" | "no duplicate/failed rows" — **table name corrected to `schema_migrations`** to match the migration DDL in 2.2 (`000_create_schema_history.sql`); `schema_version` does not exist anywhere in the planned schema.
  - [x] Phase 3: "Curated join coverage" | "matched_rows / total_break_rows" | ">= 95% or documented exception"
  - [x] Phase 4: "Baseline model trains without error" | "exit code of train_model.py" | "0"
  - [x] Phase 5: "Report artifact renders" | "manual open of output file" | "no errors, all sections populated"
- [~] `docs/00-0_overview/04_non_goals.md` — **already exists and substantially covers MVP exclusions** (no real-time/streaming, no live inference API, no asset-level prediction, no operational automation, no cloud-native/orchestration deployment, no advanced ML in early phases, scope-change control). Verbatim MVP-specific bullets below are **not yet appended** to that doc; treat as a gap-fill task, not a from-scratch task:
  - [ ] "No production API/FastAPI deployment in MVP"
  - [ ] "No real-time/streaming inference in MVP"
  - [ ] "No model comparison beyond one baseline algorithm in MVP"
  - [ ] "No authentication/authorization layer in MVP"
  - [ ] "No automated scheduling/orchestration (cron/Airflow) in MVP — manual CLI execution only"
- [ ] Create `docs/11_project_diary_notes/202608_mvp_decisions.md` logging: date, decision, rationale, alternatives considered — starting with the Turso→SQLite decision and the "Analytics-only MVP" scope decision already made in this conversation.

### 0.2 Repository Structure Readiness (exact paths to create if missing)

- [ ] `src/toronto_pipeline_failure_predict/db/__init__.py` — **not present** (no `db/` package exists in `src/` yet).
- [ ] `src/toronto_pipeline_failure_predict/db/connection.py`
- [ ] `src/toronto_pipeline_failure_predict/db/migrate.py`
- [ ] `src/toronto_pipeline_failure_predict/db/migrations/` (empty dir + `.gitkeep`)
- [ ] `src/toronto_pipeline_failure_predict/db/queries/` (empty dir + `.gitkeep`)
- [ ] `src/toronto_pipeline_failure_predict/etl/download.py` — **not present** (`etl/` currently only has `__init__.py` and stub `ingest_breaks.py`).
- [ ] `src/toronto_pipeline_failure_predict/etl/fetch_sources.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/validate_raw.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/run_ingestion.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/run_etl.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/transform/__init__.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/transform/breaks_transform.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/transform/climate_transform.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/transform/soils_transform.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/transform/neighborhoods_transform.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/transform/integrate_curated.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/load/__init__.py`
- [ ] `src/toronto_pipeline_failure_predict/etl/load/load_sqlite.py`
- [~] `src/toronto_pipeline_failure_predict/features/` — **directory exists** (`__init__.py` only, empty); `build_features.py` **not present**.
- [~] `src/toronto_pipeline_failure_predict/models/` — **directory exists** (`__init__.py` only, empty); `train_model.py`, `evaluate_model.py`, `predict_model.py`, `run_modeling.py` **not present**.
- [~] `data/raw/...` — **`data/raw/`, `data/interim/`, `data/processed/` already exist**, but current raw subfolders are `gis/`, `soils/`, `municipal/`, `climate/` (not `watermain_breaks/`/`neighborhoods/` as named here). Reconcile naming or update this checklist to match existing convention before Phase 1 work starts.
- [ ] `data/interim/` , `data/processed/`, `data/local/` (each with `.gitkeep`) — interim/processed exist; **`data/local/` does not exist yet**.
- [ ] `schemas/` with `.gitkeep` — **not present**.
- [~] `tests/db/__init__.py`, `tests/etl/__init__.py`, `tests/models/__init__.py` — **not present**; repo instead already has `tests/unit/`, `tests/integration/`, `tests/system/` (each with `__init__.py`). Decide whether to adopt this existing convention instead of `tests/db|etl|models/` before Phase 2+ tests are written.
- [ ] `reports/validation/`, `reports/etl_runs/` (each with `.gitkeep`) — **not present** (existing `reports/` is the Quarto report structure, unrelated to these run-artifact folders).
- [ ] Verify each new directory is tracked by git (empty dirs need `.gitkeep` since `.gitignore` may exclude `data/`).

### 0.3 Config + Environment Baseline (exact fields)

- [~] `src/toronto_pipeline_failure_predict/config/settings.py` — **file exists with a working baseline `Settings` class** (`PROJECT_NAME`, `VERSION`, `BASE_DIR`, `DATA_DIR`, `RAW_DATA_DIR`, `PROCESSED_DATA_DIR`, `MODELS_DIR`, `LOGS_DIR`, `RANDOM_SEED`, `TEST_SIZE`, `MUNICIPAL_API_URL`, `API_TIMEOUT`, `.env` loading). **None of the new MVP-specific fields below have been added yet**:
  - [ ] `DB_BACKEND: str = "sqlite"`
  - [ ] `SQLITE_PATH: Path = DATA_DIR / "local" / "analytics.sqlite"`
  - [ ] `INTERIM_DATA_DIR: Path = DATA_DIR / "interim"`
  - [ ] `SCHEMAS_DIR: Path = BASE_DIR / "schemas"`
  - [ ] `REPORTS_DIR: Path = BASE_DIR.parent / "reports"` (verify relative to repo root, not `src/`)
  - [ ] `MAX_DOWNLOAD_RETRIES: int = 3`
  - [ ] `DOWNLOAD_TIMEOUT_SECONDS: int = 30`
  - [ ] `RISK_CLASS_THRESHOLDS: dict = {"low": 0.33, "medium": 0.66, "high": 1.0}`
- [ ] Add `__post_init__`/validator (or simple startup check) that creates `DATA_DIR`, `RAW_DATA_DIR`, `PROCESSED_DATA_DIR`, `INTERIM_DATA_DIR`, `MODELS_DIR`, `LOGS_DIR` if they don't exist (`Path.mkdir(parents=True, exist_ok=True)`).
- [ ] Create `.env.example` with keys: `DB_BACKEND`, `SQLITE_PATH`, `MUNICIPAL_API_URL`, `API_TIMEOUT`, `RANDOM_SEED`, `TEST_SIZE`, `MAX_DOWNLOAD_RETRIES`, `DOWNLOAD_TIMEOUT_SECONDS`. — **not present** (`.env.example` does not exist in repo root today).
- [~] `pyproject.toml` — **`pydantic-settings` and `requests` already exist, but only in the `deploy` dependency group, not `[project.dependencies]`** as required here. `scikit-learn` is **not** present in any group yet.
- [ ] Confirm `dependency-groups.dev` includes `pytest>=8.0.0` (**already present**) and add `pytest-cov>=5.0.0` for coverage reporting (**not present**).

### 0.4 Quality Gate Baseline

- [ ] **NEW FINDING (uv-verified):** `pyproject.toml` has **no `[build-system]` table**. Under `uv`, a project without `[build-system]` is treated as a "virtual" (dependency-only) project — `uv sync` installs dependency groups but does **not** build/install the local package itself. Confirmed via `uv sync` + `uv run pytest -q` → `ModuleNotFoundError: No module named 'toronto_pipeline_failure_predict'`. **Fix required:** add a `[build-system]` table (e.g. `hatchling`) and a `[tool.hatch.build.targets.wheel] packages = ["src/toronto_pipeline_failure_predict"]` section (src-layout), then `uv sync` will build/install the package automatically. Verified this fix works in a scratch test (reverted after confirming).
- [ ] `.github/workflows/code_quality.yaml` line ~39: fix `import municipal_pipeline_failure_predict` to `import toronto_pipeline_failure_predict` (**confirmed still broken** — CI import smoke test currently references the wrong/old package name and will fail as written).
- [ ] Add a `pytest` step to `.github/workflows/code_quality.yaml` after the lint step: `uv sync --group dev` then `uv run pytest -q` (**not present** — CI currently only lints + does a raw `pip`/`python` import, no `pytest` invocation, and does not use `uv` at all).
- [~] `tests/test_smoke.py` — **partially verified with `uv`, corrected from an earlier pip-based check**:
  - `uv run ruff check .` → **passes** (`All checks passed!`).
  - `uv run pytest -q` → **currently fails** (`2 failed`) because the local package is not installed under a plain `uv sync` (see `[build-system]` finding above). Tests only pass once the package is installed editable — verified previously via `pip install -e .` in a separate venv, but that is **not** the workflow this project uses. Once the `[build-system]` fix above is applied, `uv sync && uv run pytest -q` should pass (spot-checked in a scratch pyproject edit and confirmed `test_package_import` passes; `test_api_client_import` will still need `requests` promoted to core `[project.dependencies]` per 0.3 above).
- [ ] `README.md` — add a "Quickstart" section with exact `uv`-based commands (**not present** — no Quickstart section currently in `README.md`):
  - [ ] `uv sync --group dev`
  - [ ] `uv run ruff check .`
  - [ ] `uv run pytest -q`
  - [ ] `uv run python -m toronto_pipeline_failure_predict.etl.run_ingestion --dataset all`
  - [ ] `uv run python -m toronto_pipeline_failure_predict.db.migrate`
  - [ ] `uv run python -m toronto_pipeline_failure_predict.etl.run_etl`
  - [ ] `uv run python -m toronto_pipeline_failure_predict.models.run_modeling --mode train+score`

### 0.5 Phase 0 Exit Gate (verify each explicitly)

- [ ] `uv run pytest -q` passes locally with 0 failures. — **currently fails** under `uv` until the `[build-system]` fix (0.4) and core-dependency fix (0.3, `requests`) are applied. (Superseded an earlier incorrect "verified" note that had used `pip install -e .` in an ad hoc venv, not this project's `uv` workflow.)
- [x] `uv run ruff check .` passes with 0 errors. — **verified**.
- [ ] `git status` shows all Phase 0 directories/files committed (no untracked scaffolding left behind).
- [x] `docs/00-1_checklists/03_mvp_acceptance_criteria.md` exists and covers all 6 MVP phases. — **verified**: 6 per-phase tables (Phases 0–5) present, each with `Criterion | Measurement Method | Pass Threshold`.

---

## Phase 1 — Data Acquisition and Contracts (Detailed)

### 1.1 Source Contracts (Per Dataset — each doc must contain all listed fields)

- [ ] `docs/02_data_sources/02_source_contract_watermain_breaks.md`:
  - [ ] CKAN package id (exact string to pass to `get_dataset()`)
  - [ ] preferred resource format (`CSV` first, `GeoJSON` fallback)
  - [ ] required raw columns list (e.g., break id/date/location fields as published)
  - [ ] assumed primary/natural key (e.g., composite of date + location if no explicit id)
  - [ ] known refresh cadence (annual/rolling) and last-checked date
  - [ ] known data quality issues (missing coordinates, inconsistent date formats, etc.)
- [ ] `docs/02_data_sources/03_source_contract_climate.md` — same 6 fields, plus station id(s) used and date range covered.
- [ ] `docs/02_data_sources/04_source_contract_soils.md` — same 6 fields, plus geometry type (polygon) and CRS used.
- [ ] `docs/02_data_sources/05_source_contract_neighborhoods.md` — same 6 fields, plus neighborhood id/name field mapping.

### 1.2 API and Download Implementation

- [~] `src/toronto_pipeline_failure_predict/api/toronto_client.py` — **core methods already implemented and verified present**, but without the hardening noted below:
  - [x] `search_datasets(self, query: str, rows: int = 10) -> dict` — **implemented** (matches signature). Return-type hint/expanded docstring still missing.
  - [x] `get_dataset(self, package_id: str) -> dict` — **implemented** (matches signature, calls `package_show`). **No `try/except` guard yet** — a failed/404 request will currently raise via `response.raise_for_status()` rather than fail-safely returning `None` as the project's documented convention (`docs/16_api/00_toronto_open_data_client.md`) intends.
  - [x] `get_resource_urls(self, dataset_json: dict) -> list[str]` — **implemented** (filters resources by `csv`/`geojson` format). **No guard for missing `"result"`/`"resources"` keys** — will raise `KeyError` on malformed input instead of returning `[]`.
- [ ] `src/toronto_pipeline_failure_predict/etl/download.py` — **not present**:
  - [ ] `download_file(url: str, destination_path: Path, timeout: int = 30, max_retries: int = 3) -> Path`
  - [ ] retry loop with exponential backoff (`1s, 2s, 4s`) on `requests.RequestException`
  - [ ] stream download using `requests.get(url, stream=True)` and write in `8192`-byte chunks
  - [ ] raise `RuntimeError` with descriptive message after `max_retries` exhausted
  - [ ] return final written `Path`
- [ ] `src/toronto_pipeline_failure_predict/etl/fetch_sources.py` — **not present** (note: `src/toronto_pipeline_failure_predict/etl/ingest_breaks.py` exists today but is a docstring-only stub with no functions implemented):
  - [ ] `fetch_watermain_breaks() -> Path`
  - [ ] `fetch_climate() -> Path`
  - [ ] `fetch_soils() -> Path`
  - [ ] `fetch_neighborhoods() -> Path`
  - [ ] each function: call `TorontoOpenDataClient`, resolve resource URL, call `download_file`, write to `data/raw/<dataset>/<original_filename or dataset>_<YYYYMMDD>.<ext>`
  - [ ] each function must log dataset name, resolved URL, and destination path via project logger

### 1.3 Raw Validation Implementation

- [ ] `src/toronto_pipeline_failure_predict/etl/validate_raw.py`:
  - [ ] `check_required_columns(df: pd.DataFrame, required: list[str]) -> list[str]` — returns list of missing column names (empty list = pass)
  - [ ] `check_null_threshold(df: pd.DataFrame, column: str, max_null_fraction: float = 0.05) -> bool`
  - [ ] `check_duplicate_keys(df: pd.DataFrame, key_columns: list[str]) -> int` — returns count of duplicate key rows
  - [ ] `coerce_types_report(df: pd.DataFrame, expected_types: dict[str, str]) -> dict[str, str]` — non-mutating; returns `{column: "ok"|"mismatch"}` per column
  - [ ] `validate_dataset(df: pd.DataFrame, schema: dict) -> ValidationResult` (dataclass with `passed: bool`, `errors: list[str]`)
- [ ] Schema files under `schemas/` (YAML, one key per required column with `type` and `nullable`):
  - [ ] `watermain_breaks_schema.yaml`
  - [ ] `climate_schema.yaml`
  - [ ] `soils_schema.yaml`
  - [ ] `neighborhoods_schema.yaml`
- [ ] Validation summary writer: `write_validation_report(result: ValidationResult, dataset: str) -> Path` writing to `reports/validation/<dataset>_<timestamp>.md` with pass/fail, missing columns, null fractions, duplicate count.

### 1.4 Ingestion CLI/Runner

- [ ] `src/toronto_pipeline_failure_predict/etl/run_ingestion.py`:
  - [ ] `argparse` with `--dataset` choice from `{"all", "watermain", "climate", "soils", "neighborhoods"}` (default `"all"`)
  - [ ] `--overwrite` boolean flag (default `False`) — if `False` and destination file exists, skip download and log a "skipped, already exists" message
  - [ ] on validation failure: print failing checks to stderr and `sys.exit(1)`
  - [ ] on success: print one-line summary per dataset (`rows`, `columns`, `destination path`)
- [ ] `tests/etl/test_run_ingestion_cli.py`:
  - [ ] test `--dataset` accepts each valid choice
  - [ ] test invalid `--dataset` value raises `SystemExit` via argparse

### 1.5 Phase 1 Exit Gate

- [ ] `uv run python -m toronto_pipeline_failure_predict.etl.run_ingestion --dataset all` completes with exit code 0 on a clean machine.
- [ ] Four raw files exist under `data/raw/<dataset>/` with non-zero size.
- [ ] Four validation report files exist under `reports/validation/` with `passed: true` (or documented, approved exceptions).
- [ ] All four source contract docs exist and are filled in (no placeholder text remaining).
- [ ] Re-running the same command without `--overwrite` skips re-download and still exits 0.

---

## Phase 2 — Analytical Storage and Data Model (SQLite, Detailed)

### 2.1 DB Module Implementation

- [ ] `src/toronto_pipeline_failure_predict/db/connection.py`:
  - [ ] `get_sqlite_connection(path: str | Path = settings.SQLITE_PATH) -> sqlite3.Connection`
  - [ ] set `conn.execute("PRAGMA foreign_keys = ON")` immediately after connecting
  - [ ] set `conn.row_factory = sqlite3.Row` for dict-like row access
  - [ ] `@contextmanager def sqlite_session(path=...)` yielding a connection and committing/closing on exit, rolling back on exception
- [ ] `src/toronto_pipeline_failure_predict/db/session.py`:
  - [ ] `execute_sql(conn, sql: str, params: tuple = ()) -> sqlite3.Cursor`
  - [ ] `fetch_df(conn, sql: str, params: tuple = ()) -> pd.DataFrame` (via `pd.read_sql_query`)
  - [ ] `write_df(conn, df: pd.DataFrame, table: str, if_exists: str = "append") -> int` returning rows written
- [ ] `src/toronto_pipeline_failure_predict/db/__init__.py` — export `get_sqlite_connection`, `sqlite_session`, `execute_sql`, `fetch_df`, `write_df`.

### 2.2 Migration Files (exact DDL — column name, type, constraint)

- [ ] `db/migrations/001_create_core_tables.sql`:
  - [ ] `pipe_breaks_clean(break_id INTEGER PRIMARY KEY, break_date DATE NOT NULL, year INTEGER NOT NULL, month INTEGER NOT NULL, neighborhood TEXT NOT NULL, break_count INTEGER NOT NULL, latitude REAL, longitude REAL, source TEXT NOT NULL, ingestion_timestamp TIMESTAMP NOT NULL)`
  - [ ] `climate_monthly(year INTEGER NOT NULL, month INTEGER NOT NULL, rainfall_mm REAL, mean_temp_c REAL, drought_index REAL, source TEXT NOT NULL, PRIMARY KEY (year, month))`
  - [ ] `soil_zones(zone_id INTEGER PRIMARY KEY, neighborhood TEXT NOT NULL, zone_code TEXT NOT NULL, description TEXT, corrosivity_index REAL)`
  - [ ] `neighborhoods(neighborhood_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, region TEXT, geometry_wkt TEXT)`
- [ ] `db/migrations/002_create_feature_table.sql`:
  - [ ] `pipe_features_monthly(year INTEGER NOT NULL, month INTEGER NOT NULL, neighborhood TEXT NOT NULL, break_count_rolling_12 REAL, avg_rainfall_6mo REAL, avg_temp_6mo REAL, soil_corrosivity REAL, prior_break_rate REAL, feature_version TEXT NOT NULL, generated_at TIMESTAMP NOT NULL, PRIMARY KEY (year, month, neighborhood, feature_version))`
- [ ] `db/migrations/003_create_prediction_tables.sql`:
  - [ ] `pipe_break_risk_scores(year INTEGER NOT NULL, month INTEGER NOT NULL, neighborhood TEXT NOT NULL, risk_score REAL NOT NULL, risk_class TEXT NOT NULL, model_version TEXT NOT NULL, prediction_timestamp TIMESTAMP NOT NULL, PRIMARY KEY (year, month, neighborhood, model_version))`
  - [ ] `model_metadata(model_version TEXT PRIMARY KEY, model_type TEXT NOT NULL, training_start_date DATE, training_end_date DATE, features_version TEXT, metrics_json TEXT)`
  - [ ] `etl_runs(run_id INTEGER PRIMARY KEY AUTOINCREMENT, pipeline_name TEXT NOT NULL, run_timestamp TIMESTAMP NOT NULL, status TEXT NOT NULL, row_count INTEGER, notes TEXT)`
- [ ] `db/migrations/004_add_indexes.sql`:
  - [ ] `CREATE INDEX idx_breaks_year_month ON pipe_breaks_clean(year, month)`
  - [ ] `CREATE INDEX idx_breaks_neighborhood ON pipe_breaks_clean(neighborhood)`
  - [ ] `CREATE INDEX idx_features_neighborhood ON pipe_features_monthly(neighborhood)`
  - [ ] `CREATE INDEX idx_scores_neighborhood ON pipe_break_risk_scores(neighborhood)`
- [ ] `db/migrations/000_create_schema_history.sql` (apply first): `schema_migrations(version TEXT PRIMARY KEY, applied_at TIMESTAMP NOT NULL)`

### 2.3 Migration Runner

- [ ] `src/toronto_pipeline_failure_predict/db/migrate.py`:
  - [ ] `list_migration_files() -> list[Path]` sorted lexically by filename prefix (`000_`, `001_`, ...)
  - [ ] `get_applied_versions(conn) -> set[str]` reading `schema_migrations`
  - [ ] `apply_migration(conn, path: Path) -> None` — execute full SQL file via `conn.executescript`, then `INSERT INTO schema_migrations`
  - [ ] `run_migrations(db_path: str | Path = settings.SQLITE_PATH) -> list[str]` returning list of newly applied version strings; must be safe to call twice in a row (second call returns empty list)
  - [ ] CLI entrypoint: `uv run python -m toronto_pipeline_failure_predict.db.migrate` prints applied versions or "up to date"

### 2.4 Query and Load Layer

- [ ] `db/queries/validate_schema.sql` — `SELECT name FROM sqlite_master WHERE type='table'`
- [ ] `db/queries/row_counts.sql` — one `SELECT 'table_name', COUNT(*) FROM table_name` per core table, `UNION ALL`'d
- [ ] `db/queries/duplicate_keys_breaks.sql` — `GROUP BY` natural key `HAVING COUNT(*) > 1` for `pipe_breaks_clean`
- [ ] `src/toronto_pipeline_failure_predict/etl/load/load_sqlite.py`:
  - [ ] `load_breaks(conn, df: pd.DataFrame) -> int`
  - [ ] `load_climate(conn, df: pd.DataFrame) -> int`
  - [ ] `load_soils(conn, df: pd.DataFrame) -> int`
  - [ ] `load_neighborhoods(conn, df: pd.DataFrame) -> int`
  - [ ] each function validates required columns present before calling `write_df`, and uses `if_exists="replace"` for MVP simplicity (documented as a known limitation vs. true upsert)
  - [ ] `record_etl_run(conn, pipeline_name: str, status: str, row_count: int, notes: str = "") -> None` writing to `etl_runs`

### 2.5 DB Tests

- [ ] `tests/db/test_connection.py`:
  - [ ] `test_connection_creates_file_if_missing(tmp_path)`
  - [ ] `test_foreign_keys_pragma_enabled(tmp_path)`
- [ ] `tests/db/test_migrations.py`:
  - [ ] `test_all_migrations_apply_cleanly(tmp_path)` — assert expected table names present via `sqlite_master`
  - [ ] `test_migrations_are_idempotent(tmp_path)` — run twice, assert second run applies zero new versions
- [ ] `tests/db/test_load_sqlite.py`:
  - [ ] `test_load_breaks_inserts_expected_row_count(tmp_path)`
  - [ ] `test_load_breaks_missing_column_raises(tmp_path)`
- [ ] All DB tests must use `tmp_path` fixture for isolated SQLite files (never touch `data/local/analytics.sqlite`).

### 2.6 Phase 2 Exit Gate

- [ ] `uv run python -m toronto_pipeline_failure_predict.db.migrate` on a fresh temp path creates all 8 tables (`schema_migrations` + 7 domain tables).
- [ ] Running migrate twice produces "up to date" on the second run with no errors.
- [ ] `uv run pytest tests/db -q` passes with 0 failures.
- [ ] Row-count query returns 0 for all tables immediately after migration (empty schema is valid state).

---

## Phase 3 — Core ETL and Curated Dataset Build (Detailed)

### 3.1 Transform Modules (Per Dataset — exact function contracts)

- [ ] `src/toronto_pipeline_failure_predict/etl/transform/breaks_transform.py`:
  - [ ] `parse_break_dates(df: pd.DataFrame, date_column: str) -> pd.DataFrame` — coerce to `datetime64`, drop/flag unparsable rows, log count dropped
  - [ ] `derive_year_month(df: pd.DataFrame) -> pd.DataFrame` — adds `year`, `month` int columns from parsed date
  - [ ] `clean_coordinates(df: pd.DataFrame, lat_col: str, lon_col: str) -> pd.DataFrame` — drop rows outside Toronto bounding box (approx lat 43.4–43.9, lon -79.7–-79.0), log count dropped
  - [ ] `standardize_neighborhood(df: pd.DataFrame, neighborhoods_ref: pd.DataFrame) -> pd.DataFrame` — spatial or name-based join to canonical neighborhood list; unmatched rows flagged with `neighborhood = "UNMATCHED"` rather than dropped
  - [ ] `aggregate_monthly_breaks(df: pd.DataFrame) -> pd.DataFrame` — group by `(year, month, neighborhood)`, produce `break_count`
- [ ] `.../climate_transform.py`:
  - [ ] `normalize_to_monthly(df: pd.DataFrame) -> pd.DataFrame` — resample/aggregate to `(year, month)` grain with mean temp, summed rainfall
  - [ ] `standardize_units(df: pd.DataFrame) -> pd.DataFrame` — confirm mm for rainfall, °C for temperature; convert if source uses other units
- [ ] `.../soils_transform.py`:
  - [ ] `normalize_zone_ids(df: pd.DataFrame) -> pd.DataFrame`
  - [ ] `compute_corrosivity_index(df: pd.DataFrame) -> pd.DataFrame` — documented simple heuristic formula (e.g., weighted combination of soil attributes) with a `ponytail`-style comment noting it is a v1 heuristic, not a geotechnical model
- [ ] `.../neighborhoods_transform.py`:
  - [ ] `normalize_names(df: pd.DataFrame) -> pd.DataFrame` — strip whitespace, title-case, resolve known aliases via a static mapping dict
  - [ ] `enforce_unique_keys(df: pd.DataFrame) -> pd.DataFrame` — raise `ValueError` if duplicate neighborhood names remain after normalization

### 3.2 Curated Integration Logic

- [ ] `src/toronto_pipeline_failure_predict/etl/transform/integrate_curated.py`:
  - [ ] `build_curated_breaks(breaks_df, neighborhoods_df) -> pd.DataFrame`
  - [ ] `join_climate_and_soil(breaks_df, climate_df, soils_df) -> pd.DataFrame` — left-join on `(year, month)` for climate and on `neighborhood` for soils
  - [ ] `log_join_coverage(before_rows: int, after_rows: int, join_name: str) -> None` — logs percentage retained; raise a warning (not failure) if coverage `< 90%`
  - [ ] `write_curated_outputs(df: pd.DataFrame, dataset_name: str) -> Path` — writes Parquet to `data/processed/<dataset_name>.parquet`
- [ ] Canonical key enforcement: every curated table function must assert `{"year", "month", "neighborhood"}.issubset(df.columns)` before returning.

### 3.3 ETL Orchestration Runner

- [ ] `src/toronto_pipeline_failure_predict/etl/run_etl.py`:
  - [ ] stage enum: `EXTRACT`, `VALIDATE_RAW`, `TRANSFORM`, `VALIDATE_PROCESSED`, `LOAD`
  - [ ] `--from-stage` / `--to-stage` args accepting stage names, default full pipeline
  - [ ] on any stage failure: log the specific dataset + stage + exception message, then `sys.exit(1)` (no partial state left marked as success)
  - [ ] on success: call `record_etl_run(conn, "run_etl", "success", row_count=<total curated rows>)`

### 3.4 ETL Tests

- [ ] `tests/etl/test_breaks_transform.py`:
  - [ ] `test_parse_break_dates_drops_invalid_rows()`
  - [ ] `test_derive_year_month_correct_values()`
  - [ ] `test_clean_coordinates_drops_out_of_bounds()`
- [ ] `tests/etl/test_climate_transform.py`:
  - [ ] `test_normalize_to_monthly_aggregates_correctly()`
- [ ] `tests/etl/test_integrate_curated.py`:
  - [ ] `test_join_climate_and_soil_preserves_row_count_within_tolerance()`
  - [ ] `test_write_curated_outputs_creates_parquet_file(tmp_path)`
- [ ] `tests/etl/test_run_etl_integration.py`:
  - [ ] uses small fixture CSVs (5–10 synthetic rows) → runs full `run_etl.py` pipeline against a `tmp_path` SQLite DB → asserts curated tables populated with expected row counts

### 3.5 Data Quality and Reproducibility Checks

- [ ] Every processed output validated for non-null `(year, month, neighborhood)` before persistence — raise on violation.
- [ ] All DataFrames sorted by `(year, month, neighborhood)` before writing (deterministic diff-friendly output).
- [ ] `reports/etl_runs/<YYYYMMDD_HHMMSS>.md` written each run with: dataset row counts in/out per stage, dropped-row counts with reasons, join coverage percentages.
- [ ] Invalid record policy documented in `docs/17_etl/00_etl_ingestor.md` addendum: "drop with logged reason" for out-of-bounds coordinates/unparsable dates; "flag as UNMATCHED" for neighborhood join misses (never silently drop breaks rows).

### 3.6 Phase 3 Exit Gate

- [ ] `uv run python -m toronto_pipeline_failure_predict.etl.run_etl` exits 0 on real (or fixture) MVP data end-to-end.
- [ ] `uv run pytest tests/etl -q` passes.
- [ ] `pipe_breaks_clean`, `climate_monthly`, `soil_zones` tables in SQLite have row counts `> 0` after a real run.
- [ ] Running `run_etl.py` twice with identical inputs produces identical row counts (verified via row-count query).

---

## Phase 4 — Baseline Modeling and Scoring Outputs (Detailed)

### 4.1 Feature Generation

- [ ] `src/toronto_pipeline_failure_predict/features/build_features.py`:
  - [ ] `load_curated_breaks(conn) -> pd.DataFrame`, `load_curated_climate(conn) -> pd.DataFrame`, `load_curated_soils(conn) -> pd.DataFrame`
  - [ ] `compute_rolling_break_count(df: pd.DataFrame, window_months: int = 12) -> pd.DataFrame` — per-neighborhood rolling sum, sorted by time
  - [ ] `compute_rolling_climate_avg(df: pd.DataFrame, window_months: int = 6) -> pd.DataFrame` — rolling mean rainfall/temp
  - [ ] `assemble_feature_table(breaks, climate, soils, feature_version: str) -> pd.DataFrame` — joins on `(year, month, neighborhood)`, adds `feature_version`, `generated_at = datetime.utcnow()`
  - [ ] `write_features(conn, df: pd.DataFrame) -> int` — writes to `pipe_features_monthly` (upsert on primary key or `if_exists="replace"` per current version, documented)
- [ ] `configs/feature_config.yaml`: `feature_version`, `rolling_break_window_months`, `rolling_climate_window_months`.

### 4.2 Model Training Module

- [ ] `src/toronto_pipeline_failure_predict/models/train_model.py`:
  - [ ] `load_training_frame(conn, feature_version: str) -> tuple[pd.DataFrame, pd.Series]` returning `(X, y)` where `y` is next-period break occurrence/count
  - [ ] `time_aware_split(X, y, test_size: float = settings.TEST_SIZE) -> tuple` — split by max date cutoff, not random shuffle (prevents leakage)
  - [ ] `train_baseline_model(X_train, y_train, random_state: int = settings.RANDOM_SEED)` — e.g., `sklearn.linear_model.PoissonRegressor` or `LogisticRegression` per problem framing (classification vs. count) — must match target definition in `docs/00-0_overview/01_watermain_break_analytics.md`
  - [ ] `save_model_artifact(model, model_version: str) -> Path` — `joblib.dump` to `models/<model_version>.joblib`
  - [ ] `write_model_metadata(conn, model_version, model_type, training_start_date, training_end_date, features_version, metrics_json) -> None`
- [ ] `src/toronto_pipeline_failure_predict/models/evaluate_model.py`:
  - [ ] `compute_metrics(y_true, y_pred) -> dict` — MAE/RMSE (regression) or precision/recall/F1 + ROC-AUC (classification), matching chosen target type
  - [ ] `error_slice_by_neighborhood(y_true, y_pred, neighborhoods) -> pd.DataFrame` — per-neighborhood metric breakdown for sanity review

### 4.3 Scoring Module

- [ ] `src/toronto_pipeline_failure_predict/models/predict_model.py`:
  - [ ] `load_model_artifact(model_version: str)`
  - [ ] `score_features(model, X: pd.DataFrame) -> np.ndarray`
  - [ ] `normalize_risk_score(raw_scores: np.ndarray) -> np.ndarray` — min-max scale to `[0, 1]`
  - [ ] `assign_risk_class(score: float, thresholds: dict = settings.RISK_CLASS_THRESHOLDS) -> str` — returns `"low"`/`"medium"`/`"high"`
  - [ ] `write_predictions(conn, df: pd.DataFrame, model_version: str) -> int` — writes to `pipe_break_risk_scores` with `prediction_timestamp = datetime.utcnow()`

### 4.4 Modeling Runner

- [ ] `src/toronto_pipeline_failure_predict/models/run_modeling.py`:
  - [ ] `--mode` choice `{"train", "score", "train+score"}` (default `"train+score"`)
  - [ ] `--model-version` optional override; default auto-generated as `v{YYYYMMDD}_{short-hash-of-feature-config}`
  - [ ] exits 1 on missing feature table data (with message telling user to run Phase 3/4.1 first)

### 4.5 Modeling Tests

- [ ] `tests/models/test_build_features.py`:
  - [ ] `test_compute_rolling_break_count_window_correctness()`
  - [ ] `test_assemble_feature_table_has_no_nulls_in_keys()`
- [ ] `tests/models/test_train_model.py`:
  - [ ] `test_time_aware_split_no_future_leakage()`
  - [ ] `test_train_baseline_model_reproducible_with_fixed_seed()`
- [ ] `tests/models/test_predict_model.py`:
  - [ ] `test_normalize_risk_score_bounds_0_to_1()`
  - [ ] `test_assign_risk_class_thresholds()`
- [ ] `tests/models/test_run_modeling_integration.py` — fixture curated tables → features → train → score → assert `pipe_break_risk_scores` populated.

### 4.6 Phase 4 Exit Gate

- [ ] `uv run python -m toronto_pipeline_failure_predict.models.run_modeling --mode train+score` exits 0 on real MVP data.
- [ ] `pipe_break_risk_scores` has one row per `(year, month, neighborhood)` in the scoring horizon.
- [ ] `model_metadata` has exactly one row per trained `model_version`.
- [ ] `uv run pytest tests/models -q` passes.
- [ ] Evaluation metrics written to `reports/model_evaluation/<model_version>.md`.

---

## Phase 5 — MVP Delivery: Analytics Consumption (Detailed)

### 5.1 Reporting Dataset Layer

- [ ] `db/queries/reporting_view.sql`: `CREATE VIEW joined_risk_view AS SELECT r.year, r.month, r.neighborhood, r.risk_score, r.risk_class, c.rainfall_mm, c.mean_temp_c, s.corrosivity_index FROM pipe_break_risk_scores r LEFT JOIN climate_monthly c USING (year, month) LEFT JOIN soil_zones s ON r.neighborhood = s.neighborhood`
- [ ] `src/toronto_pipeline_failure_predict/db/queries.py` helper: `get_reporting_extract(conn) -> pd.DataFrame` querying `joined_risk_view`
- [ ] Completeness check: `assert_no_nulls(df, required_cols=["year","month","neighborhood","risk_score","risk_class"])` before export

### 5.2 MVP Report/BI Artifact

- [ ] Choose and implement ONE of:
  - [ ] `src/toronto_pipeline_failure_predict/reporting/generate_report.py` — builds a static HTML/Markdown report using `reports/joined_risk_view` extract (tables + matplotlib/seaborn charts), OR
  - [ ] `powerbi/datasets/joined_risk_view.sql` + documented Power BI connection steps in `docs/05_powerbi/00_powerbi_dataset_requirements.md`
- [ ] Minimum content, regardless of format chosen:
  - [ ] ranked table: top-N highest-risk neighborhoods for latest scored month
  - [ ] time trend chart: total predicted risk score by month
  - [ ] simple driver panel: risk score vs. rainfall/corrosivity scatter or bar comparison

### 5.3 Documentation for Consumption

- [ ] `docs/04_reports/01_summary_reports/2026_mvp_release_notes.md` — what shipped, what didn't, known caveats.
- [ ] `docs/10_operations/01_mvp_runbook.md` — exact ordered command list (ingestion → migrate → etl → modeling → report), expected artifacts after each step, and a troubleshooting table (`symptom | likely cause | fix`).
- [ ] `docs/10_operations/02_mvp_data_lineage.md` — table mapping each curated/feature/prediction table to its upstream raw source file(s).

### 5.4 End-to-End Validation

- [ ] Execute the full runbook command sequence from a clean clone/environment.
- [ ] Record actual row counts, timings, and any manual interventions in `docs/04_reports/01_summary_reports/2026_mvp_final_run_summary.md`.
- [ ] Confirm every Phase 0–5 exit gate checkbox in this document is checked.
- [ ] Update `docs/00-0_overview/06_versioning_strategy.md` and tag release (e.g., `v0.2.0` — MVP) per project versioning convention.

### 5.5 Phase 5 Exit Gate

- [ ] Report/BI artifact opens/renders without error and shows non-empty, sensible data.
- [ ] Runbook has been executed start-to-finish by someone other than the original author (or a fresh clone), if feasible.
- [ ] All MVP assumptions/limitations are listed in release notes.
- [ ] Git tag for MVP release exists and points to the validated commit.

---

## Cross-Phase Tracking (Operational)

### Backlog Hygiene

- [ ] Track tasks as issues labeled `phase-0` through `phase-5`, one issue per checklist sub-bullet group (not one giant issue per phase).
- [ ] Blocked tasks must state the exact unblocking condition (e.g., "blocked on Phase 2.2 migration file existing").
- [ ] One named owner per checklist item; unowned items are not "in progress."

### Change Control

- [ ] Any scope addition beyond what's listed here requires a new sub-bullet added to this file before work starts (no silent scope creep).
- [ ] Any schema change requires: new migration file + this checklist updated + affected tests updated in the same change set.
- [ ] Any change to CLI flags/runner behavior requires the runbook (`docs/10_operations/01_mvp_runbook.md`) to be updated in the same change set.

### Quality Baseline

- [ ] Every new `.py` module listed above ships with at least one corresponding test file/function before being marked complete here.
- [ ] Every CLI/runner script has at least one invocation-level (not just unit-level) test.
- [ ] `uv run pytest -q` and `uv run ruff check .` must both be green before checking off any Phase Exit Gate.
