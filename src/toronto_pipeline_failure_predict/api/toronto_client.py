# src/api/toronto_client.py
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

import requests


BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action"


class TorontoOpenDataClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def search_datasets(self, query: str, rows: int = 10):
        """Search datasets"""
        url = f"{self.base_url}/package_search"
        params = {"q": query, "rows": rows}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_dataset(self, package_id: str):
        """Get dataset metadata"""
        url = f"{self.base_url}/package_show"
        params = {"id": package_id}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_resource_urls(self, dataset_json):
        """Extract usable resource URLs"""
        resources = dataset_json["result"]["resources"]
        return [r["url"] for r in resources if r["format"].lower() in ("csv", "geojson")]
