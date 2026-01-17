# src/log/logger.py
"""
Logging configuration for the Toronto pipeline failure prediction project."""

import logging
from municipal_pipeline_failure_predict.config.settings import settings
import os

# Ensure the logs directory exists
os.makedirs(settings.LOGS_DIR, exist_ok=True)
log_file_path = settings.LOGS_DIR / "app.log"
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(settings.PROJECT_NAME)
