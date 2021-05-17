import requests

from src import open_json


DATA_PATH = 'data/data.json'


if __name__ == "__main__":
    json_file = open_json(DATA_PATH)

    response = requests.post(
        "http://0.0.0.0:8000/predict",
        json=json_file,
    )
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.json()}")
