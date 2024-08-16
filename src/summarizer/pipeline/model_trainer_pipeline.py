import sys
from src.summarizer.exception import CustomException
from src.summarizer.config.configuration import ConfigurationManager
from src.summarizer.components.model_trainer import ModelTrainer
class ModelTrainerPipeline:
    def __init__(Self):
        pass
    def main(self):
        try:

            # trainer = ModelTrainer(config=model_trainer_config)
            # trainer.train()
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise CustomException(e, sys)
