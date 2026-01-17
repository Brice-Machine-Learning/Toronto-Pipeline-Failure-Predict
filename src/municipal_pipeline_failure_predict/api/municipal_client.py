# src/api/municipal_client.py
"""
API client for interacting with the City of Toronto Open Data services.

Toronto data is primarily served via:
- CKAN API (metadata + resource discovery)
- Direct dataset URLs (CSV / GeoJSON downloads)

This client supports:
- CKAN package discovery
- Direct dataset retrieval
"""

import requests
from typing import Dict, Any, Optional
from municipal_pipeline_failure_predict.config import settings


class TorontoOpenDataClient:
    """
    Lightweight client for City of Toronto Open Data.

    Handles:
    - CKAN metadata queries
    - Dataset resource lookup
    - JSON / CSV endpoint access
    """

    CKAN_BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action"

    def __init__(self, timeout: int = 15):
        self.timeout = timeout

    # ------------------------------------------------------------------
    # Core CKAN helpers
    # ------------------------------------------------------------------

    def _get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Generic GET wrapper with basic error handling."""
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP error: {e} — URL: {url}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
        except ValueError:
            print("❌ Failed to parse JSON response")
        return None

    # ------------------------------------------------------------------
    # CKAN dataset discovery
    # ------------------------------------------------------------------

    def list_datasets(self, query: Optional[str] = None) -> Any:
        """
        Search Toronto Open Data datasets.

        Example:
            client.list_datasets(query="water main")
        """
        url = f"{self.CKAN_BASE_URL}/package_search"
        params = {"q": query} if query else {}
        return self._get(url, params=params)

    def get_dataset_metadata(self, dataset_id: str) -> Any:
        """
        Fetch dataset metadata by CKAN package ID.

        Example dataset_id:
            "water-main-breaks"
        """
        url = f"{self.CKAN_BASE_URL}/package_show"
        params = {"id": dataset_id}
        return self._get(url, params=params)

    # ------------------------------------------------------------------
    # Domain-specific helpers
    # ------------------------------------------------------------------

    def get_water_main_breaks_metadata(self) -> Any:
        """
        Retrieve metadata for the Water Main Breaks dataset.

        This returns resource URLs (CSV, GeoJSON, etc.)
        that should be used for ingestion.
        """
        dataset_id = "water-main-breaks"
        return self.get_dataset_metadata(dataset_id)

    def extract_resource_url(
        self,
        metadata: Dict[str, Any],
        format_preference: str = "CSV"
    ) -> Optional[str]:
        """
        Extract a resource download URL from dataset metadata.

        Example formats:
            CSV, GEOJSON, SHP
        """
        if not metadata or not metadata.get("result"):
            return None

        resources = metadata["result"].get("resources", [])
        for r in resources:
            if r.get("format", "").upper() == format_preference.upper():
                return r.get("url")

        print(f"⚠️ No resource found with format={format_preference}")
        return None
