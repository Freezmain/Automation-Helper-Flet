from utils.style import *
from typing import Callable

# Кнопка звичайна
def Button(text: str, icon: ft.Icon, style: ft.ButtonStyle, function: Callable):
    return ft.Button(
        content = text,
        icon = icon,
        style = style,
        on_click = function,
    )

# Кнопка закриття
def IconButton_Close(icon: ft.Icon, style: dict, function: Callable):
    return ft.IconButton(
        style = ft.ButtonStyle(
            overlay_color=ft.Colors.TRANSPARENT,
            shape = style.get('shape'),
        ),
        icon_size = style.get('icon_size'),
        bgcolor = style.get('bgcolor'),
        height = style.get('height'),
        width = style.get('width'),
        icon = icon,
        on_click = function,
        )

# Кнопка переходу на сторінку (НАВІГАЦІЙНЕ МЕНЮ)
def Button_NavBar(text: str, icon: ft.Icon, style: dict, function: Callable):
    return ft.Button(
        content = ft.Container(
            ft.Row(
                controls=[
                    ft.Icon(icon = icon, size = style.get('icon_size')),
                    ft.Text(value = text, size = style.get('text_size')),
                ],
                spacing = style.get('spacing'),
            ),
            padding = ft.padding.only(style.get('padding-left'))
        ),
        style = ft.ButtonStyle(
            shape = style.get('shape')
        ),
        bgcolor = style.get('bgcolor'),
        color = style.get('color'),
        elevation = style.get('elevation'),
        height = style.get('height'),
        width = style.get('width'),
        on_click = function,
    )

# Кнопка показу доступних пристроїв проєкту (МОДАЛЬНЕ ВІКНО ДОДАВАННЯ ЕЛЕМЕНТІВ)
def Button_modal_add_element(text: str, icon: ft.Icon, style: dict, function: Callable):
    return ft.Button(
        content = ft.Container(
            ft.Row(
                controls = [
                    ft.Icon(icon = icon, size = style.get('icon_size')),
                    ft.Text(value = text, size = style.get('text_size')),
                ],
                spacing = style.get('spacing'),
            ),
            width = style.get('width'),
        ),
        bgcolor = style.get('bgcolor'),
        color = style.get('color'),
        elevation = style.get('elevation'),
        height = style.get('height'),
        on_click = function,
    )

# Кнопка показу інформації про пристрій проєкту (МОДАЛЬНЕ ВІКНО ДОДАВАННЯ ЕЛЕМЕНТІВ)
def Button_modal_add_element_item(text: str, icon: ft.Icon, style: dict, data, function: Callable):
    return ft.Button(
        content = ft.Container(
            ft.Row(
                controls = [
                    ft.Icon(icon = icon, size = style.get('icon_size')),
                    ft.Text(value = text, size = style.get('text_size')),
                ],
                spacing = style.get('spacing'),
            ),
            width = style.get('width'),
        ),
        data = data,
        bgcolor = style.get('bgcolor'),
        color = style.get('color'),
        elevation = style.get('elevation'),
        height = style.get('height'),
        on_click = function
    )