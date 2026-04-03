import flet as ft

from router import *
from utils.style import *

# ОСНОВА ДОДАТКУ
def main(page: ft.Page):
    # Основні налаштування додатку
    page.title = "SVIT Helper"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = Page_style.get('height')
    page.window.width = Page_style.get('width')

    # Навігація по сторінкам додатку
    Router(page).start_routing()

ft.run(main)