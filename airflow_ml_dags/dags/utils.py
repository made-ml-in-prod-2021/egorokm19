from pathlib import Path
from datetime import timedelta


default_args = {
    "owner": "airflow",
    "email_on_failure": True,
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


DEFAULT_PATH = "/home/egoro/homework3/airflow_ml_dags/data:/data"
