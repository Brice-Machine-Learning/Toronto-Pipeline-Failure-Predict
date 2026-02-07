# src/etl/ingest_breaks.py
"""
ETL ingestion for water main breaks data.

This module orchestrates retrieval of the Water Main Breaks dataset
from Toronto Open Data and returns a raw DataFrame for downstream use.
"""

from municipal_pipeline_failure_predict.api.municipal_client import (
    TorontoOpenDataClient,
)
import pandas as pd
from typing import Optional


def ingest_water_main_breaks() -> Optional[pd.DataFrame]:
    """
    Retrieve the Water Main Breaks dataset as a pandas DataFrame.

    Returns
    -------
    pd.DataFrame or None
        Raw dataset if retrieval succeeds, otherwise None.
    """
    client = TorontoOpenDataClient()

    metadata = client.get_water_main_breaks_metadata()
    if not metadata:
        return None

    resource_url = client.get_resource_download_url(
        metadata,
        format_preference="CSV",
    )

    if not resource_url:
        return None

    # NOTE:
    # pandas handles the CSV parsing, but download behavior
    # should be moved to a dedicated downloader in future iterations.
    try:
        df = pd.read_csv(resource_url)
    except Exception as exc:
        print(f"❌ Failed to load CSV from {resource_url}: {exc}")
        return None

    return df
