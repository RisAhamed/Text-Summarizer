from src.summarizer.logging import logger
import sys
import traceback

class CustomException(Exception):
    def __init__(self, error, sys):
        self.error = error
        self.file_name = sys.exc_info()[2].tb_frame.f_code.co_filename
        self.line_number = sys.exc_info()[2].tb_lineno
        self.error_message = str(self.error)

        logger.info(f"Error: {self.error_message} | File: {self.file_name} | Line: {self.line_number}")
        logger.info(traceback.format_exc())

    def __str__(self):
        return f"Error: {self.error_message} | File: {self.file_name} | Line: {self.line_number}"



