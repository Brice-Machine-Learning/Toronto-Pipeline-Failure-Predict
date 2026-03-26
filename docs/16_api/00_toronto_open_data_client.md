# Toronto Open Data API Client

## Purpose

This document describes the `TorontoOpenDataClient`, a lightweight Python client used to interact with the **City of Toronto Open Data portal**, which is backed by a **CKAN** instance.

The client provides a stable, explicit interface for:

- discovering datasets
- retrieving dataset metadata
- locating downloadable resource URLs (CSV, GeoJSON, etc.)

The client is intentionally **read-only** and **non-opinionated**.
It does **not** download data, transform data, or persist results. Those responsibilities belong to ETL pipelines.

---

## Background: Toronto Open Data & CKAN

Toronto’s Open Data portal exposes datasets via **CKAN**, an open-source data catalog platform commonly used by governments.

Key CKAN concepts used by this client:

| CKAN Term | Meaning |
| --------- | -------- |
| Package | A dataset (e.g. `water-main-breaks`) |
| Resource | A downloadable file within a dataset |
| Datastore | Optional CKAN-backed tabular store |

Most datasets provide direct download URLs for CSV, GeoJSON, or Shapefile resources.
The CKAN API is used primarily for **metadata discovery**, not bulk data transfer.

---

## Design Principles

The client follows several explicit design constraints:

- **Thin client**
  No business logic, transformations, or persistence.

- **Explicit over clever**
  Dataset IDs and formats are provided intentionally, not inferred.

- **Fail safely**
  Network and API failures return `None` rather than raising unhandled exceptions.

- **Domain-aware, not generic**
  Toronto-specific behavior is allowed where it improves clarity.

The goal is correctness, predictability, and long-term maintainability.

---

## Client Location

```bash
src/api/toronto_client.py
```

---

## Class Overview

```python
class TorontoOpenDataClient:
```

The class exposes a small, focused set of public methods grouped into:

- CKAN request handling
- dataset discovery
- dataset metadata access
- resource selection

---

## Configuration

### CKAN Base URL

```python
CKAN_BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action"
```

All requests are made against CKAN **action endpoints** (e.g. `package_show`, `package_search`).

### Timeout

```python
TorontoOpenDataClient(timeout=15)
```

The timeout applies to all HTTP requests to avoid blocking ETL pipelines.

---

## Internal Request Handling

### `_get()`

```python
def _get(self, endpoint: str, params: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]
```

Responsibilities:

- construct full CKAN action URLs
- execute HTTP GET requests
- handle network and API-level failures
- validate CKAN `success` responses
- return parsed JSON payloads

This method centralizes error handling so public methods remain minimal and predictable.

---

## Dataset Discovery

### `search_datasets()`

```python
def search_datasets(self, query: str) -> Optional[Dict[str, Any]]
```

Searches CKAN packages using free-text keywords.

Typical use cases:

- exploratory dataset discovery
- confirming dataset IDs
- validating naming conventions

---

### `get_dataset_metadata()`

```python
def get_dataset_metadata(self, dataset_id: str) -> Optional[Dict[str, Any]]
```

Retrieves full metadata for a specific CKAN dataset (package).

Returned metadata includes:

- dataset description
- update timestamps
- resource listings
- format availability
- datastore status

This metadata is the primary input for resource selection.

---

## Domain-Specific Dataset Access

### `get_water_main_breaks_metadata()`

```python
def get_water_main_breaks_metadata(self) -> Optional[Dict[str, Any]]
```

Convenience method that anchors the **Water Main Breaks** dataset ID in a single location.

This avoids:

- hardcoding dataset IDs across pipelines
- accidental drift between environments
- silent mismatches caused by typos

---

## Resource Handling

### `list_resources()`

```python
def list_resources(self, metadata: Dict[str, Any]) -> List[Dict[str, Any]]
```

Extracts the `resources` array from CKAN dataset metadata.

Returns an empty list if metadata is malformed or incomplete.
This avoids defensive checks throughout ingestion code.

---

### `find_resource_by_format()`

```python
def find_resource_by_format(
    self,
    metadata: Dict[str, Any],
    format_preference: str,
    datastore_only: bool = False
) -> Optional[Dict[str, Any]]
```

Selects a dataset resource based on:

- desired file format (CSV, GEOJSON, SHP, etc.)
- optional datastore backing

This allows ingestion pipelines to:

- explicitly request a preferred format
- avoid guessing which resource is correct
- enforce consistent inputs across environments

---

### `get_resource_download_url()`

```python
def get_resource_download_url(
    self,
    metadata: Dict[str, Any],
    format_preference: str = "CSV"
) -> Optional[str]
```

Returns the **direct download URL** for a selected resource.

Important notes:

- The client does **not** download the file
- The URL is passed downstream to ETL logic
- Resource selection remains deterministic

---

## Typical Usage Pattern

```python
client = TorontoOpenDataClient()

metadata = client.get_water_main_breaks_metadata()

csv_url = client.get_resource_download_url(
    metadata,
    format_preference="CSV"
)
```

At this point, `csv_url` is handed to:

- ETL ingestion pipelines
- file download utilities
- batch jobs or schedulers

---

## What This Client Intentionally Does NOT Do

- ❌ Download files
- ❌ Parse CSV or GeoJSON
- ❌ Store data in databases
- ❌ Perform validation or cleaning
- ❌ Contain ML or analytics logic

Those responsibilities belong to ETL, data processing, and modeling layers.

---

## Rationale

This client exists to solve a narrow problem cleanly:

> “Given a known Toronto Open Data dataset, reliably locate the correct resource URL.”

Maintaining this strict boundary prevents:

- tight coupling between API logic and pipelines
- brittle ingestion code
- untestable monolithic workflows
