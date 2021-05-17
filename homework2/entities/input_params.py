from pydantic import BaseModel, Field, validator


class InputParams(BaseModel):
    """
    Input params.
    """
    age: int = Field(default=None, gt=0, description="Age in years.")
    sex: int = Field(default=0, lt=2, description="1 - male, 0 - female.")
    cp: int = Field(default=0, description="Chest pain type: 0, 1, 2 or 3.")
    trestbps: int = Field(default=120, description="Resting blood pressure (in mm Hg on admission to the hospital).")
    chol: int = Field(default=200, description="Serum cholestoral in mg/dl.")
    fbs: int = Field(default=0, description="(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false).")
    restecg: int = Field(default=0, description="Resting electrocardiographic results.")
    thalach: int = Field(default=150, description="Maximum heart rate achieved.")
    exang: int = Field(default=0, description="Exercise induced angina (1 = yes; 0 = no).")
    oldpeak: float = Field(default=2.0, description="ST depression induced by exercise relative to rest.")
    slope: int = Field(default=0, description="The slope of the peak exercise ST segment.")
    ca: int = Field(default=0, description="Number of major vessels (0-3) colored by flourosopy.")
    thal: int = Field(default=0, description="Thalium Stress Test Result.")
        
    @validator('sex')
    def check_sex(cls, value_sex):
        """CHech sex values."""
        if value_sex < 0 or value_sex > 2:
            raise ValueError("The gender field cannot have a value of 0 or 1")
        return value_sex
    
    @validator('fbs')
    def check_fbs(cls, value_fbs):
        """CHech sex values."""
        if value_fbs < 0 or value_fbs > 2:
            raise ValueError("The fbs field cannot have a value of 0 or 1")
        return value_fbs
    
    @validator('exang')
    def check_exang(cls, value_exang):
        """CHech sex values."""
        if value_exang < 0 or value_exang > 2:
            raise ValueError("The exang field cannot have a value of 0 or 1")
        return value_exang