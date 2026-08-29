# MVP Acceptance Criteria (Phases 0–5)

This document defines the **objective, measurable** acceptance criteria for each MVP phase. It is the pass/fail authority for the Phase Exit Gates in [`01_mvp_checklists.md`](01_mvp_checklists.md).

**MVP definition:** analytics-only delivery with reproducible ETL, SQLite analytical storage, baseline risk outputs, and one simple stakeholder-facing analytics output.

## How to Use This Document

- Each phase has one table with columns: `Criterion | Measurement Method | Pass Threshold | Date Met`.
- A phase is **accepted** only when *every* criterion in its table passes, or a failing criterion has a written, dated exception in `docs/11_project_diary_notes/202608_mvp_decisions.md`.
- "Measurement Method" must be executable/observable by someone other than the author — no criterion may resolve to "author judgement."
- All commands assume this project's `uv` workflow (`uv run ...`), not bare `python`/`pip`.
- The **4 MVP datasets** referenced throughout are: watermain breaks, climate, soils, neighborhoods.

### `Date Met` Column Convention

- Enter an ISO date (`YYYY-MM-DD`) **only** on the day the criterion was actually measured and observed to pass — not the day the work was written.
- `—` means **not yet met**: either not measured, or measured and failing. Where a criterion is known to be *currently failing*, that is annotated inline (e.g. `— (failing: …)`) so a blank is never mistaken for "untested."
- A criterion that regresses gets its date **cleared back to `—`**, with the regression logged in the decision log. Dates are evidence of a passing observation, not a permanent award.
- Date + measurement method together must be enough for a reviewer to re-run the check and reproduce the result.

---

## Phase 0 — Foundation and Alignment

| Criterion | Measurement Method | Pass Threshold | Date Met |
|---|---|---|---|
| Test suite green | `uv run pytest -q` exit code | `0`, 0 failures, 0 errors | — (failing: 2 failed — no `[build-system]` in `pyproject.toml`, see checklist 0.4) |
| Lint clean | `uv run ruff check .` exit code | `0` (`All checks passed!`) | 2026-08-28 |
| Local package importable under `uv` | `uv sync` then `uv run python -c "import toronto_pipeline_failure_predict"` | exit code `0`, no `ModuleNotFoundError` | — (failing: `ModuleNotFoundError`, same root cause as above) |
| CI import smoke test references correct package | grep `.github/workflows/code_quality.yaml` for `municipal_pipeline_failure_predict` | 0 matches | — (failing: wrong package name still present) |
| CI runs tests | grep `.github/workflows/code_quality.yaml` for `uv run pytest` | ≥ 1 match, and the step runs after lint | — |
| Required config fields present | `uv run python -c "from toronto_pipeline_failure_predict.config.settings import Settings; s=Settings()"` then assert each field in checklist 0.3 | all 8 new MVP fields resolve without `AttributeError` | — |
| Config creates required directories | instantiate `Settings` on a clean tree, then `ls` the 6 dirs from checklist 0.3 | all 6 exist | — |
| `.env.example` complete | diff key list in `.env.example` against the 8 keys in checklist 0.3 | all 8 keys present, no missing/extra | — |
| Scaffolding committed | `git status --porcelain` after Phase 0 work | no untracked/modified Phase 0 files | — |
| Control documents exist | file existence check on the 3 docs in checklist 0.1 | all present, no placeholder/TODO text remaining | — |
| This acceptance doc covers MVP | count phase tables in this file | 6 tables (Phases 0–5) | 2026-08-29 |

---

## Phase 1 — Data Acquisition and Contracts

| Criterion | Measurement Method | Pass Threshold | Date Met |
|---|---|---|---|
| **Raw ingestion success rate** | `count(files written) / count(datasets attempted)` | `= 100%` for the 4 MVP datasets | — |
| Ingestion runner exits cleanly | exit code of `uv run python -m toronto_pipeline_failure_predict.etl.run_ingestion --dataset all` | `0` | — |
| Raw files non-empty | `stat -c %s` on each file under `data/raw/<dataset>/` | all 4 files size `> 0` bytes | — |
| Raw validation passes | read `passed:` field in each `reports/validation/<dataset>_<timestamp>.md` | 4/4 `passed: true`, or a documented approved exception per failure | — |
| Idempotent re-run | re-run the same command without `--overwrite`, capture exit code + log | exit `0` and one "skipped, already exists" log line per dataset; no file mtime change | — |
| Download retry hardening | unit test: patch `requests.get` to raise `RequestException` 3× | `RuntimeError` raised after `max_retries`, with backoff `1s, 2s, 4s` observed | — |
| API client fails safely | unit test: `get_dataset()` against a 404, `get_resource_urls({})` on malformed input | returns `None` / `[]` respectively; no unhandled exception | — |
| Source contracts complete | inspect the 4 docs in checklist 1.1 for all required fields | 4/4 docs, every listed field populated, no placeholder text | — |
| Schema files present | file existence check under `schemas/` | 4 YAML schemas, each parseable by `yaml.safe_load` | — |
| CLI arg validation | `tests/etl/test_run_ingestion_cli.py` | all 5 valid `--dataset` choices accepted; invalid value raises `SystemExit` | — |

---

## Phase 2 — Analytical Storage (SQLite)

| Criterion | Measurement Method | Pass Threshold | Date Met |
|---|---|---|---|
| **Migration idempotency** | run `migrate.py` twice, diff the `schema_migrations` table[^1] | no duplicate/failed rows; second run applies 0 new versions and prints "up to date" | — |
| Fresh migration creates full schema | `uv run python -m toronto_pipeline_failure_predict.db.migrate` on a fresh temp path, then `SELECT name FROM sqlite_master WHERE type='table'` | 9 tables present: `schema_migrations` + 8 domain tables[^2] | — |
| Indexes created | `SELECT name FROM sqlite_master WHERE type='index'` | all 4 indexes from migration `004` present | — |
| Foreign keys enforced | `PRAGMA foreign_keys` on a connection from `get_sqlite_connection()` | returns `1` | — |
| Empty-schema row counts | run `db/queries/row_counts.sql` immediately after migration | `0` for all tables (valid empty state, not an error) | — |
| DB test suite green | `uv run pytest tests/db -q` exit code | `0`, 0 failures | — |
| Test isolation | grep `tests/db/` for `analytics.sqlite` | 0 matches — every test uses the `tmp_path` fixture | — |
| Load functions validate input | `test_load_breaks_missing_column_raises` | raises before any write; target table row count unchanged | — |
| ETL run auditing | call `record_etl_run(...)`, then `SELECT COUNT(*) FROM etl_runs` | increments by exactly 1 per call, `status` persisted | — |

[^1]: The migration DDL in checklist 2.2 names this table `schema_migrations` (created by `000_create_schema_history.sql`). Earlier drafts referred to it as `schema_version`; `schema_migrations` is authoritative.
[^2]: Domain tables: `pipe_breaks_clean`, `climate_monthly`, `soil_zones`, `neighborhoods`, `pipe_features_monthly`, `pipe_break_risk_scores`, `model_metadata`, `etl_runs`. Note: the Phase 2 exit gate in `01_mvp_checklists.md` §2.6 says "8 tables (`schema_migrations` + 7 domain tables)" — that count is off by one against the migration DDL, which defines 8 domain tables. `9 = schema_migrations + 8` is correct.

---

## Phase 3 — Core ETL and Curated Dataset Build

| Criterion | Measurement Method | Pass Threshold | Date Met |
|---|---|---|---|
| **Curated join coverage** | `matched_rows / total_break_rows` from `log_join_coverage` output | `>= 95%`, or a documented exception | — |
| ETL runner exits cleanly | exit code of `uv run python -m toronto_pipeline_failure_predict.etl.run_etl` | `0` end-to-end on real (or fixture) MVP data | — |
| Curated tables populated | `SELECT COUNT(*)` on `pipe_breaks_clean`, `climate_monthly`, `soil_zones` | all `> 0` after a real run | — |
| Deterministic re-run | run `run_etl.py` twice with identical inputs, diff `row_counts.sql` output | byte-identical row counts | — |
| Deterministic output ordering | assert each written frame is sorted by `(year, month, neighborhood)` | sorted; re-write produces an identical Parquet diff | — |
| Canonical key integrity | null check on `(year, month, neighborhood)` in every processed output | 0 nulls — violation raises, does not warn | — |
| No silent row loss | compare stage-in vs. stage-out counts in `reports/etl_runs/<ts>.md` | every dropped row has a logged reason; neighborhood join misses are `UNMATCHED`, never dropped | — |
| Coordinate cleaning correct | `test_clean_coordinates_drops_out_of_bounds` | rows outside lat 43.4–43.9 / lon −79.7–−79.0 dropped and counted | — |
| ETL run report written | file existence check on `reports/etl_runs/<YYYYMMDD_HHMMSS>.md` | 1 new file per run, containing per-stage counts, drop reasons, coverage % | — |
| ETL test suite green | `uv run pytest tests/etl -q` exit code | `0`, 0 failures | — |
| Invalid-record policy documented | inspect `docs/17_etl/00_etl_ingestor.md` addendum | drop-vs-flag policy stated for dates, coordinates, and neighborhood joins | — |

---

## Phase 4 — Baseline Modeling and Scoring

| Criterion | Measurement Method | Pass Threshold | Date Met |
|---|---|---|---|
| **Baseline model trains without error** | exit code of `train_model.py` | `0` | — |
| Modeling runner exits cleanly | exit code of `uv run python -m toronto_pipeline_failure_predict.models.run_modeling --mode train+score` | `0` on real MVP data | — |
| Scoring completeness | `SELECT COUNT(*)`, `COUNT(DISTINCT (year, month, neighborhood))` on `pipe_break_risk_scores` | exactly one row per `(year, month, neighborhood)` in the scoring horizon; no duplicates | — |
| Model metadata recorded | `SELECT model_version, COUNT(*) FROM model_metadata GROUP BY model_version` | exactly 1 row per trained `model_version` | — |
| No temporal leakage | `test_time_aware_split_no_future_leakage` | `max(train date) < min(test date)`; split is date-cutoff based, not shuffled | — |
| Reproducible training | train twice with `settings.RANDOM_SEED` fixed, compare predictions | identical outputs (bitwise or within float tolerance) | — |
| Risk score bounds | `test_normalize_risk_score_bounds_0_to_1` | all scores in `[0, 1]`, no NaN/inf | — |
| Risk class assignment | `test_assign_risk_class_thresholds` | every score maps to exactly one of `low`/`medium`/`high` per `RISK_CLASS_THRESHOLDS` | — |
| Feature key integrity | `test_assemble_feature_table_has_no_nulls_in_keys` | 0 nulls in `(year, month, neighborhood, feature_version)` | — |
| Model artifact persisted | file existence check on `models/<model_version>.joblib` | present, non-zero size, loadable via `joblib.load` | — |
| Evaluation metrics published | file existence + content check on `reports/model_evaluation/<model_version>.md` | present, all metric fields populated (no `TBD`) | — |
| Missing-data guardrail | run `run_modeling.py` against an empty feature table | exits `1` with a message pointing to Phase 3 / 4.1 | — |
| Modeling test suite green | `uv run pytest tests/models -q` exit code | `0`, 0 failures | — |

---

## Phase 5 — MVP Delivery: Analytics Consumption

| Criterion | Measurement Method | Pass Threshold | Date Met |
|---|---|---|---|
| **Report artifact renders** | manual open of output file | no errors, all sections populated | — |
| Report content complete | visual inspection against checklist 5.2 minimum content | all 3 elements present: ranked top-N table, monthly trend chart, driver panel | — |
| Report data non-empty | inspect the extract behind the artifact | `> 0` rows for the latest scored month; values plausible (scores in `[0,1]`, known neighborhood names) | — |
| Reporting view queryable | `get_reporting_extract(conn)` against `joined_risk_view` | returns a non-empty DataFrame; exit code `0` | — |
| Export completeness check | `assert_no_nulls(df, ["year","month","neighborhood","risk_score","risk_class"])` | passes — 0 nulls in required columns | — |
| Runbook executable | execute the full command sequence in `docs/10_operations/01_mvp_runbook.md` from a clean clone | every step exits `0`; expected artifact exists after each step | — |
| Independent reproduction | runbook executed by someone other than the original author, or from a fresh clone | completes with no undocumented manual intervention (or "not feasible" recorded with reason) | — |
| Run evidence recorded | inspect `docs/04_reports/01_summary_reports/2026_mvp_final_run_summary.md` | actual row counts, timings, and any manual interventions recorded | — |
| Lineage documented | inspect `docs/10_operations/02_mvp_data_lineage.md` | every curated/feature/prediction table mapped to its upstream raw source file(s) | — |
| Limitations disclosed | inspect `docs/04_reports/01_summary_reports/2026_mvp_release_notes.md` | shipped / not-shipped / caveats all stated; all MVP assumptions listed | — |
| All prior gates closed | inspect Phase 0–5 exit gate checkboxes in `01_mvp_checklists.md` | 100% checked | — |
| Release tagged | `git tag --list` + `git rev-parse <tag>` | MVP tag (e.g. `v0.2.0`) exists and points to the validated commit | — |

---

## Cross-Phase Standing Criteria

These apply at **every** phase gate, in addition to the tables above. Because they are re-checked at every gate, `Date Met` here records the **most recent** passing observation, not the first.

| Criterion | Measurement Method | Pass Threshold | Date Met |
|---|---|---|---|
| Quality baseline green | `uv run pytest -q` and `uv run ruff check .` | both exit `0` before any Exit Gate is checked off | — (failing: `ruff` passes 2026-08-28, `pytest` does not) |
| Test coverage per module | each new `.py` module from `01_mvp_checklists.md` has a matching test file/function | 1:1 — no module marked complete without a test | — |
| Runner-level test coverage | each CLI/runner script has an invocation-level (not just unit) test | ≥ 1 per runner | — |
| No silent scope creep | any work not traceable to a checklist sub-bullet | 0 — new scope requires a checklist sub-bullet added *before* work starts | — |
| Schema change discipline | any schema change ships with migration + checklist update + test updates | all 3 in the same change set | — |
| CLI change discipline | any CLI flag/behavior change ships with a runbook update | same change set | — |

---

## Acceptance Progress Summary

Update alongside the `Date Met` cells so this stays a truthful roll-up.

| Phase | Criteria Met | Total | Date Phase Accepted |
|---|---|---|---|
| 0 — Foundation and Alignment | 2 | 11 | — |
| 1 — Data Acquisition and Contracts | 0 | 10 | — |
| 2 — Analytical Storage (SQLite) | 0 | 9 | — |
| 3 — Core ETL and Curated Dataset Build | 0 | 11 | — |
| 4 — Baseline Modeling and Scoring | 0 | 13 | — |
| 5 — MVP Delivery: Analytics Consumption | 0 | 12 | — |
| Cross-Phase Standing Criteria | 0 | 6 | n/a (re-checked every gate) |
