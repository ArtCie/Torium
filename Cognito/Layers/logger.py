from functools import wraps
import inspect
import logging


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        class_name = type(args[0]).__name__
        function_name = func.__name__
        method_attributes = inspect.getfullargspec(func)[0]
        message = construct_logger(class_name, function_name, method_attributes, args)
        logger.info(message)
        result = func(*args, **kwargs)
        return result
    return wrapper


def construct_logger(class_name, function_name, method_attributes, args):
    return f"{class_name}.{function_name}(): " + ' '.join(
        [f"{method_attributes[i]}: {args[i]}," for i in range(1, len(args))])[:-1]
