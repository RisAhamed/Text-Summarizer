import os
import urllib.request as request
import zipfile
from src.summarizer.logging import logger
from src.summarizer.exception import CustomException
from src.summarizer.config.configuration import ConfigurationManager
from src.summarizer.entity import DataIngestionConfig
from src.summarizer.components.data_ingestion  import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    
