import os
import random
import logging
from logging import Logger
import numpy as np

from ml_project.entities import LoggerParams


def build_logger(
    name: str, params: LoggerParams
) -> Logger:
    """
    Creater logger.
    """
    path_dir = os.path.dirname(params.path)
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    logger = logging.getLogger(name)
    logger.setLevel(params.level)

    simple_formatter = logging.Formatter(fmt=params.format,
                                         datefmt=params.date_format)

    file_handler = logging.FileHandler(filename=params.path, mode=params.mode)
    file_handler.setLevel(params.level)
    file_handler.setFormatter(simple_formatter)
    logger.addHandler(file_handler)

    if params.stdout:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(params.level)
        console_handler.setFormatter(simple_formatter)
        logger.addHandler(console_handler)

    return logger


def get_logger(
    name: str, params: LoggerParams = None
)-> Logger:
    """
    Getting logger.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        return build_logger(name, params)
    return logger