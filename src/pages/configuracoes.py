import flet as ft

class Configuracoes:
    def build(self):
        return ft.Container(
            width=600,
            height=580,
            bgcolor="white",
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text("Configurações", size=20, weight="bold"),
                    ft.Text("Em desenvolvimento: Ajustes do sistema."),
                ]
            ),
        )