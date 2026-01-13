# src/etl/ingest_breaks.py
"""Ingest water main breaks data from LA open data API."""

from municipal_pipeline_failure_predict.api.muni_client import MunicipalApiClient
import pandas as pd


def download_water_breaks():
    client = MunicipalApiClient()
    data = client.get_water_main_breaks()

    if data:
        df = pd.DataFrame(data)
        print(df.head())
        return df
    else:
        print("No data returned.")
        return None

