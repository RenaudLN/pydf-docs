from typing import Literal

import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from dash_pydantic_form import ModelForm, fields
from dash_pydantic_utils import model_construct_recursive
from pydantic import BaseModel, Field, field_validator

BASE_RENDER = "accordion"


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
    title: str | None = Field(title="Title", default="Pets")
    description: str | None = Field(title="Description", default=None)
    with_upload: bool = Field(title="With upload", default=True)
    with_download: bool = Field(title="With download", default=True)
    rows_editable: bool = Field(title="Rows editable", default=True)
    read_only: bool = Field(title="Read only", default=False)
    required: bool = Field(title="Required", default=False)
    table_height: int = Field(title="Table height", default=300)

    @field_validator("title", mode="before")
    @classmethod
    def validate_title(cls, v):
        if not v:
            return None
        return v


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(**Options().model_dump()),
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
            debounce_inputs=250,
        ),
    ],
    cols={"base": 1, "sm": 4},
    spacing="2rem",
)


@callback(
    Output("interactive3-wrapper", "children"),
    Input(ModelForm.ids.main("editable-table", "interactive-options"), "data"),
    State(ModelForm.ids.main("user", "interactive-table"), "data"),
    prevent_initial_call=True,
)
def update_form(options: dict, form_data: dict):
    item = model_construct_recursive(form_data, User)
    return create_form(user=item, **options)
