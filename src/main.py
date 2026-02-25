import flet as ft
from router import Router
from dotenv import load_dotenv

load_dotenv()

async def main(page: ft.Page):
    Router(page)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")