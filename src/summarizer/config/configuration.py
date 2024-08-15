from src.summarizer.logging import logging
from src.summarizer.exception import CustomException
from dataclasses import dataclass
from pathlib import Path
from src.summarizer.constants import  *
from src.summarizer.utils import *
from src.summarizer.entity import DataIngestionConfig
from src.summarizer.entity import DataValidationConfig
class ConfigurationManager:

    def __init__(self,config_path = CONFIG_PATH,params_path = PARAMS_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_file = config.local_data_file,
            source_URL = config.source_URL,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validation_config(self) ->DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            status_file = config.status_file,
            all_required_files = config.all_required_files
        )

        return data_validation_config
    
    
    