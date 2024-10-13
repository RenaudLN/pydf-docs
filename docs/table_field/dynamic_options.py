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

component = ModelForm(
    bob,
    "user",
    "table_dynamic",
    fields_repr={
        "pets": fields.Table(
            description="Species options depends on the name of the pet.",
            dynamic_options={"species": {"namespace": "pets", "function_name": "getSpecies"}},
            column_defs_overrides={
                "species": {
                    "cellEditorParams": {
                        "catNames": ["Felix", "Cookie"],
                        "dogNames": ["Rex", "Brownie"],
                    }
                }
            },
        )
    }
)
