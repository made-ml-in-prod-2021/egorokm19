from dataclasses import dataclass


@dataclass()
class EDAReportsParams:
    """
    EDA report config.
    """
    name: str = 'ml_project'
    path_data: str = 'ml_project/data/raw/heart.csv'
    path_save: str = 'ml_project/reports/reports.txt'