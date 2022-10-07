import logging
from json import dumps


def log_exception(class_name: str, error: str):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.exception(f"{class_name}: {error}")


def build_response(message: str, response_code: int) -> dict:
    return {
        'statusCode': response_code,
        'body': dumps(message)
    }
