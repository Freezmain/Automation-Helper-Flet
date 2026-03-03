import flet as ft

from components.nav_bar import NavBar

class View_designing():
    def __init__(self, page: ft.Page):
        self.navBar = NavBar(page)
    
    def Get_DesigningView(self):
        return ft.View(
            route="/designing",
            controls=[
                #----Шари відображення----
                ft.Stack(
                    controls=[
                        ft.Container(
                            ft.Text("Designing")
                        ),
                        self.navBar.Get_NavBar(),
                    ]
                )
            ],
            padding = 0
        )