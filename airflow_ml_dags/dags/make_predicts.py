from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.sensors.filesystem import FileSensor

from utils import default_args, DEFAULT_PATH


with DAG(
    "make_predicts",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(3)
) as dag:
    start_task = DummyOperator(task_id='start-predict')
    data_await = FileSensor(
        task_id="await-features",
        poke_interval=10,
        retries=100,
        filepath="data/raw/{{ ds }}/data.csv"
    )
    model_await = FileSensor(
        task_id="await-model",
        poke_interval=10,
        retries=100,
        filepath="data/models/{{ ds }}/log_model.pkl"
    )
    scaler_await = FileSensor(
        task_id="await-scaler",
        poke_interval=10,
        retries=100,
        filepath="{{ var.value.model_dir }}/{{ ds }}/std_model.pkl"
    )
    predict = DockerOperator(
        task_id="generate-predicts",
        image="airflow-predict",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/predictions/{{ ds }}"
                " --model-dir {{ var.value.model_dir }}/{{ ds }}/",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_PATH]
    )
    end_task = DummyOperator(task_id='end-predict')

    start_task >> [data_await, model_await, scaler_await] >> predict >> end_task
