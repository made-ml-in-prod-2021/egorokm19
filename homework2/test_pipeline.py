import json
from fastapi.testclient import TestClient

from .app import app
from .src import open_json


DATA_PATH = 'data/data.json'

client = TestClient(app)


def test_read_main():
    """
    Testing read function main.
    """
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == "This is the entry point of our predictor."
        

def test_predict():
    """
    Testing predict models.
    """
    with TestClient(app) as client:
        json_file = open_json(DATA_PATH)
        response = client.post(
            "/predict",
            json=json_file,
        )
        # check status code
        assert response.status_code == 200
        # check the length of the answer and the value of the answer itself and the answer key
        result = response.json()
        assert len(result) == 1
        assert result == {"prediction": 1}
        assert "prediction" in result
        assert result["prediction"] in [0, 1]

        
def test_validation_values():
    """
    Testing validation data.
    """
    with TestClient(app) as client:
        json_file = open_json(DATA_PATH)
        json_file['thal'] = None
        response = client.post(
            "/predict",
            json=json_file,
        )
        assert response.status_code == 422