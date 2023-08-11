from typing import Any
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger



class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self) -> Any:
        cfg_manager = ConfigurationManager()
        data_ingestion_config = cfg_manager.get_data_ingestion_config()
        print(data_ingestion_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()

if __name__ == "__main__":
    try:
        STAGE_NAME = "Data Ingestion"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        DataIngestionTrainingPipeline().main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e