from dataclasses import dataclass
from pydantic import BaseModel


@dataclass()
class PredictParams(BaseModel):
    """
    Feature extraction config.
    """
    prediction: int