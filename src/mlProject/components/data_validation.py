from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config
        
    def validate_all_columns(self)-> bool:
        try:
            status = True
            data =  pd.read_csv(self.config.unzip_data_path)
            all_cols = list(data.columns)
            
            for col in all_cols:
                if col not in self.config.all_schema:
                    status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"failed validation with column: {col} \n")
                    break
                else:
                    with open(self.config.status_file, "w") as f:
                        f.write(f"validation passed with column: {col}")
                # if self.config.all_schema[col] != type(col):
                #     status = False
                #     with open(self.config.status_file, "w") as f:
                #         f.write(f"failed validation with column: {col}")
                #     break
            return status
        except Exception as e:
            raise e