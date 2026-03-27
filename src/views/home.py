import flet as ft

from views.base_view import BaseView

# ГОЛОВНА СТОРІНКА
class View_home(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page, route="/")

    def get_content(self):
        return [
            ft.Container(
                content=ft.Text("Home"),
                padding=20
            )
        ]