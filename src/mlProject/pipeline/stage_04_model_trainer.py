from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import Trainer
from mlProject import logger

class ModelTrainingPipeline:
    def __init__(self, cfg_manager: ConfigurationManager) -> None:
        self.cfg_manager = cfg_manager
    
    def main(self):
        model_trainer_config = self.cfg_manager.get_model_trainer_config()
        model_trainer = Trainer(model_trainer_config)
        model_trainer.train()
        

if __name__ == "__main__":
    try:
        cfg_manager = ConfigurationManager()
        STAGE_NAME = "Model training"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        ModelTrainingPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e