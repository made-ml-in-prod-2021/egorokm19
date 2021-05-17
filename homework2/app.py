import os
from typing import Optional, Union
import logging
import uvicorn
import pickle
from fastapi import FastAPI
from sklearn.pipeline import Pipeline
from pydantic import BaseModel, Field

from entities import InputParams, PredictParams
from src import load_object, make_predict


logger = logging.getLogger(__name__)


# initialize the model
model: Optional[Pipeline] = None
# we raise the server
app = FastAPI()


@app.get("/")
def main():
    return "This is the entry point of our predictor."


@app.on_event("startup")
def load_model():
    """
    Load model.
    """
    global model
    model_path = os.getenv("PATH_MODEL", "rf_classifier.pkl")
    if model_path is None:
        err = f"PATH_MODEL {model_path} is None"
        logger.error(err)
        raise RuntimeError(err)

    model = load_object(model_path)


@app.get("/health")
def health() -> bool:
    return not (model is None)


@app.post("/predict")
def predict(request: InputParams):
    """
    Predict results.
    """
    return make_predict(request, model)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))