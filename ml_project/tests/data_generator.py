import random
import numpy as np
import pandas as pd


def generate_dataframe(data_shape, random_state, columns=None):
    """
    Generates random data.
    """
    random.seed(random_state)
    np.random.seed(random_state)

    dataset = pd.DataFrame({
        'age': np.random.randint(20, 81, data_shape),
        'cp': np.random.randint(0, 4, data_shape),
        'sex': np.random.randint(0, 2, data_shape),
        'trestbps': np.random.randint(100, 181, data_shape),
        'chol': np.random.randint(150, 380, data_shape),
        'fbs': np.random.randint(0, 2, data_shape),
        'restecg': np.random.randint(0, 2, data_shape),
        'thalach': np.random.randint(120, 211, data_shape),
        'exang': np.random.randint(0, 2, data_shape),
        'oldpeak': 4*np.random.rand(data_shape),
        'slope': np.random.randint(0, 3, data_shape),
        'ca': np.random.randint(0, 5, data_shape),
        'thal': np.random.randint(1, 4, data_shape),
        'target': np.random.randint(0, 2, data_shape),
    })

    if columns:
        dataset = dataset[colums]

    return dataset