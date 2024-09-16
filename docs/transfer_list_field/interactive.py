from functools import lru_cache
from typing import Literal

import dash_mantine_components as dmc
import pandas as pd
from dash import Input, Output, State, callback
from dash_pydantic_form import ModelForm, fields
from dash_pydantic_form.utils import model_construct_recursive
from pydantic import BaseModel, Field


@lru_cache
def _get_cities():
    return (
        pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv")[["name"]]
        .drop_duplicates()
        .assign(name=lambda df: df["name"].str.strip())
    )


def get_cities(search: str, max_items: int | None):
    cities = _get_cities()
    if search:
        cities = cities[cities["name"].str.contains(search, case=False, regex=False)]
    if max_items:
        cities = cities.head(max_items)
    return cities["name"].to_list()


fields.TransferList.register_data_getter(get_cities, "cities")


class Travels(BaseModel):
    cities: list[str] = Field(title="Cities visited", default_factory=list)


class Options(BaseModel):
    placeholder: str = Field(title="Placeholder", default="No cities")
    search_placeholder: str = Field(title="Search placeholder", default="Search cities")
    nothing_found: str = Field(title="Nothing found", default="No city match your search")
    show_transfer_all: bool = Field(title="Show 'Transfer all'", default=True)
    list_height: int = Field(title="List height", default=200)
    max_items: int = Field(title="Max items", default=25)
    radius: Literal["xs", "sm", "md", "lg", "xl"] = Field(title="Border radius", default="sm")


def create_form(
    travels: Travels | None = None,
    **options,
):
    travels = travels or Travels()
    options = options or Options().model_dump(mode="json")
    return ModelForm(
        travels,
        "travels",
        "interactive-transferlist",
        fields_repr={"cities": fields.TransferList(data_getter="cities", **options)},
    )


component = dmc.SimpleGrid(
    [
        dmc.Paper(
            create_form(),
            id="interactive4-wrapper",
            style={"gridColumn": "1 / 4"},
        ),
        ModelForm(
            Options,
            aio_id="transfer-list",
            form_id="interactive-options",
            fields_repr={
                "list_height": fields.Slider(input_kwargs={"min": 150, "max": 400, "step": 50}),
                "max_items": fields.Slider(input_kwargs={"min": 5, "max": 50, "step": 5}),
                "radius": fields.SegmentedControl(),
            },
            debounce_inputs=300,
        ),
    ],
    cols=4,
    spacing="2rem",
)


@callback(
    Output("interactive4-wrapper", "children"),
    Input(ModelForm.ids.main("transfer-list", "interactive-options"), "data"),
    State(ModelForm.ids.main("travels", "interactive-transferlist"), "data"),
    prevent_initial_call=True,
)
def update_form(options_data: dict, form_data: dict):
    item = model_construct_recursive(form_data, Travels)
    return create_form(travels=item, **options_data)
