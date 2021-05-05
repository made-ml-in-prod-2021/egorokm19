from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    """
    Model training config
    """
    model_type: str = field(default="RandomForestClassifier")
    random_state: int = field(default=42)
    max_depth: int = field(default=4)