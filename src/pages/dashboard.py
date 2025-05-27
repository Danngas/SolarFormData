import flet as ft

class Dashboard:
    def build(self):
        return ft.Container(
            width=600,
            height=580,
            bgcolor="white",
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text("Dashboard", size=20, weight="bold"),
                    ft.Text("Em desenvolvimento: Tabela de projetos (Cliente, Projeto ID, Status)."),
                ]
            ),
        )