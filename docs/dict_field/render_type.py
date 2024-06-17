from typing import Literal

import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from dash_pydantic_form import ModelForm
from dash_pydantic_form.utils import model_construct_recursive
from pydantic import BaseModel, Field

BASE_RENDER = "accordion"


class Pet(BaseModel):
    name: str = Field(title="Name")
    species: Literal["cat", "dog"] = Field(title="Species")

    def __str__(self):
        return str(self.name)


class User(BaseModel):
    pets: dict[str, Pet] = Field(title="Pets", default_factory=dict)


def create_form(render: str = BASE_RENDER, user: User | None = None):
    user = user or User(
        pets={
            "rex": {"name": "Rex", "species": "dog"},
            "felix": {"name": "Felix", "species": "cat"},
        },
    )
    return ModelForm(
        user,
        "user",
        "dict-renders",
        fields_repr={
            "pets": {"render_type": render},
        },
    )


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(BASE_RENDER),
            id="dict-renders-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        dmc.Stack(
            [
                dmc.RadioGroup(
                    label="Sections render",
                    id="dict-renders-render",
                    value=BASE_RENDER,
                    children=dmc.Stack(
                        [dmc.Radio(label=x, value=x) for x in ["accordion", "modal"]],
                        gap="0.5rem",
                    ),
                ),
            ],
        ),
    ],
    cols=4,
    spacing="2rem",
)


@callback(
    Output("dict-renders-wrapper", "children"),
    Input("dict-renders-render", "value"),
    State(ModelForm.ids.main("user", "dict-renders"), "data"),
    prevent_initial_call=True,
)
def update_form(render: str, form_data: dict):
    item = model_construct_recursive(form_data, User)
    return create_form(render, item)
