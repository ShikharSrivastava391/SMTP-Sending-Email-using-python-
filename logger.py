import logging
import os
from datetime import date


class CustomLogger:
    @staticmethod
    def get_logger(name="", level=logging.INFO):
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        today = date.today()
        if name != "":
            name = "{:<25}".format(name)
        logging.basicConfig(
            filename=f'./logs/log_{today.strftime("%Y-%m-%d")}.log',
            format="%(asctime)s: %(levelname)s: %(name)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
        )
        logger = logging.getLogger(str(name))
        logger.setLevel(level)
        return logger
