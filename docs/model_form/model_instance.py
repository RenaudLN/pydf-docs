from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(title="Email")
    username: str = Field(title="Username")
    favourite_game: str = Field(title="Favourite game")

user1 = User(
    email="user1@example.com",
    username="user1",
    favourite_game="Tetris",
)

component = ModelForm(user1, "user_form", "user1")
