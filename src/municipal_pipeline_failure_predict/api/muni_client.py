# src/api/la_client.py
""" 
API client for interacting with the LA data collection service.
"""

import requests
from typing import Dict, Any, Optional
from municipal_pipeline_failure_predict.config import settings

class MunicipalApiClient:
    """
    Lightweight client for LA open data endpoints.
    Handles auth token, request retries, and JSON parsing.
    """

    BASE_URL = "https://data.lacity.org/resource"

    def __init__(self, token: Optional[str] = None):
        self.token = token
        self.headers = {
            "X-App-Token": self.token
        }

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """
        Generic GET wrapper.
        Example: client.get('/xxxx-xxxx', {'$limit': 500})
        """
        url = f"{self.BASE_URL}/{endpoint}"

        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP error: {e} — URL: {url}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None

        try:
            return response.json()
        except ValueError:
            print("❌ Failed to parse JSON")
            return None

    def get_water_main_breaks(self, limit: int = 50000) -> Any:
        """
        Fetch the water main break dataset.

        Dataset identifier (example):
        https://data.lacity.org/resource/xxxx-xxxx.json
        Replace 'xxxx-xxxx' with the actual dataset ID.
        """
        endpoint = "t6jv-5njd.json"  # <--- update this with the real ID
        params = {"$limit": limit}
        return self.get(endpoint, params=params)