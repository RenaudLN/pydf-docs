from typing import Literal

import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from dash_pydantic_form import ModelForm, fields
from dash_pydantic_form.utils import model_construct_recursive
from pydantic import BaseModel, Field


class Pet(BaseModel):
    name: str = Field(title="Name")
    species: Literal["cat", "dog"] = Field(title="Species")


class User(BaseModel):
    username: str = Field(title="Username")
    pets: list[Pet] = Field(title="Pets", default_factory=list)


def create_form(
    user: User | None = None,
    **options,
):
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
        "interactive-table",
        fields_repr={"pets": fields.Table(**options)},
    )


class Options(BaseModel):
    with_upload: bool = Field(title="With upload", default=True)
    rows_editable: bool = Field(title="Rows editable", default=True)
    table_height: int = Field(title="Table height", default=300)


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(),
            id="interactive3-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        ModelForm(
            Options,
            aio_id="editable-table",
            form_id="interactive-options",
            fields_repr={
                "table_height": fields.Slider(input_kwargs={"min": 150, "max": 400, "step": 50}),
            },
        ),
    ],
    cols=4,
    spacing="2rem",
)


@callback(
    Output("interactive3-wrapper", "children"),
    Input(ModelForm.ids.main("editable-table", "interactive-options"), "data"),
    State(ModelForm.ids.main("user", "interactive-table"), "data"),
    prevent_initial_call=True,
)
def update_form(options_data: dict, form_data: dict):
    item = model_construct_recursive(form_data, User)
    return create_form(user=item, **options_data)
