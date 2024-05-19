import dash_mantine_components as dmc
from dash_iconify import DashIconify

excluded_links = [
    "/404",
    "/getting-started",
    "/styles-api",
    "/style-props",
    "/dash-iconify",
    "/",
    "/migration",
]

category_data = {
    "API": {"icon": "material-symbols:trackpad-input-rounded"},
}

def create_content(data):

    body = []
    for entry in data:
        if entry["path"] not in excluded_links:
            link = dmc.Anchor(
                [DashIconify(icon=entry["icon"], height=20), entry["name"]],
                href=entry["path"],
                className="navbar-link",
            )
            body.append(link)

    return dmc.ScrollArea(
        offsetScrollbars=True,
        type="scroll",
        style={"height": "100%"},
        children=dmc.Stack(gap=0, children=[
            dmc.Anchor([DashIconify(icon="fluent:star-24-regular", height=20), "Introduction"], href="/", className="navbar-link",),
            dmc.Divider(label="Components", mt="2rem", mb="1rem", labelPosition="left", pl="1rem"),
            *body
        ], px="1rem", py="2rem"),
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
