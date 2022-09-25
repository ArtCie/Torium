from functools import wraps
import inspect
import logging
from logging.handlers import RotatingFileHandler
from application import application

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('/var/log/application.log', maxBytes=1024, backupCount=5)
handler.setFormatter(formatter)
application.logger.addHandler(handler)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        class_name = type(args[0]).__name__
        function_name = func.__name__
        method_attributes = inspect.getfullargspec(func)[0]
        message = construct_logger(class_name, function_name, method_attributes, args)
        logger.info(message)
        result = func(args[0], args[1], **kwargs)
        return result
    return wrapper


def construct_logger(class_name, function_name, method_attributes, args):
    base = f"{class_name}.{function_name}(): "
    if args:
        return base + ' '.join([f"{method_attributes[i]}: {args[i]}," for i in range(1, len(method_attributes))])
    return base


def log_exception(class_name: str, error: str):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.exception(f"{class_name}: {error}")
