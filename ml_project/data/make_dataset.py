from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from ml_project.entities.split_params import SplittingParams


def read_dataset(path: str) -> pd.DataFrame:
    """
    Read csv file.
    """
    dataset = pd.read_csv(path)
    return dataset


def split_train_val_data(
    data: pd.DataFrame, params: SplittingParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data to train and test.
    """
    train_data, val_data = train_test_split(
        data, test_size=params.val_size,
        random_state=params.random_state
    )
    return train_data, val_data


