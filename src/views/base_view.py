import flet as ft

from components.nav_bar import NavBar
from components.buttons import *
from components.texts import *
from utils.style import *

class BaseView:
    def __init__(self, page: ft.Page, route: str):
        self.page = page
        self.route = route
        self.navBar = NavBar(page, NavBar_style)

    def get_content(self) -> list[ft.Control]:
        return []

    def build(self):
        return ft.View(
            route = self.route,
            controls=[
                ft.Stack(
                    controls=[
                        # Контент конкретної сторінки
                        ft.Container(
                            content = ft.Column(
                                controls = [
                                    ft.Row(
                                        controls=[
                                            ft.IconButton(icon=ft.Icons.MENU, on_click = self.navBar.toggle_visible),
                                            Text("SVIT Helper", TextTitle_style)
                                        ]
                                    ),
                                    *self.get_content(),
                                ]
                            ),
                            padding = 20
                        ),
                        # Спільний NavBar поверх всього
                        self.navBar.Get_NavBar(),
                    ]
                )
            ],
            padding = 0,
        )