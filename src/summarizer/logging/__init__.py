import os
import logging
from datetime import datetime

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

class Logger:
    def __init__(self):
        

        log_filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_info.log"
        log_filepath = os.path.join(log_dir, log_filename)

        logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
        logging.basicConfig(
            level=logging.INFO,
            format=logging_str,
            handlers=[
                logging.FileHandler(log_filepath),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger("textSummarizerLogger")

    def info(self, message):
        self.logger.info(message)

# Initialize the logger
logger = Logger()

