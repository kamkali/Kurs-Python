import logging
import functools
import time

"""Logger module created by Kamil Kaliś"""


def logger_setup():
    """Sets up the logger.
    Usage:
        1. With wrapper @log_exec_time
        2. Set logger within module as:
            2.1 log = logging.getLogger('exec_time.log')
            2.2 use 'log' variable to use logger and write them to file"""

    logformat = "[%(asctime)s %(levelname)s] %(message)s"
    dateformat = "%d-%m-%y %H:%M:%S"
    logger = logging.getLogger("exec_time.log")
    formatter = logging.Formatter(logformat)
    formatter.datefmt = dateformat
    fh = logging.FileHandler("exec_time.log", mode="a")
    fh.setFormatter(formatter)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.propagate = False


def log_exec_time(func):
    """Wrapper for logging execution time of marked function.
    Usage:
    Add adnotation above function: '@log_exec_time'"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Make singleton logger
        logger_setup()
        log = get_logger()
        log.info(f"Running {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        exec_time = time.time() - start_time
        log.info(f"Function {func.__name__} finished in {exec_time}s")
        return result

    return wrapper


def get_logger(logger_name='exec_time.log'):
    return logging.getLogger(logger_name)
