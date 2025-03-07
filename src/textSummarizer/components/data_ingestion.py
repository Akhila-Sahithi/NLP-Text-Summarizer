import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import (DataIngestionConfig)

import os
from pathlib import Path
from urllib import request

class DataIngestion:
    def __init__(self, config):
        self.config = config 

    def download_file(self):
        local_data_file = self.config["local_data_file"] 
        os.makedirs(os.path.dirname(local_data_file), exist_ok=True) 

        if not os.path.exists(local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config["source_URL"],
                filename=local_data_file
            )
            print(f"{filename} downloaded! Info: \n{headers}")
        else:
            print(f"File already exists at: {local_data_file}")

    def extract_zip_file(self):
        unzip_path = self.config["unzip_dir"]
        local_data_file = self.config["local_data_file"]

        os.makedirs(unzip_path, exist_ok=True)  

        if os.path.exists(local_data_file):
            import zipfile
            with zipfile.ZipFile(local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            print(f"Extracted to: {unzip_path}")
        else:
            raise FileNotFoundError(f"Zip file not found: {local_data_file}")
