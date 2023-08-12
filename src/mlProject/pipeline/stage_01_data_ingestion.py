from typing import Any
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger



class DataIngestionTrainingPipeline:
    def __init__(self, cfg_manager) -> None:
        self.cfg_manager = cfg_manager
    
    def main(self) -> Any:
        
        data_ingestion_config = self.cfg_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()

if __name__ == "__main__":
    try:
        cfg_manager = ConfigurationManager()
        STAGE_NAME = "Data Ingestion"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        DataIngestionTrainingPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e