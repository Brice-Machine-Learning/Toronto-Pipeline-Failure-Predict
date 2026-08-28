# Database Direction Update: Turso → SQLite

The project database direction is now **SQLite**.

Based on the current repository state, there is **no implemented Turso setup yet** (no Turso connection code, migrations, or runtime wiring in `src/`), so this is a planning/documentation alignment change rather than a migration of working code.

## Current Database Progress (as of this update)

1. Database architecture and planning docs exist and are detailed.
2. A proposed Turso-oriented schema document exists in `docs/06_database/00_turso_database_tables.md`.
3. Backend parity/switching procedures are documented (`01_duckdb_turso_parity_checklist.md`, `02_db_switch_procedure.md`) but remain procedural guidance, not implemented code.
4. The implementation checklist still shows database implementation tasks as pending (connection layer, migrations, query directory, integration tests, and Turso instance creation).
5. No committed code currently establishes Turso credentials, opens Turso/libSQL connections, or executes Turso-specific migrations.

## Decision

Use **SQLite** as the project database going forward.

For local analytical iteration, DuckDB may still be used where appropriate, but the relational datastore target for implementation and documentation should now be SQLite (not Turso).

## Documentation Follow-Through Required

Update docs that still reference Turso as the deployment database so they consistently state SQLite as the selected datastore.