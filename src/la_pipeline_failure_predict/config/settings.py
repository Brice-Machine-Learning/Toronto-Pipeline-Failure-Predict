# src/config/settings.py
"""
Settings configuration for the LA pipeline failure prediction project.
"""

from pydantic import BaseSettings
from pathlib import Path
class Settings(BaseSettings):
    # Project metadata
    PROJECT_NAME: str = "LA Pipeline Failure Prediction"
    VERSION: str = "1.0.0"

    # Data paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"
    MODELS_DIR: Path = BASE_DIR / "models"
    LOGS_DIR: Path = BASE_DIR / "logs"

    # Model parameters
    RANDOM_SEED: int = 42
    TEST_SIZE: float = 0.2

    # API settings
    LA_API_URL: str = "https://api.la-data-collection.com"
    API_TIMEOUT: int = 10  # seconds

    class Config:
        env_file = ".env"

settings = Settings()
