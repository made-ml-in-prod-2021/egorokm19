import logging
import requests

from src import open_json


logger = logging.getLogger(__name__)


# file path
DATA_PATH = 'data/data.json'


if __name__ == "__main__":
    json_file = open_json(DATA_PATH)

    response = requests.post(
        "http://0.0.0.0:8000/predict",
        json=json_file,
    )
    logger.info(f"Status code: {response.status_code}\n")
    logger.info(f"Response body: {response.json()}\n")