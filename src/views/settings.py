import flet as ft

from views.base_view import BaseView

class View_settings(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page, route="/settings")

    def get_content(self):
        return [
            ft.Container(
                content=ft.Text("Settings"),
                padding=20
            )
        ]