import os
from mlProject.utils.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig

class ConfigurationManager:
    def __init__(self) -> None:
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            config.root_dir,
            config.source_url,
            config.local_data_file,
            config.unzip_dir
        )
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        return DataValidationConfig(
            config.root_dir,
            config.unzip_data_path,
            config.status_file,
            self.schema.columns
        )
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        return DataTransformationConfig(
            config.root_dir,
            config.data_path,
        )
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.target_columns
        
        create_directories([config.root_dir])
        return ModelTrainerConfig(
            config.root_dir,
            config.train_data_path,
            config.test_data_path,
            config.model_name,
            params.alpha,
            params.l1_ratio,
            schema.name
        )
        
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.target_columns
        
        create_directories([config.root_dir])
        return ModelEvaluationConfig(
            config.root_dir,
            config.test_data_path,
            config.model_path,
            config.metric_file,
            params,
            schema.name,
            mlflow_uri=os.getenv("MLFLOW_TRACKING_URI")
        )