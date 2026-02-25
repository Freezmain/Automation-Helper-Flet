from utils.style import *
from typing import Callable

class Navigation_button:
    def __init__(self, text: str, icon):
        self.button = ft.Button(
            content=text,
            icon=icon,
            width=220,
            style=ft.ButtonStyle(
                alignment=ft.Alignment.CENTER_LEFT
            )
        )

def ButtonWithIcon(text: str, icon: ft.Icon, style: dict, width: int, height: int, function: Callable):
    return ft.FilledButton(text=text, icon=icon, style=ft.ButtonStyle(**style),
                           width=width, height=height,
                           on_click=lambda e: function())

def Button(text: str, style: dict, width: int, height: int, function: Callable):
    return ft.FilledButton(text=text, style=ft.ButtonStyle(**style),
                           width=width, height=height, 
                           on_click=lambda e: function())