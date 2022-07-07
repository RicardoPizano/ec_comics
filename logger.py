import logging
from logging.config import dictConfig

from constans import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("ec_mscomics")


def inf(file: str, section: str, message: str):
    logger.info(f"{file} | {section} | {message}")


def war(file: str, section: str, message: str):
    logger.warning(f"{file} | {section} | {message}")


def err(file: str, section: str, message: str):
    logger.error(f"{file} | {section} | {message}")
