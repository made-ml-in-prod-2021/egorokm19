import os
import pickle

import pandas as pd
import numpy as np
import click
from sklearn.linear_model import LogisticRegression


@click.command("train")
@click.option("--data-dir")
@click.option("--model-dir")
def train(data_dir: str, model_dir: str):
    """Обучение модели"""
    X = pd.read_csv(os.path.join(data_dir, "train_std.csv"), header=None).to_numpy()
    y = pd.read_csv(os.path.join(data_dir, "train_target.csv")).values.ravel()
    model = LogisticRegression()
    model.fit(X, y)

    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "log_model.pkl"), "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    train()
