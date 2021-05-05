import os
import logging
from logging import Logger
import pandas as pd
import seaborn as sns

from ml_project.utils import build_logger
from ml_project.entities import EDAReportsParams, LoggerParams


ALL_FEATURES = ['sex', 'cp', 'fbs', 'restecg',
                'exang', 'slope', 'thal', 'age',
                'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']
TARGET_COl = 'target'


def option_pandas():
    """
    Pandas stats all data.
    """
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)


def build_report(writer: Logger, config_params: EDAReportsParams):
    """
    Create EDA reports.
    """
    dataset = pd.read_csv(config_params.path_data)

    get_title(writer, config_params.path_data)
    get_stats(writer, dataset)
    get_correlations(writer, dataset)
    get_correlations(writer, dataset)
    save_figure_correlations(dataset)


def get_title(writer: Logger, path_data: str):
    """
    Print EDA reports.
    """
    title = 'Exploratory data analysis (EDA) for Heart Disease UCI'
    writer.info(title)
    writer.info(f'\nDataset source: {os.path.abspath(path_data)}\n')


def get_stats(writer: Logger, dataset: pd.DataFrame):
    """
    Print statistics dataset.
    """
    writer.info(f'*** Outputting the first 5 lines: ***\n{dataset.head}\n')
    writer.info(f'*** Info dataset: ***\n{dataset.info()}\n')
    writer.info(f'*** Describe dataset: ***\n{dataset.describe()}\n')
    writer.info(f'*** Values missing in dataset: ***\n{dataset.isnull().sum()}\n')
    writer.info(f'*** Targets value: ***\n{dataset[TARGET_COl].value_counts().to_dict()}\n')


def get_correlations(writer: Logger, dataset: pd.DataFrame):
    """
    Print correlation analysis.
    """
    writer.info('*** Feature Correlations: ***')
    writer.info(dataset[ALL_FEATURES].corr())

    
def save_figure_correlations(dataset: pd.DataFrame):
    """
    Save figure correlation.
    """
    sns_heatmap = sns.heatmap(dataset[ALL_FEATURES].corr())
    sns_heatmap.figure.savefig("ml_project/reports/figures/dataset_corr.png")


def main(params: EDAReportsParams):
    """
    Pipeline entry point.
    """
    writer_params = LoggerParams(path=params.path_save,
                                 format='%(message)s',
                                 date_format='%Y-%m-%d %H:%M:%S',
                                 stdout=False,
                                 level=logging.INFO,
                                 mode='w+')
    writer = build_logger(params.name, writer_params)

    option_pandas()
    build_report(writer, params)


if __name__ == '__main__':
    main(EDAReportsParams)