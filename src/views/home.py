import flet as ft

from components.nav_bar import NavBar

class View_home():
    def __init__(self, page: ft.Page):
        self.navBar = NavBar(page)
        
    def Get_HomeView(self):
        return ft.View(
            route="/",
            controls=[
                #----Шари відображення----
                ft.Stack(
                    controls=[
                        ft.Container(
                            ft.Text("Home")
                        ),
                        self.navBar.Get_NavBar(),
                    ]
                )
            ],
            padding = 0
        )