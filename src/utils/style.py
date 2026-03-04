import flet as ft

Page_style: dict = {
    'bgcolor': "#2C3440",
    'height': 1024,
    'width': 576,
}

TextTitle_style: dict = {
    'color': '#FFFFFF',
    'size': 17,
    'weight': ft.FontWeight.W_600,
}

TextSubTitle_style: dict = {
    'color': '#FFFFFF',
    'size': 25,
    'weight': ft.FontWeight.W_400
}

Button_close_style: dict = {
    'bgcolor': "#373E49",
    'shape': ft.RoundedRectangleBorder(radius=0),
    'height': 30,
    'width': 30,
    'icon_size': 15,
}

NavBar_style: dict = {
    'bgcolor': "#373E49",
    'height': 1280,
    'width': 210,
    'padding-left': 10,
    'spacing': 1,
    'padding': 0,
    'padding-right': 2,
}

Button_navBar_style: dict = {
    'shape': ft.RoundedRectangleBorder(radius=0),
    'alignment': ft.MainAxisAlignment.START,
    'color': "#FFFFFF",
    'bgcolor': "#373E49",
    'height': 60,
    'weight': 200,
    'elevation': 0,
    'icon_size': 25,
    'text_size': 15,
    'spacing': 10,
    'padding-left': 0,
}

Button_calculationBar_style: dict = {
    'shape': ft.RoundedRectangleBorder(radius=15),
    'alignment': ft.MainAxisAlignment.START,
    'color': "#80BCE4",
    'height': 30,
    'width': 120,
    'icon_size': 20,
    'text_size': 13,
}