from textual.app import App, ComposeResult
from textual import on
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Button, LoadingIndicator, RichLog
from gi.repository import Gio


class Sidebar(Vertical):
    def compose(self) -> ComposeResult:
        yield Button(
            label="Show Schemas",
            id="show_schemas",
        )


class TuiApp(App):

    CSS_PATH = "tui.tcss"

    def show_loading(self):
        yield LoadingIndicator("Loading...")

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Sidebar(id="sidebar")
            yield RichLog(
                highlight=True,
                wrap=False,
                markup=True,
            )
        yield Footer()

    @on(Button.Pressed, "#show_schemas")
    def show_schemas(self):
        schemas = Gio.Settings.list_schemas()
        self.query_one(RichLog).write(schemas)
