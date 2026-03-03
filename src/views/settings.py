import flet as ft

from components.nav_bar import NavBar

class View_settings():
    def __init__(self, page: ft.Page):
        self.navBar = NavBar(page)
    
    def Get_SettingsView(self):
        return ft.View(
            route="/settings",
            controls=[
                #----Шари відображення----
                ft.Stack(
                    controls=[
                        ft.Container(
                            ft.Text("Settings")
                        ),
                        self.navBar.Get_NavBar(),
                    ]
                )
            ],
            padding = 0
        )