import flet as ft

from utils.style import *
from utils.catalogs import *
from components.buttons import *

class Light_list:
    def __init__(self, page):
        self.page = page
        self.light_list = self.take_elements_list("Light")
        self.climate_list = self.take_elements_list("Climate")
        self.drive_list = self.take_elements_list("Drive")
        self.sensor_list = self.take_elements_list("Sensor")
        self.key_list = self.take_elements_list("Key")
        self.other_list = self.take_elements_list("Other")
    
    def take_elements_list(self, element):
        return ft.Column(
            controls = self.take_elements(element),
            spacing = 5,
            scroll=ft.ScrollMode.AUTO,
            visible = False,
        )
    
    def take_elements(self, category_name):
        lights_catalog = CATALOG_ELEMENTS[category_name]
        lights_buttons = []
        
        for l in lights_catalog:
            button = Button_modal_add_element_item(
                l['name'],
                l['icon'],
                Button_modal_add_element_style_item,
                l,
                self.open_details
            )
            lights_buttons.append(button)
        
        return lights_buttons
    
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

    def close_modal_details(self, modal):
        modal.open = False
        self.page.update()
    
    def toggle_vision(self, category_element):
        target_list = self.get_elements(category_element)
        
        if target_list:
            target_list.visible = not target_list.visible
            self.page.update()
    
    def get_elements(self, element):
        if element == "Light":
            return self.light_list
        elif element == "Climate":
            return self.climate_list
        elif element == "Drive":
            return self.drive_list
        elif element == "Sensor":
            return self.sensor_list
        elif element == "Key":
            return self.key_list
        else:
            return self.other_list