import flet as ft

from router import *
from utils.style import *

def main(page: ft.Page):
    page.title = "SVIT Helper"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = Page_style.get('bgcolor')
    page.window.height = Page_style.get('height')
    page.window.width = Page_style.get('width')

    Router(page).start_routing()

ft.run(main)