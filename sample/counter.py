import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="10", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()  # 画面を更新

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()  # 画面を更新

        # page.controls[0].controls.pop(2)
        # page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


# webブラウザで起動
ft.app(target=main, view=ft.WEB_BROWSER)
