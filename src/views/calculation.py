import flet as ft

from components.nav_bar import NavBar

class View_calculation():
    def __init__(self, page: ft.Page):
        self.navBar = NavBar(page)

    def Get_CalculationView(self):
        return ft.View(
            route="/calculation",
            controls=[
                #----Шари відображення----
                ft.Stack(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.IconButton(icon=ft.Icons.MENU),
                                        ft.Text(value="SVIT Helper")
                                    ]  
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Button(icon=ft.Icons.LIGHTBULB_OUTLINE, content="Світло"),
                                        ft.Button(icon=ft.Icons.LIGHTBULB_OUTLINE, content="Механізми"),
                                        ft.Button(icon=ft.Icons.LIGHTBULB_OUTLINE, content="Датчики"),
                                        ft.Button(icon=ft.Icons.LIGHTBULB_OUTLINE, content="Клавіші")
                                    ]
                                )
                            ]
                        ),
                        self.navBar.Get_NavBar(),
                    ]
                )
            ],
            padding = 0
        )