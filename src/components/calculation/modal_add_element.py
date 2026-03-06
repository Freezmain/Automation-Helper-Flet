import flet as ft

from utils.style import *
from utils.catalogs import *
from components.buttons import *
from components.texts import *
from components.calculation.calculation_lists.light_list import Light_list

class Modal_add_element:
    def __init__(self, page):
        self.page = page
        self.light_list = Light_list(self.page)
        self.modal_add_element = ft.AlertDialog(
            modal = True,
            content = ft.Container(
                ft.Column(
                    controls = [
                        ft.Row(
                            controls = [
                                IconButton_Close(ft.Icons.CLOSE, Button_close_style, self.toggle_visible),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        Text("Оберіть елементи:", TextSubTitle_style),
                        ft.Button("Світло", icon = ft.Icons.KEYBOARD_ARROW_RIGHT, on_click = lambda _: self.light_list.toggle_vision("Light")),
                        self.light_list.get_elements("Light"),
                        ft.Button("Клімат", icon = ft.Icons.KEYBOARD_ARROW_RIGHT, on_click = lambda _: self.light_list.toggle_vision("Climate")),
                        self.light_list.get_elements("Climate"),
                        ft.Button("Привода", icon = ft.Icons.KEYBOARD_ARROW_RIGHT, on_click = lambda _: self.light_list.toggle_vision("Drive")),
                        self.light_list.get_elements("Drive"),
                        ft.Button("Датчики", icon = ft.Icons.KEYBOARD_ARROW_RIGHT, on_click = lambda _: self.light_list.toggle_vision("Sensor")),
                        self.light_list.get_elements("Sensor"),
                        ft.Button("Клавіші", icon = ft.Icons.KEYBOARD_ARROW_RIGHT, on_click = lambda _: self.light_list.toggle_vision("Key")),
                        self.light_list.get_elements("Key"),
                        ft.Button("Інше", icon = ft.Icons.KEYBOARD_ARROW_RIGHT, on_click = lambda _: self.light_list.toggle_vision("Other")),
                        self.light_list.get_elements("Other"),
                    ]
                )
            )
        )
    
    def toggle_visible(self):
        self.modal_add_element.open = not self.modal_add_element.open
        
    def get_modal(self):
        return self.modal_add_element