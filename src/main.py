import flet as ft

from router import *
from utils.style import *

def main(page: ft.Page):
    page.title = "SVIT Helper"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = pageBgColor
    page.height = pageHeight
    page.width = pageWidth

    Router(page).start_routing()

ft.run(main)