import json
from typing import Literal

import dash_mantine_components as dmc
from dash import Input, Output, callback
from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field


class Pet(BaseModel):
    name: str = Field(title="Name")
    species: Literal["cat", "dog"] = Field(title="Species")

    def __str__(self):
        return str(self.name)


class User(BaseModel):
    pets: dict[str, Pet] = Field(title="Pets", default_factory=dict)


bob = User(
    pets={
        "rex": {"name": "Rex", "species": "dog"},
        "felix": {"name": "Felix", "species": "cat"},
    },
)
component = dmc.Stack(
    [
        ModelForm(bob, "user", "dict1", submit_on_enter=True),
        dmc.Code(id="output-dict1", style={"whiteSpace": "pre"}),
    ]
)


@callback(
    Output("output-dict1", "children"),
    Input(ModelForm.ids.main("user", "dict1"), "data"),
)
def update_dict_form(form_data: dict):
    return json.dumps(form_data, indent=2)
