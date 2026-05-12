from loguru import logger
import sys
from pathlib import Path


# Create logs directory if it does not exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


# Remove default logger
logger.remove()


# Console logging
logger.add(
    sys.stdout,
    level="INFO",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level} | "
        "{message}"
    ),
)


# File logging
logger.add(
    "logs/policyassist.log",
    level="INFO",
    rotation="1 MB",
    retention="7 days",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level} | "
        "{message}"
    ),
)


def get_logger():
    """
    Returns configured application logger.
    """

    return logger