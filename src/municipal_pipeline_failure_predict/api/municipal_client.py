# src/api/municipal_client.py
"""
Toronto Open Data API client.

This client provides a thin, explicit interface over Toronto's CKAN-based
Open Data portal. It is intentionally minimal and focused on:

- Dataset discovery via CKAN
- Dataset metadata retrieval
- Resource URL extraction for downstream ingestion

It does not perform data downloading or transformation. Those concerns
belong in ingestion pipelines, not the API client layer.
"""

