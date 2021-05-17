### Запуск проекта
#### Предварительно нужно запустить:
```shell script
$ pip install -e .
```
#### После чего можно запускать докер:
```shell script
$ docker build -t egorokm/made_ml_prod_homework2:latest . 
$ docker run -p 8000:8000 egorokm/made_ml_prod_homework2:latest
```
----------
### Запуск с докер-хаба
```shell script
$ docker pull egorokm/made_ml_prod_homework2:latest
$ docker run -p 8000:8000 egorokm/made_ml_prod_homework2
```
----------
#### Тестовый запрос:
```shell script
$ python make_request.py
```
----------
#### Запуск для тестов проекта:
```shell script
$ python test_pipeline.py
```
----------
#### Оптимизация докер образа:
Изначально строил образ на `python:3.6` - получилось 1.29GB. Попробовал вместо этого `python:3.6-slim` - стало 524MB.