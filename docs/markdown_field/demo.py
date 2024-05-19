from dash_pydantic_form import ModelForm, fields
from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str = Field(title="Project name")
    description: str = Field(title="Description")


bob = Project(
    name="Flying to Paris",
    description=(
        "### Act 1\n\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam mollis dui quam, eget aliquam sem bibendum a. "
        "Praesent et sapien et nibh blandit facilisis id eget orci. Donec in ligula eget augue efficitur elementum. "
        "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; "
        "Aenean vel molestie ligula, sit amet euismod lorem. Proin lobortis ipsum odio, et tempor quam suscipit eget."
        "\n\n### Requirements\n\n"
        "* Passport\n"
        "* Toothbrush"
    ),
)

component = ModelForm(bob, "user", "table1", fields_repr={"description": fields.Markdown()})
