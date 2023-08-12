

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import pandas as pd
import os
from mlProject.utils.common import load_bin, save_json
from mlProject.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config
        
    def eval_metrics(self, gt_y, pred_y):
        mae = mean_absolute_error(gt_y, pred_y)
        mse = mean_squared_error(gt_y, pred_y)
        r2 = r2_score(gt_y, pred_y)
        return mae, mse, r2
    
    def log_in_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        model = load_bin(self.config.model_path)
        
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            pred_y = model.predict(test_x)
            mae, mse, r2 = self.eval_metrics(test_y, pred_y)
            
            # save metrics in local metric file
            scores = {"mean_absolute_error": mae, "mean_squared_error": mse, "r2_score": r2}
            save_json(os.path.join(self.config.root_dir, self.config.metric_file), scores)
            
            # track in mlflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)
            
            if tracking_url_type_store != "file":
                # log and register in remote server
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNet")
            else:
                # log model in local
                mlflow.sklearn.log_model(model, "model")
        