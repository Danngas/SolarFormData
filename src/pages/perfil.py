import flet as ft

class Perfil:
    def build(self):
        return ft.Container(
            width=600,
            height=580,
            bgcolor="white",
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text("Perfil", size=20, weight="bold"),
                    ft.Text("Em desenvolvimento: Dados do usuário."),
                ]
            ),
        )