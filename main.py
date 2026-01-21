import flet as ft

def main(page: ft.Page):
    page.title = "SVIT-Helper"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input = ft.TextField(value = "0", text_align = ft.TextAlign.RIGHT, width = 50)

    def button_minus(e):
        input.value = str(int(input.value) - 1)
    
    def button_plus(e):
        input.value = str(int(input.value) + 1)

    page.add(
        ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [
                ft.IconButton(ft.Icons.REMOVE, on_click = button_minus),
                input,
                ft.IconButton(ft.Icons.ADD, on_click = button_plus),
            ],
        )
    )

ft.run(main)