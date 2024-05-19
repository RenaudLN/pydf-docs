from dash_pydantic_form import ModelForm, fields
from pydantic import BaseModel, Field

email_regex = r'^\S+@\S+\.\S+$'
class LoginData(BaseModel):
    email: str = Field(
        title="Email",
        description="Work email only, no gmail allowed",
        pattern=email_regex,
    )
    password: str = Field(
        title="Password",
        description="Make it strong",
        min_length=6
    )

component = ModelForm(
    LoginData,
    "login",
    "custom",
    fields_repr={
        # Using a dict will pass the arguments to the default field input
        "email": {"input_kwargs": {"placeholder": "abc@email.com"}},
        # You can also pass the field repr directly
        "password": fields.Password(),
    }
)
