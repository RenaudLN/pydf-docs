from datetime import date

from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field


class User(BaseModel):
    jobs: dict[str, str] = Field(title="Jobs", default_factory=dict)
    dates: dict[str, date] = Field(title="Dates", default_factory=dict)


bob = User(
    jobs={"2018": "Engineer", "2020": "Data scientist", "2023": "Frontend dev"},
    dates={"birth": "1990-01-01", "graduation": "2010-07-09"},
)
component = ModelForm(bob, "user", "scalar_dict")
