from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from mlProject.config.configuration import ConfigurationManager
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    cfg_manager = ConfigurationManager()
    try:
        STAGE_NAME = "Data Ingestion"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline(cfg_manager)
        obj.main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    try:
        STAGE_NAME = "Data Validation"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline(cfg_manager)
        validation_status = obj.main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    try:
        if not validation_status:
            raise ValueError("Data is not valid.")
        STAGE_NAME = "data trandformation"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        DataTransformationTrainingPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    try:
        STAGE_NAME = "Model training"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        ModelTrainingPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
    try:
        cfg_manager = ConfigurationManager()
        STAGE_NAME = "Model evaluation"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        ModelEvaluationPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e