from dash_pydantic_form import ModelForm, fields
from pydantic import BaseModel, Field

BASE_RENDER = "accordion"


class Stats(BaseModel):
    wins: int = Field(title="Wins")
    losses: int = Field(title="Losses")
    draws: int = Field(title="Draws")


class User(BaseModel):
    username: str = Field(title="Username")
    stats: Stats = Field(title="Stats")


component = ModelForm(
    User,
    "user",
    "interactive",
    fields_repr={
        "stats": {
            "fields_repr": {
                "wins": fields.Number(input_kwargs={"placeholder": "Oh yeah!"}),
            },
        },
    },
)
