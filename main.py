from src.summarizer.logging import logger
import sys
from src.summarizer.exception import CustomException    
from src.summarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

try:
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
except Exception as e:
    raise CustomException(e,sys)