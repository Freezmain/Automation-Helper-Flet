from utils.style import *
from typing import Callable

def Text(text: str, style: dict):
    return ft.Text(
        value = text,
        **style,
    )