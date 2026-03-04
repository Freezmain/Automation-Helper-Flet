import flet as ft

from views.base_view import BaseView
from components.buttons import *

class View_calculation(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page, route="/calculation")

    def get_content(self):
        return [
            ft.Row(
                controls=[
                    Button_CalculationBar("Світло", ft.Icons.LIGHTBULB_OUTLINE, Button_calculationBar_style),
                    Button_CalculationBar("Клімат", ft.Icons.LIGHTBULB_OUTLINE, Button_calculationBar_style),
                    Button_CalculationBar("Керування", ft.Icons.LIGHTBULB_OUTLINE, Button_calculationBar_style),
                    Button_CalculationBar("Інше", ft.Icons.LIGHTBULB_OUTLINE, Button_calculationBar_style)
                ],
                alignment = ft.MainAxisAlignment.CENTER,
            )
        ]