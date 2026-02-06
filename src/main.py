import flet as ft
import components.buttons

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window_height = 1280
    page.window_width = 720

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
        icon=ft.Icons.MENU
    )

    navigation_button_menu = ft.Button(
        content="Головне меню",
        icon=ft.Icons.LIBRARY_BOOKS_ROUNDED,
        width=220,
        style=ft.ButtonStyle(
            alignment=ft.Alignment.CENTER_LEFT
        )
    )

    navigation_button_calculating = ft.Button(
        content="Розрахунок модулів",
        icon=ft.Icons.CALCULATE_OUTLINED,
        width=220,
        style=ft.ButtonStyle(
            alignment=ft.Alignment.CENTER_LEFT
        )
    )

    navigation_button_settings = ft.Button(
        content="Налаштування",
        icon=ft.Icons.SETTINGS_ROUNDED,
        width=220,
        style=ft.ButtonStyle(
            alignment=ft.Alignment.CENTER_LEFT
        )
    )

    stack = ft.Stack(
        [
            ft.Container(
                ft.Row(
                    controls=[
                        navigation_button_open,
                        app_title
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            ),

            ft.Container(
                ft.Column(
                    controls=[
                        navigation_title,
                        navigation_button_menu,
                        navigation_button_calculating,
                        navigation_button_settings
                    ]
                ),
                bgcolor=ft.Colors.GREY_900,
                padding=10,
                expand=True
            )
        ],
        expand=True
    )

    page.add(
        stack
    )

    page.update()

ft.app(target=main)