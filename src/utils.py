import logging

def config_logging(experiment_name):
    logging.basicConfig(level=logging.INFO, filename=f"log/{experiment_name}.log", filemode="a")

def get_logger(name=None):
    """ Creates a module-level logger """
    logger_name = '' if name is None else str(name)
    logger = logging.getLogger(f"[lime-rs]: {logger_name}")
    logger.setLevel(logging.INFO)

    return logger
