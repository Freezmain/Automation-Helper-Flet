import flet as ft

from components.buttons import *
from components.texts import *
from utils.style import *

# НАВІГАЦІЙНЕ МЕНЮ
class NavBar:
    def __init__(self, page: ft.Page, style: dict):
        self.page = page
        self.navBar = ft.Container(
            ft.Column(
                controls=[
                    # Header навігаційного меню
                    ft.Container(
                        content = ft.Row(
                            controls=[
                                IconButton_Close(ft.Icons.CLOSE, Button_close_style, self.toggle_visible),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        padding = ft.padding.only(right = style.get('padding-right')),
                    ),
                    # Кнопки навігаційного меню
                    ft.Column(
                        controls=[
                            Button_NavBar("Головна", ft.Icons.HOME_ROUNDED, Button_navBar_style, self.open_home),
                            Button_NavBar("Розрахунок", ft.Icons.CALCULATE_ROUNDED, Button_navBar_style, self.open_calculation),
                            Button_NavBar("Проєктування", ft.Icons.ARCHITECTURE, Button_navBar_style, self.open_designing),
                            Button_NavBar("Інсталяція", ft.Icons.BUILD_ROUNDED, Button_navBar_style, self.open_installation),
                            Button_NavBar("Налаштування", ft.Icons.SETTINGS_ROUNDED, Button_navBar_style, self.open_settings),
                        ],
                        spacing = style.get('spacing'),
                    )
                ],
            ),
            height = style.get('height'),
            width = style.get('width'),
            bgcolor = style.get('bgcolor'),
            padding = style.get('padding'),
            visible = False
        )

    # Перемикання видимості навігаційного меню
    def toggle_visible(self, e = None):
        self.navBar.visible = not self.navBar.visible
    
    # Перемикання сторінки на home
    async def open_home(self, e):
        await self.page.push_route("/")
        self.toggle_visible()

    # Перемикання сторінки на calculation
    async def open_calculation(self, e):
        await self.page.push_route("/calculation")
        self.toggle_visible()
    
    # Перемикання сторінки на designing
    async def open_designing(self, e):
        await self.page.push_route("/designing")
        self.toggle_visible()
    
    # Перемикання сторінки на installation
    async def open_installation(self, e):
        await self.page.push_route("/installation")
        self.toggle_visible()
    
    # Перемикання сторінки на settings
    async def open_settings(self, e):
        await self.page.push_route("/settings")
        self.toggle_visible()
    
    # Повернення навігаційного меню
    def Get_NavBar(self):
        return self.navBar