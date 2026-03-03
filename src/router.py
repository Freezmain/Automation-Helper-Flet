import flet as ft

from views.home import View_home
from views.calculation import View_calculation
from views.designing import View_designing
from views.installation import View_installation
from views.settings import View_settings

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        
        self.views = {
            "/": View_home(page),
            "/calculation": View_calculation(page),
            "/designing": View_designing(page),
            "/installation": View_installation(page),
            "/settings": View_settings(page),
        }

    def route_change(self, e=None):
            self.page.views.clear()
            
            if self.page.route == "/":
                self.page.views.append(
                    self.views["/"].Get_HomeView()
                )
            if self.page.route == "/calculation":
                self.page.views.append(
                    self.views["/calculation"].Get_CalculationView()
                )
            if self.page.route == "/designing":
                self.page.views.append(
                    self.views["/designing"].Get_DesigningView()
                )
            if self.page.route == "/installation":
                self.page.views.append(
                    self.views["/installation"].Get_InstallationView()
                )
            if self.page.route == "/settings":
                self.page.views.append(
                    self.views["/settings"].Get_SettingsView()
                )
            self.page.update()
    
    def start_routing(self):
        self.page.on_route_change = self.route_change

        self.route_change()