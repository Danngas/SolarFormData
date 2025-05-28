import flet as ft

class TopBar:
    def __init__(self, page: ft.Page, user_name: str, company: str):
        self.page = page
        self.user_name = user_name
        self.company = company

        # Paleta de cores (mesma do navbar.py)
        self.color_blue = "#005e9b"
        self.color_white = "#ffffff"
        self.color_gray_dark = "#333333"
        self.color_orange = "#ff8f0d"

    def logout(self, e):
        self.page.window.close()  # Simula logout fechando a aplicação

    def build(self):
        return ft.Container(
            height=60,
            bgcolor=self.color_blue,
            border_radius=0,  # Bordas retas
            padding=ft.padding.symmetric(horizontal=20),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        value="Enner Engenharia",
                        size=20,
                        weight="bold",
                        color=self.color_white,
                    ),
                    ft.Row(
                        spacing=10,
                        controls=[
                            ft.Text(
                                value=f"{self.user_name} | {self.company}",
                                size=14,
                                color=self.color_white,
                            ),
                            ft.IconButton(
                                icon=ft.icons.LOGOUT,
                                icon_color=self.color_white,
                                icon_size=20,
                                tooltip="Sair",
                                on_click=self.logout,
                                style=ft.ButtonStyle(
                                    overlay_color={"hovered": self.color_orange},
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )