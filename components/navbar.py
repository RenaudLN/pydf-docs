import dash_mantine_components as dmc
from dash_iconify import DashIconify

excluded_links = [
    "/404",
    "/",
]

category_data = {
    "API": {"icon": "material-symbols:trackpad-input-rounded"},
}


def create_content(data):
    sections = {
        "form": [],
        "fields": [],
        "examples": [],
    }
    entries = sorted(
        [datum for datum in data if datum["path"] not in excluded_links],
        key=lambda d: d["order"] or 1000,
    )
    for entry in entries:
        link = dmc.Anchor(
            [DashIconify(icon=entry["icon"], height=24), entry["name"]],
            href=entry["path"],
            className="navbar-link",
        )
        if entry.get("section") not in sections:
            raise ValueError(f"Unknown section in {entry['name']}: {entry.get('section')}")

        sections[entry.get("section")].append(link)

    return dmc.ScrollArea(
        offsetScrollbars=True,
        type="scroll",
        style={"height": "100%"},
        children=dmc.Stack(
            gap=0,
            children=[
                dmc.Anchor(
                    [
                        DashIconify(icon="fluent:star-24-regular", height=24),
                        "Introduction",
                    ],
                    href="/",
                    className="navbar-link",
                ),
            ]
            + sum(
                [
                    [
                        dmc.Divider(
                            label=k.title(),
                            mt="2rem",
                            mb="1rem",
                            labelPosition="left",
                            pl="1rem",
                        )
                    ]
                    + v
                    for k, v in sections.items()
                ],
                [],
            ),
            px="1rem",
            py="2rem",
        ),
    )


def create_navbar(data):
    return dmc.AppShellNavbar(children=create_content(data))


def create_navbar_drawer(data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayProps={"opacity": 0.55, "blur": 3},
        zIndex=1500,
        offset=10,
        radius="md",
        withCloseButton=False,
        size="75vw",
        children=create_content(data),
        trapFocus=False,
    )
