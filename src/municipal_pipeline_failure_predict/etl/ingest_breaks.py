# src/etl/ingest_breaks.py
"""Ingest water main breaks data from LA open data API."""

from municipal_pipeline_failure_predict.api.municipal_client import TorontoOpenDataClient as MunicipalApiClient
import pandas as pd


def download_water_breaks():
    client = MunicipalApiClient()
    metadata = client.get_water_main_breaks_metadata()
    url = client.extract_resource_url(metadata, format_preference="CSV")

    if url:
        df = pd.read_csv(url)
        print(df.head())
        return df
    else:
        print("No data returned.")
        return None

