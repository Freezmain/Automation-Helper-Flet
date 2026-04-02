import flet as ft

from assets.icons import *
from utils.style import *
from utils.catalogs import *
from components.buttons import *
from components.texts import *
from components.calculation.calculation_lists.light_list import Light_list

# МОДАЛЬНЕ ВІКНО ДОДАВАННЯ ПРИСТРОЇВ
class Modal_add_element:
    def __init__(self, page):
        self.page = page
        self.light_list = Light_list(self.page)
        self.modal_add_element = ft.AlertDialog(
            modal = True,
            content = ft.Container(
                content = ft.Column(
                    controls = [
                        # Header модального вікна додавання пристроїв
                        ft.Row(
                            controls = [
                                IconButton_Close(ft.Icons.CLOSE, Button_close_style, self.toggle_visible),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        # Список пристроїв
                        TextCenter("Оберіть елементи", TextSubTitle_style),
                        ft.Container(height = 10),
                        ft.ExpansionTile(
                            title = "Світло",
                            leading = ft.Icons.LIGHTBULB_ROUNDED,
                            controls = self.light_list.get_elements("Light"),
                        ),
                        ft.ExpansionTile(
                            title = "Клімат",
                            leading = ft.Icons.LIGHTBULB_ROUNDED,
                            controls = self.light_list.get_elements("Climate"),
                        ),
                        ft.ExpansionTile(
                            title = "Приводи",
                            leading = ft.Icons.LIGHTBULB_ROUNDED,
                            controls = self.light_list.get_elements("Drive"),
                        ),
                        ft.ExpansionTile(
                            title = "Датчики",
                            leading = ft.Icons.LIGHTBULB_ROUNDED,
                            controls = self.light_list.get_elements("Sensor"),
                        ),
                        ft.ExpansionTile(
                            title = "Вимикачі",
                            leading = ft.Icons.LIGHTBULB_ROUNDED,
                            controls = self.light_list.get_elements("Key"),
                        ),
                        ft.ExpansionTile(
                            title = "Інше",
                            leading = ft.Icons.LIGHTBULB_ROUNDED,
                            controls = self.light_list.get_elements("Other"),
                        ),
                    ],
                    width = 380,
                    height = 500,
                    scroll = ft.ScrollMode.ADAPTIVE,
                    tight = True,
                )
            )
        )
    
    # Перемикання видимості модального вікна
    def toggle_visible(self):
        self.modal_add_element.open = not self.modal_add_element.open
    
    # Повернення модального вікна
    def get_modal(self):
        return self.modal_add_element