from pydantic import BaseModel


class PredictParams(BaseModel):
    """
    Predict params.
    """
    prediction: int