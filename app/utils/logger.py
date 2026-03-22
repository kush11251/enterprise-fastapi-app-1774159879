import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s %(message)s")
logger = logging.getLogger("enterprise")

def trace(message: str):
    logger.info(f"TRACE: {message}")