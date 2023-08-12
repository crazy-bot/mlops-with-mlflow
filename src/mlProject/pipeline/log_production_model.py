from mlProject.config.configuration import ConfigurationManager
import argparse
import mlflow
from mlflow.tracking import MlflowClient
from pprint import pprint
import joblib
import os
from dotenv import load_dotenv
load_dotenv()

def log_prod_model():
    model_name = "ElasticNet"
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
    mlflow.get_tracking_uri()
    #exp = mlflow.get_experiment_by_name("Default")
    runs = mlflow.search_runs(experiment_ids=["0"])
    lowest_mse = runs["metrics.mean_squared_error"].sort_values(ascending=True)[0]
    lowest_run_id = runs[runs["metrics.mean_squared_error"] == lowest_mse]["run_id"][0]
    client = MlflowClient()
    for mv in client.search_model_versions(f"name='{model_name}'"):
        print(mv)
        if mv.run_id == lowest_run_id:
            cur_version = mv.version
            logged_model = mv.source
            pprint(mv, indent=4)
            client.transition_model_version_stage(
                name=model_name,
                version=cur_version,
                stage="Production"
            )
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    joblib.dump(loaded_model, os.path.join("artifacts", "prodmodel.joblib"))