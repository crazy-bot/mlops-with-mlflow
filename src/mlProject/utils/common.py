import os
from pathlib import Path
import json
import yaml
import joblib
from mlProject import logger
from box.exceptions import BoxValueError
from box import ConfigBox
from typing import Any, Dict, List


def read_yaml(path: Path)->ConfigBox:
    try:
        with open(path) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file: {path} loaded successfully") 
    return ConfigBox(content)


def save_json(path:Path, data:Dict)->None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file: {path} dumped successfully") 


def load_bin(path:Path)->Any:
    data = joblib.load(path)
    logger.info(f"bin file: {path} loaded successfully")
    return data


def save_bin(data:Any, path:Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"bin file: {path} dumped successfully")


def getsize(path:Path):
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"size in kb: {size_in_kb}"

def create_directories(paths, verbose=True):
    for path in paths:
        path = Path(path)
        os.makedirs(path, exist_ok=True)
        
        if verbose:
            logger.info(f"created directory: {path}")
