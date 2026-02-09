import flet as ft
from components.app_buttons import *

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "SVIT Helper"
    page.padding = 0
    page.window_height = 1280
    page.window_width = 720

    def navigation_visible_toggle():
        navigation_panel.visible = not navigation_panel.visible
        page.update()
    
    app_title = ft.Text(
        value="SVIT Helper",
        size=30,
        weight=ft.FontWeight.W_600,
        color="white"
    )

    navigation_title = ft.Text(
        value="Навігація",
        size=25,
        weight=ft.FontWeight.W_400,
        color="white"
    )

    navigation_button_open = ft.Button(
        content="Меню",
        icon=ft.Icons.MENU,
        on_click=navigation_visible_toggle
    )

    #----Кнопки навігації----
    navigation_menu = Navigation_button("Головне меню", ft.Icons.LIBRARY_BOOKS_ROUNDED)
    navigation_calculating = Navigation_button("Розрахунок модулів", ft.Icons.CALCULATE_OUTLINED)
    navigation_settings = Navigation_button("Налаштування", ft.Icons.SETTINGS_ROUNDED)

    #----Навігаційна панель----
    navigation_panel = ft.Container(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        navigation_button_open,
                        navigation_title,
                    ]
                ),
                navigation_menu.button,
                navigation_calculating.button,
                navigation_settings.button
            ]
        ),
        bgcolor=ft.Colors.GREY_900,
        padding=10,
        width=260,
        expand=True,
        visible=False
    )

    #----Основна частина апки----
    stack = ft.Stack(
        [
            ft.Container(
                ft.Row(
                    controls=[
                        navigation_button_open,
                        app_title
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                padding=10
            ),

            navigation_panel
        ],
        expand=True
    )

    page.add(
        stack
    )

    page.update()

ft.app(target=main)