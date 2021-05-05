from dataclasses import dataclass, field
from typing import List, Optional


@dataclass()
class FeatureParams:
    """
    Feature extraction config.
    """
    all_features: List[str] = field(default_factory=list)
    target_col: Optional[str] = None