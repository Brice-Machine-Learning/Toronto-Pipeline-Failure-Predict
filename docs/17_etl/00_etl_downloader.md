# ETL Downloader: Toronto Open Data

## Purpose

This document describes the **ETL downloader layer** responsible for retrieving raw datasets from the City of Toronto Open Data portal and persisting them to disk for downstream processing.

The downloader sits **between API discovery and data processing**:

- API client → discovers datasets and resource URLs
- ETL downloader → retrieves and stores raw files
- Processing / features → cleans, validates, and transforms data

This separation enforces clear ownership boundaries and improves reliability, testability, and maintainability.

---

## Role in the Pipeline

```text
TorontoOpenDataClient (api/)
        ↓
ETL Downloader (etl/)
        ↓
data/raw/
        ↓
Processing / Feature Engineering
```

The downloader is responsible only for **retrieval and persistence**, not interpretation.

---

## Design Principles

The downloader follows these constraints:

- **Single responsibility**  
  Download files and write them to disk.

- **Idempotent behavior**  
  Re-running the downloader should not corrupt or duplicate data.

- **Explicit I/O**  
  File paths, filenames, and formats are deterministic.

- **Streaming downloads**  
  Large datasets are streamed to avoid memory pressure.

- **Failure visibility**  
  Errors are logged and surfaced clearly.

---

## Location

```text
src/toronto_pipeline_failure_predict/etl/
```

Recommended initial structure:

```text
etl/
├── __init__.py
├── download_resources.py
└── ingest_water_main_breaks.py
```

---

## Downloader Responsibilities

The ETL downloader layer is responsible for:

- accepting a resource download URL
- issuing HTTP GET requests
- streaming file contents to disk
- applying consistent file naming
- overwriting or skipping existing files (explicitly)
- logging download outcomes

It is **not** responsible for:

- schema validation
- parsing CSV or GeoJSON
- database ingestion
- analytics or ML logic

---

## Core Utility: `download_file()`

A reusable download helper should live in a shared location (e.g. `utils/`).

### Function Contract

```python
def download_file(
    url: str,
    destination: Path,
    chunk_size: int = 1024 * 1024,
) -> None:
    ...
```

### Behavior

- streams the response body in chunks
- writes to a temporary file
- atomically renames on success
- raises or logs on failure

This ensures partial downloads never appear as valid files.

---

## Domain-Specific ETL Script

### `ingest_water_main_breaks.py`

This script orchestrates dataset retrieval for the **Water Main Breaks** dataset.

High-level flow:

1. instantiate `TorontoOpenDataClient`
2. retrieve dataset metadata
3. select preferred resource format
4. pass resource URL to downloader
5. persist file to `data/raw/`

---

## Example Flow (Pseudocode)

```python
client = TorontoOpenDataClient()

metadata = client.get_water_main_breaks_metadata()

resource_url = client.get_resource_download_url(
    metadata,
    format_preference="CSV"
)

destination = Path("data/raw/water_main_breaks.csv")

download_file(resource_url, destination)
```

The ETL script owns orchestration; utilities handle mechanics.

---

## File Naming & Storage Conventions

Recommended conventions:

```text
data/raw/
├── water_main_breaks/
│   ├── water_main_breaks_latest.csv
│   ├── water_main_breaks_2024-01-15.csv
│   └── README.md
```

This supports:

- reproducibility
- historical backfills
- auditability
- rollback capability

---

## Error Handling Strategy

Downloader failures should:

- fail fast
- log HTTP status and URL
- avoid creating partial files
- return non-zero exit codes in batch runs

Silent failures are explicitly avoided.

---

## Why This Layer Exists

Separating downloading from discovery and processing:

- prevents API logic from handling side effects
- enables retry logic without re-querying CKAN
- simplifies testing and mocking
- mirrors production ETL architecture

This structure reflects how data pipelines are implemented in professional analytics environments.

---

## Summary

The ETL downloader layer:

- consumes resource URLs from the API client
- reliably retrieves raw datasets
- persists files deterministically
- enforces clean architectural boundaries

It is intentionally simple, explicit, and boring.

That is exactly what you want between the internet and your data.
