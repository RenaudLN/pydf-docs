import json

import dash_mantine_components as dmc
from dash import Input, Output, callback
from dash_pydantic_form import ModelForm
from dash_pydantic_form.quantity import Quantity
from pydantic import BaseModel, Field

default_repr_kwargs = {"decimalScale": 2, "thousandSeparator": ","}


class Room(BaseModel):
    """Room model."""

    area: Quantity = Field(repr_type="Quantity", repr_kwargs={"unit_options": ["m^2", "ft^2"], **default_repr_kwargs})
    height: Quantity = Field(
        repr_type="Quantity", repr_kwargs={"unit_options": ["m", "cm", "ft", "in"], **default_repr_kwargs}
    )
    temperature: Quantity = Field(repr_type="Quantity", repr_kwargs={"unit_options": ["C", "F"], **default_repr_kwargs})
    light_bulb_power: Quantity = Field(
        repr_type="Quantity",
        repr_kwargs={"unit_options": ["W"], **default_repr_kwargs},
    )


component = dmc.Stack(
    [
        ModelForm(Room, "quantity", "basic"),
        dmc.Box(id="quantity-basic-output"),
    ]
)


@callback(
    Output("quantity-basic-output", "children"),
    Input(ModelForm.ids.main("quantity", "basic"), "data"),
)
def show_data(form_data: dict):
    return json.dumps(form_data)
