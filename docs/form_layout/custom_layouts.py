# ruff: noqa
from typing import Any, Literal

import dash_mantine_components as dmc
from dash_pydantic_form import FormLayout, ModelForm
from pydantic import BaseModel, Field


class Pet(BaseModel):
    name: str
    species: str


class Person(BaseModel):
    name: str
    age: int
    pets: list[Pet] = Field(default_factory=list)


class PetsHighlightLayout(FormLayout):
    layout: Literal["pets-highlight"] = "pets-highlight"
    color: str = "red"

    def render(
        self,
        *,
        field_inputs: dict[str, Any],
        aio_id: str,  # If you need to add matching ids to the layout
        form_id: str,  # If you need to add matching ids to the layout
        path: str,  # If you need to add matching ids to the layout
        read_only: bool,  # If you need a different behavior in read-only mode
        form_cols: int,  # If you need to match the number of columns in the form
    ) -> list:
        """Render the User form, highlighting the pets fields."""
        # All the non pets fields are displayed in the default `grid`,
        # which is a responsive grid matching the form columns
        base = self.grid([inp for field, inp in field_inputs.items() if field != "pets"])
        # For pets we wrap them in a box with a border
        pets_highlighted = dmc.Box(
            field_inputs["pets"],
            bd=f"2px solid {self.color}",
            px="md",
            py="sm",
        )
        return [dmc.Stack([base, pets_highlighted])]


component = ModelForm(Person, "custom-layout", "pets-highlight", form_layout=PetsHighlightLayout(color="orange"))
