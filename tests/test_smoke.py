"""
Smoke tests for toronto_pipeline_failure_predict.

These tests verify that the package installs correctly and that
core modules can be imported without triggering runtime errors.
"""


def test_package_import():
    import municipal_pipeline_failure_predict  # noqa: F401


def test_api_client_import():
    from municipal_pipeline_failure_predict.api.municipal_client import (
        TorontoOpenDataClient,
    )

    client = TorontoOpenDataClient()
    assert client is not None
