from typing import Literal

from dash_pydantic_form import ModelForm, fields
from pydantic import BaseModel, Field


class Pet(BaseModel):
    name: str = Field(title="Name")
    species: Literal["cat", "dog"] = Field(title="Species")


class User(BaseModel):
    username: str = Field(title="Username")
    pets: list[Pet] = Field(title="Pets", default_factory=list)


bob = User(
    username="Bob",
    pets=[
        {"name": "Rex", "species": "dog"},
        {"name": "Felix", "species": "cat"},
    ],
)

component = ModelForm(bob, "user", "table1", fields_repr={"pets": fields.EditableTable()})
