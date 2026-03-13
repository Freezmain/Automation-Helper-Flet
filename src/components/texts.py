from utils.style import *
from typing import Callable

def Text(text: str, style: dict):
    return ft.Text(
        value = text,
        **style,
    )

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