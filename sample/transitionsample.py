import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View


def main(page: Page):
    def route_change(e):
        print("Route change:", e.route)

        page.views.clear()

        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("トップページ")),
                    ElevatedButton(
                        "テストページへ移動", on_click=open_test
                    ),
                ],
            )
        )

        if page.route == "/test":
            page.views.append(
                View(
                    "/test",
                    [
                        AppBar(title=Text("テストページ")),
                        Text("これはテストページです。", size=20),
                        ElevatedButton(
                            "戻る", on_click=return_home
                        ),
                    ],
                )
            )

        page.update()

    # 現在のページを削除して前のページに戻る
    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def open_test(e):
        page.go("/test")

    def return_home(e):
        page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
