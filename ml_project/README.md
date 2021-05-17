ml_project
==============================

This is the first homework project

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── configs            <- Config file in model and logging.
    │   ├── logging.conf.yml    
    │   └── train_config.yaml
    ├── data               <- The original, immutable data dump.
    │   ├── raw
    │   │   └── heart.csv  <- Dataset.    
    │   └── make_dataset.py
    │
    ├── entities                       <- Parametrs for entities.
    │   ├── eda_params.py              <- EDA analysis.
    │   ├── feature_params.py          <- Parametrs features.
    │   ├── logger_params.py           <- Parametrs logging.
    │   ├── split_params.py            <- Split dataset.
    │   ├── train_params.py            <- Parametrs for train model.
    │   └── train_pipeline_params.py   <- Pipeline train model.
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   ├── utils.py
    │   └── metrics.json
    │
    ├── notebooks          <- Jupyter notebooks. EDA for dataset.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── eda_reports.py <- Generated analysis as txt file.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── test                             <- Test for projects.
    │   ├── data                         <- Test for dataset.
    │   │   ├── test_make_dataset.py
    │   │   └── test.csv                 <- Generated random dataset.
    │   ├── features                     <- Test for features.
    │   │   └── test_process_features.py
    │   ├── models                       <- Test for models.
    │   │   └── test_process_features.py
    │   └── data_generator               <- Scripts for generated random data.
    │
    ├── LICENSE    <- Project license.
    │
    ├── Makefile   <- Project makefile.
    │
    ├── README.md  <- Project description.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
    │
    ├── tox.ini            <- Tox file with settings for running tox; see tox.readthedocs.io
    │
    ├── train_pipeline.py  <- Scripts all pipeline model (transform, train, predict, valid and save model)
    │
    └── utils.py           <- Build logger.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
