from src.summarizer.logging import logger
import sys
from src.summarizer.exception import CustomException    
try :
    a = 2/0
except Exception as e :
    raise CustomException(e,sys)
logger.info("THie is the demo file logger ")