# src/log/logger.py
"""
Logging configuration for the LA pipeline failure prediction project."""

import logging
from src.config import settings
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
