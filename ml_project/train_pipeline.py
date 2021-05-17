import json
import logging
import logging.config
import yaml
import click

from utils import setup_logging
from ml_project.data import read_dataset, split_train_val_data
from ml_project.entities import (
    TrainingPipelineParams,
    read_training_pipeline_params,
)
from ml_project.features import (
    build_transformer,
    transform_features,
    extract_target
)
from ml_project.models import (
    train_model,
    predict,
    evaluate_model,
    save_model,
)


logger = logging.getLogger(__name__)
        
        
def save_metrics(metric_path: str, metrics: dict):
    """
    Save metrics.
    """
    with open(metric_path, "w") as metric_file:
        json.dump(metrics, metric_file)
        

def train_pipeline(training_pipeline_params: TrainingPipelineParams):
    """
    Pipeline train model.
    """
    logger.info(f"Start train pipeline with params {training_pipeline_params}\n")
    data = read_dataset(training_pipeline_params.input_data_path)
    logger.info(f"Data shape is {data.shape}")
    data_train, data_val = split_train_val_data(
        data, training_pipeline_params.split_params
    )
    logger.info(f"Data_train shape is {data_train.shape}")
    logger.info(f"Data_val shape is {data_val.shape}")

    transformer = build_transformer(training_pipeline_params.feature_params)
    transformer.fit(data_train)
    train_features = transform_features(transformer, data_train)
    logger.debug(f"train_features shape is {train_features.shape}")
    train_target = extract_target(data_train,
                              training_pipeline_params.feature_params)

    model = train_model(
        train_features, train_target, training_pipeline_params.train_params
    )
    logger.info(f"{training_pipeline_params.train_params.model_type} trained")

    test_features = transform_features(transformer, data_val)
    test_target = extract_target(data_val, training_pipeline_params.feature_params)

    logger.info(f"test_features shape is {test_features.shape}")
    predicted = predict(
        model,
        test_features
    )

    metrics = evaluate_model(
        predicted,
        test_target
    )

    logger.info(f"Metrics on test: {metrics}")
    save_metrics(metric_path=training_pipeline_params.metric_path, metrics=metrics)
    logger.info(f"Metrics save in file")

    save_model(model, training_pipeline_params.output_model_path)

    return metrics


@click.command()
@click.argument("config_path")
def train_pipeline_command(config_path: str):
    params = read_training_pipeline_params(config_path)
    setup_logging(params)
    train_pipeline(params)


if __name__ == "__main__":
    train_pipeline_command()