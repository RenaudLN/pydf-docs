from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field

email_regex = r"^\S+@\S+\.\S+$"


class LoginData(BaseModel):
    email: str = Field(
        title="Email",
        description="Work email only, no gmail allowed",
        pattern=email_regex,
        # Add repr_kwargs to add default field arguments
        json_schema_extra={"repr_kwargs": {"placeholder": "abc@email.com"}},
    )
    password: str = Field(
        title="Password",
        description="Make it strong",
        min_length=6,
        # Add repr_type to change the default field type
        json_schema_extra={"repr_type": "Password"},
    )


component = ModelForm(LoginData, "login", "custom_in_model")
