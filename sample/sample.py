import flet as ft


def main(page: ft.Page):
    t = ft.Text(value="Hello, World!", color="blue", size=50)
    page.add(t)

    def button_clicked(e):
        page.add(ft.Text(value="Clicked!", color="green", size=30))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    output_text = ft.Text(value="Checkboxの値 : False", size=20)

    def checkbox_changed(e):
        output_text.value = (
            f"Checkboxの値 : {todo_check.value}"
        )
        page.update()

    todo_check = ft.Checkbox(label="テスト", value=False,  on_change=checkbox_changed)

    page.add(todo_check, output_text)


ft.app(target=main)
