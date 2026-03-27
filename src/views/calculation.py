import flet as ft

from views.base_view import BaseView
from components.calculation.modal_add_element import Modal_add_element
from components.buttons import *

# РОЗРАХУНОК КІЛЬКОСТІ МОДУЛІВ
class View_calculation(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page, route="/calculation")
        self.modal_add_element = Modal_add_element(page)
    
    def get_content(self):
        return [
            # Додавання пристроїв проєкту
            ft.Container(
                content = ft.Row(
                    controls=[
                        Button("Додати", ft.Icons.ADD, Button_style, self.modal_add_element.toggle_visible),
                    ],
                    alignment = ft.MainAxisAlignment.START,
                ),
                padding = ft.Padding(left = 20),
            ),
            # Модальне вікно додавання пристроїв
            ft.Container(
                content = self.modal_add_element.get_modal(),
            )
        ]