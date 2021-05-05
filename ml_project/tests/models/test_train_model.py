import pytest
import pandas as pd
from typing import Tuple
from sklearn.ensemble import RandomForestClassifier
import pickle
from py._path.local import LocalPath

from ml_project.tests.data import data_small
from ml_project.tests.features import feature_params
from ml_project.features import (build_transformer,
                                 transform_features,
                                 extract_target)
from ml_project.entities import TrainingParams

from ml_project.models.utils import (
    train_model,
    predict,
    save_model
)


@pytest.fixture
def get_features_target_value(data_small, feature_params):
    transformer = build_transformer(feature_params)
    transformer.fit(data_small)
    features = transform_features(transformer, data_small)
    target = extract_target(data_small, feature_params)

    return features, target


def test_can_train_model(get_features_target_value: Tuple[pd.DataFrame, pd.Series]):
    """
    TEst model train.
    """
    features, target = get_features_target_value
    model = train_model(features, target, train_params=TrainingParams())

    assert isinstance(model, RandomForestClassifier), \
        f"unexpected model {model.__dict__['base_estimator']}"
    predicted_shape = predict(model, features).shape[0]
    assert predicted_shape == target.shape[0], \
        f"predicted shape {predicted_shape} while should be {target.shape[0]}"


def test_can_save_model(tmpdir: LocalPath):
    """
    Test save model.
    """
    model = RandomForestClassifier(n_estimators=50)
    expected_path = tmpdir.join("model.pkl")
    save_model(model, expected_path)
    with open(expected_path, "rb") as f:
        model = pickle.load(f)

    assert isinstance(model, RandomForestClassifier), \
        f"unexpected model {model.__dict__['base_estimator']}"




