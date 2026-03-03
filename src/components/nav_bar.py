import flet as ft

from components.buttons import *
from utils.style import *

class NavBar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.navBar = ft.Container(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(value="Навігаційне меню"),
                            IconButton(ft.Icons.CLOSE, Button_close, self.toggle_visible),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        
                    ),
                    ft.Column(
                        controls=[
                            Button("Головна", ft.Icons.HOME_ROUNDED, Button_navBar, self.open_home),
                            Button("Розрахунок", ft.Icons.CALCULATE_ROUNDED, Button_navBar, self.open_calculation),
                            Button("Проєктування", ft.Icons.ARCHITECTURE, Button_navBar, self.open_designing),
                            Button("Інсталяція", ft.Icons.BUILD_ROUNDED, Button_navBar, self.open_installation),
                            Button("Налаштування", ft.Icons.SETTINGS_ROUNDED, Button_navBar, self.open_settings),
                        ],
                        spacing = 1
                    )
                ],
                height = navBarHeight,
                width = navBarWidth,
            ),
            bgcolor = navBarBgColor,
        )

    def toggle_visible(self, e):
        self.navBar.visible = not self.navBar.visible
    
    async def open_home(self, e):
        await self.page.push_route("/")

    async def open_calculation(self, e):
        await self.page.push_route("/calculation")
    
    async def open_designing(self, e):
        await self.page.push_route("/designing")
        
    async def open_installation(self, e):
        await self.page.push_route("/installation")
    
    async def open_settings(self, e):
        await self.page.push_route("/settings")
    
    def Get_NavBar(self):
        return self.navBar