import dash_mantine_components as dmc
from dash import Input, Output, State, callback, html
from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field, ValidationError

email_regex = r"^\S+@\S+\.\S+$"


class LoginData(BaseModel):
    email: str = Field(
        title="Email",
        description="Work email only, no gmail allowed",
        pattern=email_regex,
    )
    password: str = Field(title="Password", description="Make it strong", min_length=6)


component = dmc.Stack(
    [
        ModelForm(LoginData, "login", "auto", submit_on_enter=True),
        html.Div(dmc.Button("Submit", id="submit", mt=-10)),
        html.Div(id="output"),
    ]
)


@callback(
    Output("output", "children"),
    Input("submit", "n_clicks"),
    Input(ModelForm.ids.form("login", "auto"), "data-submit"),
    State(ModelForm.ids.main("login", "auto"), "data"),
    prevent_initial_call=True,
)
def check_form(_trigger: int, _trigger2: int, form_data: dict):
    try:
        LoginData.model_validate(form_data)
    except ValidationError as exc:
        return [
            dmc.Text("Validation errors", fw=500, c="red"),
            dmc.List(
                [
                    dmc.ListItem(
                        [
                            ".".join([str(x) for x in error["loc"]]),
                            f" : {error['msg']}, got {error['input']}",
                        ],
                    )
                    for error in exc.errors()
                ],
                size="sm",
                c="red",
            ),
        ]

    return dmc.Text("Form is valid", c="green")
