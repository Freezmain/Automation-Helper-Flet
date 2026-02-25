from utils.style import *
from components.app_buttons import *
from flet_route import Params, Basket
import flet as ft

class CalculationPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = "SVIT Helper"
        page.theme_mode = ft.ThemeMode.DARK
        page.window_height = pageHeight
        page.window_width = pageWidth

        #----Functions----
        def NavigationPanel_toggle_visible():
            NavigationPanel.visible = not NavigationPanel.visible
            page.update()
        
        def Link_menu():
            pass

        def Link_calculation():
            pass

        def Link_settings():
            pass

        #----Views----
        App_title = ft.Container(
            ft.Text(value='SVIT Helper', **TextTitle_style)
        )

        NavigationPanel_title = ft.Container(
            ft.Text(value='Навігація', **TextSubTitle_style)
        )

        Navigation_button_open = Button('Меню', Button_white, 220, 60, NavigationPanel_toggle_visible)
        Navigation_button_close = Button('X', Button_white, 60, 60, NavigationPanel_toggle_visible)

        NavigationPanel_button_menu = ButtonWithIcon('Головне меню', ft.Icons.LIBRARY_BOOKS_ROUNDED, Button_white, 280, 70, Link_menu)
        NavigationPanel_button_calculation = ButtonWithIcon('Розрахунок модулів', ft.Icons.CALCULATE_OUTLINED, Button_white, 280, 70, Link_calculation)
        NavigationPanel_button_settings = ButtonWithIcon('Налаштування', ft.Icons.SETTINGS_ROUNDED, Button_white, 280, 70, Link_settings)

        NavigationPanel = ft.Container(
                    ft.Column(
                        ft.Row(
                            NavigationPanel_title,
                            Navigation_button_close
                        ),
                        NavigationPanel_button_menu,
                        NavigationPanel_button_calculation,
                        NavigationPanel_button_settings
                    ),
                    bgcolor=ft.Colors.GREY_900,
                    padding=10,
                    width=260,
                    expand=True,
                    visible=False
                )

        PageBody = ft.Stack(
            [
                ft.Container(
                    ft.Row(
                        controls=[
                            Navigation_button_open,
                            App_title
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=10
                ),

                NavigationPanel
            ],
            expand=True
        )

        st = ft.ResponsiveRow([
            ft.Column(col={"xs": 12, "sm": 4, "xl": 6}, controls=[PageBody])
        ])

        return ft.View('/', controls=[st], bgcolor=PageBgColor, padding=0)