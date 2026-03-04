import flet as ft

from views.home import View_home
from views.calculation import View_calculation
from views.designing import View_designing
from views.installation import View_installation
from views.settings import View_settings

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        
        # Створюємо словник інстансів класів
        self.views = {
            "/": View_home(page),
            "/calculation": View_calculation(page),
            "/designing": View_designing(page),
            "/installation": View_installation(page),
            "/settings": View_settings(page),
        }

    def route_change(self, e=None):
        self.page.views.clear()
        
        # Отримуємо об'єкт в'ю за маршрутом (або за замовчуванням "/")
        current_view_obj = self.views.get(self.page.route)
        
        if current_view_obj:
            # Викликаємо спільний метод .build(), який ми створили в BaseView
            self.page.views.append(current_view_obj.build())
        else:
            # Опціонально: обробка 404 або редирект на головну
            self.page.go("/")
            
        self.page.update()
    
    def start_routing(self):
        self.page.on_route_change = self.route_change
        # Ініціалізуємо початковий маршрут
        self.route_change()