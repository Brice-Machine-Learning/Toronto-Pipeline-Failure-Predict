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

from typing import Any, Dict, Optional, List
import requests


# Ignore me
class TorontoOpenDataClient:
    """
    Client for interacting with the City of Toronto Open Data CKAN API.

    CKAN concepts:
    - Package: a dataset (e.g. "water-main-breaks")
    - Resource: a downloadable file within a dataset (CSV, GeoJSON, etc.)
    """

    CKAN_BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action"

    def __init__(self, timeout: int = 15) -> None:
        """
        Parameters
        ----------
        timeout : int
            Request timeout in seconds. Applied to all API calls.
        """
        self.timeout = timeout

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Execute a GET request against a CKAN action endpoint.

        This method centralizes error handling and ensures consistent
        response parsing across all client operations.
        """
        url = f"{self.CKAN_BASE_URL}/{endpoint}"

        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            payload = response.json()
        except requests.exceptions.RequestException as exc:
            print(f"❌ CKAN request failed: {exc}")
            return None

        if not payload.get("success", False):
            print(f"❌ CKAN API returned success=false for endpoint={endpoint}")
            return None

        return payload

    # ------------------------------------------------------------------
    # Dataset discovery
    # ------------------------------------------------------------------

    def search_datasets(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Search datasets by keyword.

        Parameters
        ----------
        query : str
            Free-text search term (e.g. "water main").

        Returns
        -------
        dict or None
            CKAN search results payload.
        """
        return self._get(
            endpoint="package_search",
            params={"q": query},
        )

    def get_dataset_metadata(self, dataset_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve full metadata for a CKAN dataset (package).

        Parameters
        ----------
        dataset_id : str
            CKAN package ID (URL slug), not the title.
            Example: "water-main-breaks"
        """
        return self._get(
            endpoint="package_show",
            params={"id": dataset_id},
        )

    # ------------------------------------------------------------------
    # Domain-specific helpers
    # ------------------------------------------------------------------

    def get_water_main_breaks_metadata(self) -> Optional[Dict[str, Any]]:
        """
        Retrieve metadata for the Water Main Breaks dataset.

        This method exists to anchor domain intent in code and avoid
        scattering dataset IDs across the codebase.
        """
        return self.get_dataset_metadata("water-main-breaks")

    def list_resources(self, metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract the resource list from a dataset metadata payload.

        Returns an empty list if metadata is malformed or incomplete.
        """
        try:
            return metadata["result"]["resources"]
        except (TypeError, KeyError):
            return []

    def find_resource_by_format(
        self,
        metadata: Dict[str, Any],
        format_preference: str,
        datastore_only: bool = False,
    ) -> Optional[Dict[str, Any]]:
        """
        Locate a dataset resource matching a desired format.

        Parameters
        ----------
        format_preference : str
            Desired resource format (e.g. "CSV", "GEOJSON").
        datastore_only : bool
            If True, only return resources backed by CKAN's datastore.

        Returns
        -------
        dict or None
            Matching resource metadata.
        """
        format_preference = format_preference.upper()

        for resource in self.list_resources(metadata):
            if resource.get("format", "").upper() != format_preference:
                continue

            if datastore_only and not resource.get("datastore_active", False):
                continue

            return resource

        return None

    def get_resource_download_url(
        self,
        metadata: Dict[str, Any],
        format_preference: str = "CSV",
    ) -> Optional[str]:
        """
        Retrieve the direct download URL for a dataset resource.

        This URL should be passed to ingestion logic, not fetched here.
        """
        resource = self.find_resource_by_format(
            metadata=metadata,
            format_preference=format_preference,
        )

        if not resource:
            print(f"⚠️ No resource found with format={format_preference}")
            return None

        return resource.get("url")
