import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ml_project.entities import FeatureParams


def build_feature_pipeline() -> Pipeline:
    """
    Build standart scaler feature pipeline.
    """
    features_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(missing_values=np.nan,
                                     strategy="most_frequent")),
            ("scaler", StandardScaler()),
        ]
    )

    return features_pipeline


def build_transformer(params: FeatureParams) -> ColumnTransformer:
    """
    Build feature pipeline.
    """
    transformer = ColumnTransformer(
        [
            (
                "all_pipeline",
                build_feature_pipeline(),
                params.all_features,
            )
        ]
    )

    return transformer


def transform_features(transformer: ColumnTransformer, dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Make transform features.
    """
    return pd.DataFrame(transformer.transform(dataset))


def extract_target(dataset: pd.DataFrame, params: FeatureParams) -> pd.Series:
    """
    Extract target in dataset
    """
    target = dataset[params.target_col]
    return target
