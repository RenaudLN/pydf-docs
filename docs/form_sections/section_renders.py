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

BASE_RENDER = "accordion"


class User(BaseModel):
    email: str = Field(title="Email")
    username: str = Field(title="Username")
    favourite_game: str = Field(title="Favourite game")
    continent: Continent = Field(title="Continent")


def create_form(render: str = BASE_RENDER, item: User | None = None):
    return ModelForm(
        item or User,
        "new_user",
        "renders",
        sections=Sections(
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
            remaining_fields_position="top",
            render=render,
        ),
    )


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(BASE_RENDER),
            id="intro-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        dmc.Stack(
            [
                dmc.RadioGroup(
                    label="Sections render",
                    id="intro-render",
                    value=BASE_RENDER,
                    children=dmc.Stack(
                        [dmc.Radio(label=x, value=x) for x in ["accordion", "tabs", "steps"]],
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
    Output("intro-wrapper", "children"),
    Input("intro-render", "value"),
    State(ModelForm.ids.main("new_user", "renders"), "data"),
    prevent_initial_call=True,
)
def update_form(render: str, form_data: dict):
    item = model_construct_recursive(form_data, User)
    return create_form(render, item)
