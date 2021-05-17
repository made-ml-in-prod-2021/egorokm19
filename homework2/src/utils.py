from typing import Union
import pickle
import json
import pandas as pd
from fastapi import FastAPI, HTTPException
from sklearn.pipeline import Pipeline
from entities import InputParams, PredictParams


def load_object(
    path: str
) -> Pipeline:
    """
    Load models pickle.
    """
    with open(path, "rb") as f:
        return pickle.load(f)
    
def open_json(path: str) -> json:
    """
    Open file json.
    """
    with open(path, 'r') as file:
        json_file = json.load(file)
       
    return json_file
    
    
def make_predict(
    request: InputParams, model: Pipeline
) -> Union[HTTPException, PredictParams]:
    """
    Make predict values.
    """
    df = pd.DataFrame([dict(request)])
    # add to data validation
    if df['cp'].values[0] not in [0, 1, 2, 3]:
        raise HTTPException(status_code=400, detail="Chest pain type must be on of: 0, 1, 2 or 3.")
    # models preict
    pred = model.predict(df)
    
    return PredictParams(prediction=pred)