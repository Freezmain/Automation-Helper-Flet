import flet as ft

from assets.icons import *
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
                content = (
                    ft.Column(
                        controls = [
                            ft.Row(
                                controls = [
                                    IconButton_Close(ft.Icons.CLOSE, Button_close_style, self.toggle_visible),
                                ],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                            TextCenter("Оберіть елементи", TextSubTitle_style),
                            ft.Container(height = 10),
                            Button_modal_add_element("Світло", ft.Icons.LIGHTBULB_ROUNDED, Button_modal_add_element_style, function = lambda _: self.light_list.toggle_vision("Light")),
                            self.light_list.get_elements("Light"),
                            Button_modal_add_element("Клімат",, Button_modal_add_element_style, function = lambda _: self.light_list.toggle_vision("Climate")),
                            self.light_list.get_elements("Climate"),
                            Button_modal_add_element("Привода", ft.Icons.KEYBOARD_ARROW_RIGHT, Button_modal_add_element_style, function = lambda _: self.light_list.toggle_vision("Drive")),
                            self.light_list.get_elements("Drive"),
                            Button_modal_add_element("Датчики", ft.Icons.KEYBOARD_ARROW_RIGHT, Button_modal_add_element_style, function = lambda _: self.light_list.toggle_vision("Sensor")),
                            self.light_list.get_elements("Sensor"),
                            Button_modal_add_element("Клавіші", ft.Icons.KEYBOARD_ARROW_RIGHT, Button_modal_add_element_style, function = lambda _: self.light_list.toggle_vision("Key")),
                            self.light_list.get_elements("Key"),
                            Button_modal_add_element("Інше", ft.Icons.KEYBOARD_ARROW_RIGHT, Button_modal_add_element_style, function = lambda _: self.light_list.toggle_vision("Other")),
                            self.light_list.get_elements("Other"),
                        ],
                        width = 380,
                        scroll = ft.ScrollMode.ADAPTIVE, 
                        tight = True,
                    )
                )
            )
        )
    
    def toggle_visible(self):
        self.modal_add_element.open = not self.modal_add_element.open
        
    def get_modal(self):
        return self.modal_add_element