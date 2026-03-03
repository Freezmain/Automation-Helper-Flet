import flet as ft

pageBgColor: str = "#2C3440"
navBarBgColor: str = "#373E49"

pageWidth: int = 720
navBarWidth: int = 200

pageHeight: int = 1280
navBarHeight: int = 1280

pageFont: dict = {

}

TextTitle_style: dict = {
    'color': 'white',
    'size': 30,
    'weight': ft.FontWeight.W_600
}

TextSubTitle_style: dict = {
    'color': 'white',
    'size': 25,
    'weight': ft.FontWeight.W_400
}

Button_close: dict = {
    'color': "white",
    'bgcolor': "#373E49",
    'side': ft.BorderSide(2, "#1D1F25"),
    'shape': ft.RoundedRectangleBorder(radius=10),
}

Button_navBar: dict = {
    'color': "white",
    'bgcolor': "#373E49",
    'side': ft.BorderSide(2, "#1D1F25"),
    'shape': ft.RoundedRectangleBorder(radius=0),
}