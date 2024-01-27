from textSummerizer.pipleline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummerizer.pipleline.stage_02_data_validation import (
    DataValidationTraningPipeline,
)
from textSummerizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<< \n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<")
    data_validation = DataValidationTraningPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<< \n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e
