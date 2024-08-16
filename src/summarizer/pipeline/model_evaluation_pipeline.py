from src.summarizer.config.configuration import ConfigurationManager
from src.summarizer.components.model_evaluation import ModelEvaluation
from src.summarizer.logging import logger




class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
        logger.info("Model Evaluation Completed")