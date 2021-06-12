from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

from utils import default_args, DEFAULT_PATH


with DAG(
    "generation_data",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(3)
) as dag:
    start_task = DummyOperator(task_id='start-generation-data')
    download_data = DockerOperator(
        task_id="docker-airflow-download",
        image="airflow-download",
        command="/data/raw/{{ ds }}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_PATH]
    )

    end_task = DummyOperator(task_id='end-generation-data')

    start_task >> download_data >> end_task
