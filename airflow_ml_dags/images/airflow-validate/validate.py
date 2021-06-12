import os
import pickle
import json

import pandas as pd
import click
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score


@click.command("validate")
@click.option("--data-dir")
@click.option("--model-dir")
def validate(data_dir: str, model_dir: str):
    """Смотрим на метрике для модели."""
    # загрузка модели
    with open(os.path.join(model_dir, "log_model.pkl"), "rb") as log_model:
        model = pickle.load(log_model)
    # загрузка std модели
    with open(os.path.join(model_dir, "std_model.pkl"), "rb") as std:
        std_model = pickle.load(std)
    
    # загруажем данные
    data_test = pd.read_csv(os.path.join(data_dir, "test.csv"))
    test_X, test_y = data_test.drop('target', axis=1), data_test['target']
    test_X = std_model.transform(test_X)
    predict_model = model.predict(test_X)
    metrics = {
        "roc_auc_score": roc_auc_score(test_y, predict_model),
        "accuracy_score": accuracy_score(test_y, predict_model),
        "f1_score": f1_score(test_y, predict_model),
    }

    with open(os.path.join(model_dir, "metrics.json"), "w") as f:
        json.dump(metrics, f)


if __name__ == '__main__':
    validate()
