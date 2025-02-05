import json

import dash_mantine_components as dmc
from dash import Input, Output, callback
from dash_pydantic_form import ModelForm
from dash_pydantic_utils import Quantity
from pydantic import BaseModel, Field

default_repr_kwargs = {"decimalScale": 2, "thousandSeparator": ","}


class Room(BaseModel):
    """Room model."""

    area: Quantity = Field(
        repr_type="Quantity", repr_kwargs={"unit_options": {"m^2": "m²", "ft^2": "sqft"}, **default_repr_kwargs}
    )
    height: Quantity = Field(
        repr_type="Quantity", repr_kwargs={"unit_options": ["m", "cm", "ft", "in"], **default_repr_kwargs}
    )
    temperature: Quantity = Field(
        repr_type="Quantity", repr_kwargs={"unit_options": {"C": "°C", "F": "°F"}, **default_repr_kwargs}
    )
    light_bulb_power: Quantity = Field(
        repr_type="Quantity", repr_kwargs={"unit_options": {"W": "Watt"}, **default_repr_kwargs}
    )


component = dmc.Stack(
    [
        ModelForm(Room, "quantity", "basic"),
        dmc.Code(id="quantity-basic-output", style={"whiteSpace": "pre"}),
    ]
)


@callback(
    Output("quantity-basic-output", "children"),
    Input(ModelForm.ids.main("quantity", "basic"), "data"),
)
def show_data(form_data: dict):
    indented = json.dumps({k: f"<{k}>" for k in form_data}, indent=4)
    for k, v in form_data.items():
        indented = indented.replace(f'"<{k}>"', json.dumps(v))
    return indented
