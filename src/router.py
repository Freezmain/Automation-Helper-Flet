from flet_route import Routing, path
import flet as ft

#----Сторінки----
from views.app_calculating_page import CalculationPage

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routes = [
            #path(url='/h', clear=True, view=HomePage().view),
            path(url='/', clear=True, view=CalculationPage().view),
            #path(url='/settings', clear=True, view=SettingsPage().view),
        ]

        Routing(page=self.page, app_routes=self.app_routes)
        self.page.go(self.page.route)