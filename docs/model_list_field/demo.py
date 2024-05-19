from typing import Literal

from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field

BASE_RENDER = "accordion"

class Pet(BaseModel):
    name: str = Field(title="Name")
    species: Literal["cat", "dog"] = Field(title="Species")

class User(BaseModel):
    username: str = Field(title="Username")
    pets: list[Pet] = Field(title="Pets", default_factory=list)

bob = User(username="Bob", pets=[{"name": "Rex", "species": "dog"}])

component = ModelForm(bob, "user", "list1")
