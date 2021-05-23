from collections import defaultdict, OrderedDict
from typing import List
import numpy as np
import pandas as pd
import pytest

from ml_project.data.make_dataset import read_dataset, split_train_val_data
from ml_project.entities.split_params import SplittingParams
from ml_project.tests.data_generator import generate_dataframe


DATA_PATH = "ml_project/files/raw/heart.csv"
DATA_TEST = "ml_project/files/raw/test.csv"
TARGET_COL = "target"
SMALL_SHAPE = 300
MEAN_SHAPE = 500
VAL_FEATURE = 9


@pytest.fixture()
def data_small() -> pd.DataFrame:
    return generate_dataframe(SMALL_SHAPE, VAL_FEATURE)


@pytest.fixture()
def data_mean() -> pd.DataFrame:
    return generate_dataframe(MEAN_SHAPE, VAL_FEATURE)


def test_can_load_dataset(data_small):
    """
    Test assembly dataset.
    """
    assert data_small.shape[0] == SMALL_SHAPE
    assert data_small.isna().sum().sum() == 0, \
        "fake data has NaN"
    assert TARGET_COL in data_small.keys(), \
        "target columns is missing from the fake data"


def test_read_data(tmpdir, data_small):
    """
    Test open file.
    """
    data_small.to_csv(DATA_TEST, index=False)
    data = read_dataset(DATA_TEST)

    assert np.allclose(data_small.values, data.values)


def test_split_train_valid_data(data_mean):
    """
    Test data shape and split.
    """
    val_size = 0.2
    splitting_params = SplittingParams(random_state=9, val_size=val_size)
    train, valid = split_train_val_data(data_mean, splitting_params)

    assert len(train.index) == 400
    assert len(valid.index) == 100
    assert train.shape[0] == MEAN_SHAPE * (1 - val_size), \
            "wrong train shape"
    assert valid.shape[0] == MEAN_SHAPE * val_size, \
            "wrong valid shape"