import os,sys
import urllib.request as request
import zipfile
from src.summarizer.logging import logger
from src.summarizer.exception import CustomException
from src.summarizer.config.configuration import ConfigurationManager
from src.summarizer.entity import DataIngestionConfig
from src.summarizer.components.data_validation import DataValidation


class DatavalidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation =  DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
    