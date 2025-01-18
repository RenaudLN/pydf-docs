from typing import Literal

import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from dash_pydantic_form import FormLayout, FormSection, ModelForm
from dash_pydantic_form.utils import model_construct_recursive
from pydantic import BaseModel, Field

Continent = Literal[
    "Africa",
    "Antarctica",
    "Asia",
    "Australia",
    "Europe",
    "North America",
    "South America",
]


class User(BaseModel):
    email: str = Field(title="Email")
    username: str = Field(title="Username")
    favourite_game: str = Field(title="Favourite game")
    continent: Continent = Field(title="Continent")
    extra: str = Field(title="Extra field")


class LayoutOptions(BaseModel):
    layout: Literal["accordion", "tabs", "steps"] = Field(
        default="accordion", json_schema_extra={"repr_type": "RadioItems", "repr_kwargs": {"orientation": "vertical"}}
    )
    remaining_fields_position: Literal["top", "bottom", "none"] = Field(
        default="top", json_schema_extra={"repr_type": "RadioItems", "repr_kwargs": {"orientation": "vertical"}}
    )


def create_form(options: LayoutOptions, item: User | None = None):
    return ModelForm(
        item or User,
        "new_user",
        "renders",
        form_layout=FormLayout.load(
            sections=[
                FormSection(
                    name="General",
                    fields=["email", "username"],
                    default_open=True,
                    icon="carbon:user",
                ),
                FormSection(
                    name="Detail",
                    fields=["favourite_game", "continent"],
                    default_open=True,
                    icon="carbon:settings",
                ),
            ],
            remaining_fields_position=options.remaining_fields_position,
            layout=options.layout,
        ),
    )


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(LayoutOptions()),
            id="intro-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        dmc.Stack(
            [
                options_form := ModelForm(
                    LayoutOptions,
                    aio_id="layout",
                    form_id="interactive-layout",
                    debounce_inputs=250,
                ),
            ],
        ),
    ],
    cols={"base": 1, "sm": 4},
    spacing="2rem",
)


@callback(
    Output("intro-wrapper", "children"),
    Input(options_form.ids.main, "data"),
    State(ModelForm.ids.main("new_user", "renders"), "data"),
    prevent_initial_call=True,
)
def update_form(layout_options: dict, form_data: dict):
    options = LayoutOptions(**layout_options)
    item = model_construct_recursive(form_data, User)
    return create_form(options, item)
