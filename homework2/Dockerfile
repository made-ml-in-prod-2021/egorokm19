FROM python:3.6-slim
COPY setup.py ./setup.py
RUN pip install -e .

COPY entities /entities
COPY src /src
COPY rf_classifier.pkl /model.pkl
COPY app.py /app.py

WORKDIR .

ENV PATH_MODEL="/model.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]