import sys

import pytest
from airflow.models import DagBag


sys.path.append("dags")


@pytest.fixture()
def dags_airflow():
    """Загружаем DAG."""
    return DagBag(dag_folder="dags/", include_examples=False)


def test_dags_airflow_import_correct(dags_airflow):
    """Проверка вызова DAG."""
    assert dags_airflow.dags is not None
    assert dags_airflow.import_errors == {}


def test_generation_data_dag_load(dags_airflow):
    """Проверка загрузки данных."""
    assert "generation_data" in dags_airflow.dags
    assert len(dags_airflow.dags["generation_data"].tasks) == 3


def test_generation_data_dag_structure(dags_airflow):
    """Проверка стурктуры блока загрузки данных."""
    generation_structure = {
        "start-generation-data": ["docker-airflow-download"],
        "docker-airflow-download": ["end-generation-data"],
        "end-generation-data": [],
    }
    dag = dags_airflow.dags["generation_data"]
    for name, task in dag.task_dict.items():
        assert set(generation_structure[name]) == task.downstream_task_ids


def test_train_model_dag_load(dags_airflow):
    """Проверка загрузки модели."""
    assert "train_models" in dags_airflow.dags
    assert len(dags_airflow.dags["train_models"].tasks) == 8


def test_train_model_dag_structure(dags_airflow):
    """Проверка структуры блока train модели."""
    structure_train = {
        "start-train-pipeline": ["await-target", "await-features"],
        "await-features": ["split-data"],
        "await-target": ["split-data"],
        "split-data": ["preprocess-data"],
        "preprocess-data": ["train-model"],
        "train-model": ["evaluate-model"],
        "evaluate-model": ["end-train-pipeline"],
        "end-train-pipeline": [],
    }
    dag = dags_airflow.dags["train_models"]
    for name, task in dag.task_dict.items():
        assert set(structure_train[name]) == task.downstream_task_ids


def test_predicts_dag_load(dags_airflow):
    """Проверка загрузки predict модели."""
    assert "make_predicts" in dags_airflow.dags
    assert len(dags_airflow.dags["make_predicts"].tasks) == 6


def test_predicts_dag_structure(dags_airflow):
    """Проверка структуры блока train модели."""
    structure_predict = {
        "start-predict": ["await-features", "await-scaler", "await-model"],
        "await-features": ["generate-predicts"],
        "await-scaler": ["generate-predicts"],
        "await-model": ["generate-predicts"],
        "generate-predicts": ["end-predict"],
        "end-predict": [],
    }
    dag = dags_airflow.dags["make_predicts"]
    for name, task in dag.task_dict.items():
        assert set(structure_predict[name]) == task.downstream_task_ids
