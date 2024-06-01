from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(title="Username")
    jobs: list[str] = Field(title="Jobs", default_factory=list)


bob = User(
    username="Bob",
    jobs=["Engineer", "Data scientist", "Frontend dev"],
)
component = ModelForm(bob, "user", "scalar_list")
