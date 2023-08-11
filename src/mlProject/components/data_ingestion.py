import os
import zipfile
from mlProject import logger
from mlProject.utils.common import getsize
from urllib import request
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: {headers}")
        else:
            logger.info(f"file already exists with size: {getsize(self.config.local_data_file)}")
    
    def extract_zipfile(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)