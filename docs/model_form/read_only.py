from typing import Literal

from dash_pydantic_form import ModelForm, fields
from pydantic import BaseModel, Field


class Metadata(BaseModel):
    param1: str
    param2: str | None = None
    param_english: str | None = None


class User(BaseModel):
    username: str = Field(title="Username")
    country: Literal["us", "fr", "uk"] = Field(title="Country")
    likes_baguettes: bool = Field(title="Likes baguettes", default=False)
    metadata: Metadata = Field(title="Metadata")
    bonus: str


bob = User(
    username="Bob",
    country="fr",
    likes_baguettes=True,
    metadata=Metadata(
        param1="value1",
    ),
    bonus="Yay 🎉",
)


component = ModelForm(
    bob,
    "user_form",
    "read_only",
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
            "visible": [("country", "==", "fr"), ("username", "==", "Bob")],
        },
    },
    read_only=True,
)
