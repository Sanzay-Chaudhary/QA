import logging

def get_logger():

    logging.basicConfig(
        filename="automation.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )

    return logging.getLogger()