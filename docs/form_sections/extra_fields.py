from typing import Literal

import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from dash_pydantic_form import FormSection, ModelForm, Sections
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

BASE_POSITION = "top"


class User(BaseModel):
    email: str = Field(title="Email")
    username: str = Field(title="Username")
    favourite_game: str = Field(title="Favourite game")
    continent: Continent = Field(title="Continent")


def create_form(position: str = BASE_POSITION, item: User | None = None):
    return ModelForm(
        item if item is not None else User,
        "new_user",
        "extra_fields",
        sections=Sections(
            sections=[
                FormSection(
                    name="Detail",
                    fields=["favourite_game", "continent"],
                    default_open=True,
                    icon="carbon:settings",
                ),
            ],
            remaining_fields_position=position,
        ),
    )


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(BASE_POSITION),
            id="extra-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        dmc.Stack(
            [
                dmc.RadioGroup(
                    label="Extra fields position",
                    id="extra-position",
                    value=BASE_POSITION,
                    children=dmc.Stack(
                        [dmc.Radio(label=x, value=x) for x in ["top", "bottom", "none"]],
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
    Output("extra-wrapper", "children"),
    Input("extra-position", "value"),
    State(ModelForm.ids.main("new_user", "extra_fields"), "data"),
    prevent_initial_call=True,
)
def update_form(position: str, form_data: dict):
    item = model_construct_recursive(form_data, User)
    return create_form(position, item)
