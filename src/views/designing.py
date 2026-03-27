import flet as ft

from views.base_view import BaseView

# КОНФІГУРАТОР ПРОЄКТУ
class View_designing(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page, route="/designing")

    def get_content(self):
        return [
            ft.Container(
                content=ft.Text("Designing"),
                padding=20
            )
        ]