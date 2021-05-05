import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score

from ml_project.entities import TrainingParams


def train_model(
        features: pd.DataFrame,
        target: pd.Series,
        train_params: TrainingParams
) -> RandomForestClassifier:
    """
    Build trainer and train model.
    """
    if train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(max_depth=train_params.max_depth,
                                       random_state=train_params.random_state)
    else:
        raise NotImplementedError()

    model.fit(features, target)
    return model


def predict(
    model: RandomForestClassifier,
    features: pd.DataFrame
) -> np.ndarray:
    """
    Predict model."""
    pred = model.predict(features)
    return pred


def evaluate_model(
        pred: np.ndarray,
        target: pd.Series
) -> Dict[str, float]:
    """
    Result metrics.
    """
    return {
        "accuracy": accuracy_score(target, pred),
        "f1": f1_score(target, pred),
        "precision": precision_score(target, pred)
    }


def save_model(
    model: RandomForestClassifier,
    output: str
) -> str:
    """
    Save result model.
    """
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output