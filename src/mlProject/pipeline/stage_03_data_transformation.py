from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger

class DataTransformationTrainingPipeline:
    def __init__(self, cfg_manager) -> None:
        self.cfg_manager = cfg_manager
    
    def main(self):
        data_transformation_config = self.cfg_manager.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.train_test_split()
        

if __name__ == "__main__":
    try:
        cfg_manager = ConfigurationManager()
        STAGE_NAME = "data trandformation"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        DataTransformationTrainingPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e