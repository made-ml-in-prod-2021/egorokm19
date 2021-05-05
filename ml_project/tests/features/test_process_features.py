import numpy as np
import pytest
from sklearn.preprocessing import StandardScaler
from ml_project.entities import FeatureParams
from ml_project.features import (build_transformer,
                                 transform_features,
                                 extract_target)
from ml_project.tests.data import data_small


ALL_FEATURES = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "age", "trestbps", "chol", "thalach", "oldpeak"]
TARGET = "target"



@pytest.fixture
def feature_params() -> FeatureParams:
    params = FeatureParams(
        all_features=ALL_FEATURES,
        target_col=TARGET,
    )
    return params


def test_can_transform_features(data_small,
                            feature_params):
    """
    Test transform features.
    """
    transformer = build_transformer(feature_params)
    transformer.fit(data_small)
    features = transform_features(transformer, data_small)
    features_all = features.iloc[:, : len(ALL_FEATURES)]
    
    print(features_all.std(axis=0))

    assert np.allclose(features_all.mean(axis=0), 0, atol=1e-1), \
        "mean of scaled features not 0"
    assert np.allclose(features_all.std(axis=0), 1, atol=1e-1), \
        "std of scaled features not 1"
    assert features.isna().sum().sum() == 0, \
        "NaNs are present after transform"
    assert features.shape[0] == data_small.shape[0], \
        "features must contain the same number of rows as original data"
    assert data_small.shape[1] > features.shape[1], \
        "all features shape"


def test_can_extract_target(data_small, feature_params):
    """
    Test target value.
    """
    target = extract_target(data_small, feature_params)
    targets = set(np.unique(target))

    assert targets == {0, 1}, \
        f"target variable contains unexpected values {targets}"