import logging

def get_logger(name=None):
    """ Creates a module-level logger """
    logger_name = '' if name is None else str(name)
    logging.basicConfig(level=logging.INFO, filename=f"log/{logger_name}.log", filemode="a")
    logger = logging.getLogger(f"[lime-rs]: {logger_name}")
    logger.setLevel(logging.INFO)

    return logger