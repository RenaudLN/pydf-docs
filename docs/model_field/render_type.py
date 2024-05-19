import dash_mantine_components as dmc
from dash import Input, Output, State, callback
from dash_pydantic_form import ModelForm
from dash_pydantic_form.utils import model_construct_recursive
from pydantic import BaseModel, Field

BASE_RENDER = "accordion"


class Stats(BaseModel):
    wins: int = Field(title="Wins")
    losses: int = Field(title="Losses")
    draws: int = Field(title="Draws")


class User(BaseModel):
    username: str = Field(title="Username")
    stats: Stats = Field(title="Stats")


def create_form(render: str = BASE_RENDER, item: User | None = None):
    return ModelForm(
        item if item is not None else User,
        "user",
        "renders",
        fields_repr={
            "stats": {"render_type": render},
        },
    )


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(BASE_RENDER),
            id="interactive-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        dmc.Stack(
            [
                dmc.RadioGroup(
                    label="Sections render",
                    id="interactive-render",
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
    Output("interactive-wrapper", "children"),
    Input("interactive-render", "value"),
    State(ModelForm.ids.main("user", "renders"), "data"),
    prevent_initial_call=True,
)
def update_form(render: str, form_data: dict):
    item = model_construct_recursive(form_data, User)
    return create_form(render, item)
