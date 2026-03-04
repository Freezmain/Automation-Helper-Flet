import flet as ft

from views.base_view import BaseView

class View_installation(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page, route="/installation")

    def get_content(self):
        return [
            ft.Container(
                content=ft.Text("Installation"),
                padding=20
            )
        ]