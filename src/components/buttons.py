from utils.style import *
from typing import Callable

def Button_NavBar(text: str, icon: ft.Icon, style: dict, function: Callable):
    return ft.Button(
        content = ft.Container(
            ft.Row(
                controls=[
                    ft.Icon(icon = icon, size = style.get('icon_size')),
                    ft.Text(value = text, size = style.get('text_size')),
                ],
                alignment = style.get('alignment'),
                spacing = style.get('spacing'),
            ),
            padding = ft.padding.only(style.get('padding-left'))
        ),
        style = ft.ButtonStyle(
            shape = style.get('shape')
        ),
        bgcolor = style.get('bgcolor'),
        color = style.get('color'),
        elevation = style.get('elevation'),
        height = style.get('height'),
        width = style.get('width'),
        on_click = function,
    )

def Button_CalculationBar(text: str, icon: ft.Icon, style: dict):
    return ft.Button(
        content = ft.Row(
            controls = [
                ft.Icon(icon = icon, size = style.get('icon_size')),
                ft.Text(value = text, size = style.get('text_size')),
            ],
            alignment = style.get('alignment'),
        ),
        style = ft.ButtonStyle(
            shape = style.get('shape'),
        ),
        color = style.get('color'),
        height = style.get('height'),
        width = style.get('width'),
    )

def IconButton_Close(icon: ft.Icon, style: dict, function: Callable):
    return ft.IconButton(
        style = ft.ButtonStyle(
            overlay_color=ft.Colors.TRANSPARENT,
            shape = style.get('shape'),
        ),
        icon_size = style.get('icon_size'),
        bgcolor = style.get('bgcolor'),
        height = style.get('height'),
        width = style.get('width'),
        icon = icon,
        on_click = function,
        )
