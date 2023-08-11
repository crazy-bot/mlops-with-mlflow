from typing import Any
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger



class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self) -> Any:
        cfg_manager = ConfigurationManager()
        data_validation_config = cfg_manager.get_data_ingestion_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        STAGE_NAME = "Data Validation"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        DataValidationTrainingPipeline()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e