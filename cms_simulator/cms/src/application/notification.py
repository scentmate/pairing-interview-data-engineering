import requests

from cms.src.infrastructure.logging import logger


def notify(delta, host=None):
    logger.debug("Notifiying")
    
    if host is not None:
        logger.info(f"Notifiying to {host}:\n{delta}")
        try:
            r = requests.post(host, json=delta)
        except Exception as e:
            logger.error("Host is not reacheable!")
    
    logger.warning(f"Data change: {delta}")