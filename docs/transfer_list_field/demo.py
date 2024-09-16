from functools import lru_cache

import pandas as pd
from dash_pydantic_form import ModelForm, fields
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
    cities: list[str] = Field(title="Cities visited")


component = ModelForm(
    Travels,
    "user",
    "list1",
    fields_repr={
        "cities": fields.TransferList(
            data_getter="cities",
            show_transfer_all=True,
            placeholder="No cities",
            search_placeholder="Search cities",
            nothing_found="No city match your search",
            max_items=25,
        ),
    },
)
