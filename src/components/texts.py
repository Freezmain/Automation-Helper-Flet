from utils.style import *

# Текст звичайний
def Text(text: str, style: dict):
    return ft.Text(
        value = text,
        **style,
    )

# Рядок з текстом
def TextCenter(text: str, style: dict):
    return ft.Column(
        controls = [
            ft.Text(
                value = text,
                **style
            ),
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        width = float("inf"),
    )