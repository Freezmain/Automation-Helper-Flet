import flet as ft

from components.nav_bar import NavBar
from components.buttons import *
from components.texts import *
from utils.style import *

# ШАБЛОН СТОРІНОК ДОДАТКУ
class BaseView:
    def __init__(self, page: ft.Page, route: str):
        self.page = page
        self.route = route
        self.navBar = NavBar(page, NavBar_style)

    # Універсальний метод повернення вмісту дочірніх класів
    def get_content(self) -> list[ft.Control]:
        return []

    # Метод повернення вмісту сторінки
    def build(self):
        return ft.View(
            route = self.route,
            controls=[
                ft.Stack(
                    controls=[
                        ft.Container(
                            content = ft.Column(
                                controls = [
                                    # Спільний header для сторінок
                                    ft.Row(
                                        controls=[
                                            ft.IconButton(icon=ft.Icons.MENU, on_click = self.navBar.toggle_visible),
                                            Text("SVIT Helper", TextTitle_style)
                                        ]
                                    ),
                                    # Контент конкретної сторінки
                                    *self.get_content(),
                                ]
                            ),
                            padding = 20
                        ),
                        # Спільний NavBar для сторінок (поверх інших елементів)
                        self.navBar.Get_NavBar(),
                    ]
                )
            ],
            padding = 0,
        )