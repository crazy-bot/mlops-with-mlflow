from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

class ModelEvaluationPipeline:
    def __init__(self, cfg_manager: ConfigurationManager) -> None:
        self.cfg_manager = cfg_manager
    
    def main(self):
        model_eval_config = self.cfg_manager.get_model_evaluation_config()
        model_evaluator = ModelEvaluation(model_eval_config)
        model_evaluator.log_in_mlflow()
        

if __name__ == "__main__":
    try:
        cfg_manager = ConfigurationManager()
        STAGE_NAME = "Model evaluation"
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        ModelEvaluationPipeline(cfg_manager).main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e