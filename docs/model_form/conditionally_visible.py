from typing import Literal

from dash_pydantic_form import ModelForm, fields
from pydantic import BaseModel, Field


class Metadata(BaseModel):
    param1: str
    param2: str
    param_english: str | None = None


class User(BaseModel):
    username: str = Field(title="Username")
    country: Literal["us", "fr", "uk"] = Field(title="Country")
    likes_baguettes: bool = Field(title="Likes baguettes", default=False)
    metadata: Metadata | None = None
    bonus: str | None = None


component = ModelForm(
    User,
    "user_form",
    "conditional",
    fields_repr={
        "country": fields.RadioItems(
            options_labels={"us": "USA", "fr": "France", "uk": "UK"},
        ),
        "likes_baguettes": {
            "visible": ("country", "==", "fr"),
        },
        "metadata": {
            "fields_repr": {
                "param_english": {
                    "visible": ("_root_:country", "in", ["uk", "us"]),
                },
            }
        },
        "bonus": {
            "visible": [("country", "==", "uk"), ("username", "==", "Bob")],
        },
    },
)
