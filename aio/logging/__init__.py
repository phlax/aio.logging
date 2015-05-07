__version__ = "0.0.1"

import asyncio

import logging.config


@asyncio.coroutine
def start_logging():
    logging.config.fileConfig('logging.conf')
