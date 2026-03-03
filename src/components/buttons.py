from utils.style import *
from typing import Callable

def Button(text: str, icon: ft.Icon, style: dict, function: Callable):
    return ft.Button(content = text, icon = icon, height = 60, width = 198, style = ft.ButtonStyle(**style), on_click = lambda e: function())

def IconButton(icon: ft.Icon, style: dict, function: Callable):
    return ft.IconButton(icon = icon, height = 30, width = 30, style = ft.ButtonStyle(**style), on_click = lambda e: function())