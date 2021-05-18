import os

from ml_project.train_pipeline import train_pipeline
from ml_project.entities import read_training_pipeline_params


CONFIG_PATH = "ml_project/configs/test_config.yaml"


def test_can_train_metrics():
    params = read_training_pipeline_params(CONFIG_PATH)
    metrics = train_pipeline(params)
    assert {"accuracy", "f1", "precision"} == metrics.keys(), \
        f"unexpected metrics output {metrics.keys()}"
    assert metrics["precision"] > 0, \
        f"Precision score {metrics['precision']} < 0"
    assert os.path.exists(params.output_model_path), \
        f"no such file {params.output_model_path}"
    assert os.path.exists(params.metric_path), \
        f"no such file {params.metric_path}"

