from functools import wraps
from flask import request


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from application import logger
        class_name = type(args[0]).__name__
        function_name = func.__name__
        message = construct_logger(class_name, function_name, kwargs)
        logger.info(message)
        result = func(args[0], args[1], **kwargs)
        return result
    return wrapper


def construct_logger(class_name, function_name, kwargs):
    headers = {header_key[4:].replace('-', '_').lower(): header_value for (header_key, header_value)
               in request.headers.items()
               if header_key.lower().startswith('trm')}
    return f"{class_name}.{function_name}(): kwargs: {kwargs}, headers: {headers}"


def log_exception(class_name: str, error: str):
    from application import logger
    logger.exception(f"{class_name}: {error}")
