import os

from pydantic import BaseModel

MARVEL_PUBLIC_KEY = os.getenv("MARVEL_PUBLIC_KEY", "")
MARVEL_PRIVATE_KEY = os.getenv("MARVEL_PRIVATE_KEY", "")


class LogConfig(BaseModel):
    LOGGER_NAME: str = "ec_mscomics"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }
