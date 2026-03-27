import flet as ft

# Стиль додатку
Page_style: dict = {
    'bgcolor': "#2C3440",
    'height': 1024,
    'width': 576,
}

# Стиль навігаційного меню
NavBar_style: dict = {
    'bgcolor': "#373E49",
    'height': 1280,
    'width': 210,
    'padding-left': 10,
    'spacing': 1,
    'padding': 0,
    'padding-right': 2,
}

# Стиль заголовку
TextTitle_style: dict = {
    'color': '#FFFFFF',
    'size': 20,
    'weight': ft.FontWeight.W_600,
}

# Стиль підзаголовку
TextSubTitle_style: dict = {
    'color': '#FFFFFF',
    'size': 17,
    'weight': ft.FontWeight.W_600
}

# Стиль кнопки
Button_style = ft.ButtonStyle(
    color = "#80BCE4",
    shape = ft.RoundedRectangleBorder(radius=15),
    icon_size = 25,
)

# Стиль кнопки закриття
Button_close_style: dict = {
    'bgcolor': ft.Colors.TRANSPARENT,
    'shape': ft.RoundedRectangleBorder(radius=0),
    'height': 40,
    'width': 40,
    'icon_size': 20,
}

# Стиль кнопки переходу на сторінку (НАВІГАЦІЙНЕ МЕНЮ)
Button_navBar_style: dict = {
    'shape': ft.RoundedRectangleBorder(radius=0),
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

# Стиль кнопки показу доступних пристроїв проєкту (МОДАЛЬНЕ ВІКНО ДОДАВАННЯ ЕЛЕМЕНТІВ)
Button_modal_add_element_style: dict = {
    'color': "#FFFFFF",
    'bgcolor': "#373E49",
    'height': 40,
    'width': 310,
    'elevation': 0,
    'icon_size': 25,
    'text_size': 15,
    'spacing': 10
}

# Стиль кнопки показу інформації про пристрій проєкту (МОДАЛЬНЕ ВІКНО ДОДАВАННЯ ЕЛЕМЕНТІВ)
Button_modal_add_element_style_item: dict = {
    'color': "#FFFFFF",
    'bgcolor': "#31373D",
    'height': 30,
    'width': 100,
    'elevation': 0,
    'icon_size': 22,
    'text_size': 13,
    'spacing': 10
}