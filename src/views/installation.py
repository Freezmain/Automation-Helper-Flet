import flet as ft

from components.nav_bar import NavBar

class View_installation():
    def __init__(self, page: ft.Page):
        self.navBar = NavBar(page)
    
    def Get_InstallationView(self):
        return ft.View(
            route="/installation",
            controls=[
                #----Шари відображення----
                ft.Stack(
                    controls=[
                        ft.Container(
                            ft.Text("Installation")
                        ),
                        self.navBar.Get_NavBar(),
                    ]
                )
            ],
            padding = 0
        )