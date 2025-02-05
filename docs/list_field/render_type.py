from typing import Literal

import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from dash_pydantic_form import ModelForm
from dash_pydantic_utils import model_construct_recursive
from pydantic import BaseModel, Field


class Pet(BaseModel):
    name: str = Field(title="Name")
    species: Literal["cat", "dog"] = Field(title="Species")

    def __str__(self):
        return str(self.name)


class User(BaseModel):
    username: str = Field(title="Username")
    pets: list[Pet] = Field(title="Pets", default_factory=list)


def create_form(user: User | None = None, **options):
    user = user or User(
        username="Bob",
        pets=[
            {"name": "Rex", "species": "dog"},
            {"name": "Felix", "species": "cat"},
        ],
    )
    return ModelForm(
        user,
        "user",
        "list-renders",
        fields_repr={"pets": options},
    )


class Options(BaseModel):
    render_type: Literal["accordion", "modal", "list"] = Field(
        title="List render", default="accordion", json_schema_extra={"repr_type": "RadioItems"}
    )
    items_creatable: bool = Field(title="Items creatable", default=True)
    items_deletable: bool = Field(title="Items deletable", default=True)
    read_only: bool = Field(title="Read only", default=False)
    required: bool = Field(title="Required", default=False)


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(None, **Options().model_dump()),
            id="list-renders-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        ModelForm(
            Options,
            aio_id="list",
            form_id="interactive-options",
            debounce_inputs=250,
        ),
    ],
    cols={"base": 1, "sm": 4},
    spacing="2rem",
)


@callback(
    Output("list-renders-wrapper", "children"),
    Input(ModelForm.ids.main("list", "interactive-options"), "data"),
    State(ModelForm.ids.main("user", "list-renders"), "data"),
    prevent_initial_call=True,
)
def update_form(options: dict, form_data: dict):
    item = model_construct_recursive(form_data, User)
    return create_form(item, **options)
