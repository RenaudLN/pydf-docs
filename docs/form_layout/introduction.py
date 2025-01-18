from typing import Literal

from dash_pydantic_form import AccordionFormLayout, FormSection, ModelForm
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


component = ModelForm(
    User,
    "new_user",
    "sections",
    form_layout=AccordionFormLayout(
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
    ),
)
