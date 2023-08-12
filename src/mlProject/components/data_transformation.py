import pandas as pd
import os
from sklearn.model_selection import train_test_split
from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig
class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config
        
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        
        train_df, test_df = train_test_split(data, test_size=0.2)
        train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("splitted data into train and test set")
        logger.info(train_df.shape)
        logger.info(test_df.shape)