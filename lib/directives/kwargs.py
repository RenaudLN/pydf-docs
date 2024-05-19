import importlib
import inspect

import dash_mantine_components as dmc
from dash.development.base_component import Component
from markdown2dash.src.directives.kwargs import Kwargs as KwargsBase

def convert_docstring_to_dict(docstring):
    """Convert numpy style parameter docstring to a list of dicts with keys name, type, description"""

    lines: list[str] = docstring.split("----------\n")[-1].split("\n")

    params = []
    new_param = None
    for line in lines:
        if not line.startswith("    "):
            if new_param is not None:
                params.append(new_param)
            name, type = line.split(": ", 1)
            new_param = {"name": name, "type": type, "description": ""}
        else:
            new_param["description"] += " " + line.strip()
    params.append(new_param)

    return params

class Kwargs(KwargsBase):

    def hook(self, md, state):
        sections = []

        for tok in state.tokens:
            if tok["type"] == self.block_name:
                sections.append(tok)

        for section in sections:
            attrs = section["attrs"]
            package = attrs.pop("library", "dash_pydantic_form")
            component_name = attrs["title"]
            imported = importlib.import_module(package)
            component = getattr(imported, component_name)
            docstring = inspect.getdoc(component).split("----------\n")[-1]
            attrs["kwargs"] = convert_docstring_to_dict(docstring)

    def render(self, renderer, title: str, content: str, **options) -> Component:
        data = options.pop("kwargs")
        if data:
            kwargs = dmc.Stack(
                [
                    dmc.Stack(
                        [
                            dmc.Group(
                                [
                                    dmc.Text(dmc.Code(arg["name"], style={"fontSize": "inherit"}), fw=600),
                                    dmc.Text(
                                        dmc.CodeHighlight(
                                            arg["type"],
                                            styles={"pre": {"fontSize": "inherit", "padding": "0 0.5rem"}, "root": {"borderRadius": "0.25rem"}},
                                            language="py",
                                            withCopyButton=False,
                                            py=0,
                                        ),
                                        c="dimmed",
                                        size="sm",
                                    ),
                                ],
                                gap="0.5rem",
                            ),
                            dmc.Text(arg["description"], size="sm"),
                        ],
                        gap="0.5rem",
                    )
                    for arg in data
                ],
                gap="1.25rem",
                pl="1.25rem",
            )
        else:
            kwargs = None
        return kwargs