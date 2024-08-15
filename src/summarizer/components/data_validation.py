import os,sys
from src.summarizer.logging import logger
from src.summarizer.utils  import get_size
from src.summarizer.logging import logging
from src.summarizer.exception import CustomException
from pathlib import Path
from src.summarizer.constants import  *
from src.summarizer.utils import *
from src.summarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config : DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in all_files:
                if file not in self.config.all_required_files:
                    validation_status = False
                    with open(self.config.status_file,"w") as f:
                        f.write(f"Validation status: {validation_status}")

                else: 
                    validation_status = True
                    with open(self.config.status_file,"r") as f:
                        existing_status = f.read()
                        if existing_status == "Validation status: True":
                            logger.info("No new files found. Skipping validation")
                        else:
                            with open(self.config.status_file,"w") as f:
                                f.write(f"Validation status: {validation_status}")
        except Exception    as e:
                raise CustomException(e,sys)
