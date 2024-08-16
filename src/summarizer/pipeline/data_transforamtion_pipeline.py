from src.summarizer.exception import CustomException
from src.summarizer.logging import logger
from src.summarizer.config.configuration import ConfigurationManager
from src.summarizer.components.data_transformation import DataTransformation


class DataTransformationTrainingpipeline:
    def __init__(self):
        pass

    def  main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()