import flet as ft

class Navigation_button:
    def __init__(self, text, icon):
        self.button = ft.Button(
            content=text,
            icon=icon,
            width=220,
            style=ft.ButtonStyle(
                alignment=ft.Alignment.CENTER_LEFT
            )
        )