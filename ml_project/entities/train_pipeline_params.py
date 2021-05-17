import yaml
from dataclasses import dataclass
from marshmallow_dataclass import class_schema

from ml_project.entities.split_params import SplittingParams
from ml_project.entities.feature_params import FeatureParams
from ml_project.entities.train_params import TrainingParams


@dataclass()
class TrainingPipelineParams:
    """
    Pipeline params.
    """
    logging_config_path: str
    input_data_path: str
    output_model_path: str
    metric_path: str
    split_params: SplittingParams
    feature_params: FeatureParams
    train_params: TrainingParams


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(path: str) -> TrainingPipelineParams:
    """
    Read train data.
    """
    with open(path, "r") as input_data:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_data))
