import os
import pickle

import pandas as pd
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
def predict(input_dir: str, output_dir: str, model_dir: str):
    # загрузка модели
    with open(os.path.join(model_dir, "log_model.pkl"), "rb") as log_model:
        model = pickle.load(log_model)
    # загрузка std модели
    with open(os.path.join(model_dir, "std_model.pkl"), "rb") as std:
        std_model = pickle.load(std)
    # загружаем датасет
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    data["predict"] = model.predict(std_model.transform(data))
    # записываем результаты
    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "predict.csv"), index=False)


if __name__ == '__main__':
    predict()