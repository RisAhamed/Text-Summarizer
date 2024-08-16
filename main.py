from src.summarizer.logging import logger
import sys
from src.summarizer.exception import CustomException    
from src.summarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.summarizer.pipeline.data_validation_pipeline import DatavalidationTrainingPipeline
from src.summarizer.pipeline.data_transforamtion_pipeline import DataTransformationTrainingpipeline

try:
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
except Exception as e:
    raise CustomException(e,sys)

try:
    datavalidation = DatavalidationTrainingPipeline()
    datavalidation.main()
except Exception as e:
    raise CustomException(e,sys)


try:
    datatransformation = DataTransformationTrainingpipeline()
    datatransformation.main()
except Exception as e:
    raise CustomException(e,sys)