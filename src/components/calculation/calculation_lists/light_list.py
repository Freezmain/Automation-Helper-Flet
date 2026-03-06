import flet as ft

from utils.style import *
from utils.catalogs import *
from components.buttons import *

class Light_list:
    def __init__(self, page):
        self.page = page
        self.light_list = ft.Column(
            controls = self.take_lights("Light"),
            spacing = 5,
            scroll=ft.ScrollMode.AUTO,
            visible = False,
        )
    
    def open_details(self, e):
        element_data = e.control.data

        modal_controls = [
            ft.Text("Налаштування елемента:"),
            ft.Text(f"Назва: {element_data.get('name')}"),
        ]

        if "base_voltage" in element_data:
            modal_controls.append(ft.Text(f"Напруга: {element_data.get('base_voltage')}")),
        
        if "base_type_output" in element_data:
            modal_controls.append(ft.Text(f"Тип виходу: {element_data.get('base_type_output')}")),
            modal_controls.append(ft.Text(f"Кількість виходів: {element_data.get('base_count_output')}")),
        else:
            modal_controls.append(ft.Text(f"Тип входу: {element_data.get('base_type_input')}")),
            modal_controls.append(ft.Text(f"Кількість входів: {element_data.get('base_count_input')}")),
        
        modal_controls.append(ft.Button("Додати", on_click = lambda _: self.close_modal_details(modal_details)))
        
        modal_details = ft.AlertDialog(
            content = ft.Column(
                controls = modal_controls,
                spacing = 5,
                tight = True
            )
        )
        
        self.page.overlay.append(modal_details)
        modal_details.open = True
        self.page.update()
    
    def take_lights(self, category_name):
        lights_catalog = CATALOG_ELEMENTS[category_name]
        lights_buttons = []
        
        for l in lights_catalog:
            button = ft.Button(
                content = l['name'],
                data = l,
                on_click = self.open_details,
            )
            lights_buttons.append(button)
        
        return lights_buttons

    def close_modal_details(self, modal):
        modal.open = False
        self.page.update()
    
    def toggle_vision(self, e = None):
        self.light_list.visible = not self.light_list.visible
    
    def get_lights(self):
        return self.light_list