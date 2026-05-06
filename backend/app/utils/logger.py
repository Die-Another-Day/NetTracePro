import os
import logging
from logging.handlers import RotatingFileHandler
from app.utils.config import settings

logger = logging.getLogger("sentinelsight")


def configure_logging() -> None:
    logger.setLevel(settings.LOG_LEVEL.upper())

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    os.makedirs("logs", exist_ok=True)

    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=5_000_000,
        backupCount=5
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
