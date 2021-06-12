import os
import pickle
import pandas as pd
import numpy as np
import click
from sklearn.preprocessing import StandardScaler


@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
def preprocess(input_dir: str, output_dir: str, model_dir: str):
    """Обработка данных через std."""
    train = pd.read_csv(os.path.join(input_dir, "train.csv"))
    std = StandardScaler()
    std_train = std.fit_transform(train.drop('target', axis=1))
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(model_dir, exist_ok=True)
    train['target'].to_csv(os.path.join(output_dir, "train_target.csv"), index=False)
    np.savetxt(os.path.join(output_dir, "train_std.csv"), std_train, delimiter=",")
    with open(os.path.join(model_dir, "std_model.pkl"), "wb") as f:
        pickle.dump(std, f)


if __name__ == '__main__':
    preprocess()
