from functools import wraps


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
    return f"{class_name}.{function_name}(): {kwargs}"


def log_exception(class_name: str, error: str):
    from application import logger
    logger.exception(f"{class_name}: {error}")
