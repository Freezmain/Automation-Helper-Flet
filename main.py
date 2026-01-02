import flet as ft

def main(page: ft.Page):
    page.title = "SVIT-Helper" # Назва
    page.window.icon = "icons/logo.png" # Іконка
    page.theme_mode = 'black' # Тема
    page.padding = 0
    page.spacing = 0

    main_text = ft.Text("Головний екран")

    #---- Зміна робочого розділу ----
    def change_tab(element):
        index = element.control.selected_index
        if index == 0:
            main_text.value = "Головний екран"
        elif index == 1:
            main_text.value = "Розрахунок модулів"
        elif index == 2:
            main_text.value = "Конфігуратор проєкту"
        elif index == 3:
            main_text.value = "Процес підключення"
        elif index == 4:
            main_text.value = "Налаштування"
        page.update()

    #---- Вигляд застосунку -----
    page.add(
        ft.Column(
            [
                ft.Container(
                    bgcolor = "#18181c",
                    height = 100,
                    width = float("inf"),
                    content = ft.Text("Хедер", color = "white"),
                ),

                ft.Row(
                    [
                        ft.Container(
                            bgcolor = "#17171a",
                            height = float("inf"),
                            width = 150,
                            content = ft.Text("Бокове меню", color = "white"),
                        ),

                        ft.Container(
                            bgcolor = "#373840",
                            height = float("inf"),
                            expand = True,
                            content = main_text,
                        ),
                    ],
                    expand = True,
                    spacing = 0,
                )
            ],
            expand = True,
            spacing = 0,
        )
    )

ft.app(target = main) # Запуск застосунку