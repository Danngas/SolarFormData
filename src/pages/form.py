import flet as ft

class Form:
    def build(self):
        return ft.Container(
            width=600,
            height=580,
            bgcolor="white",
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text("Formulário", size=20, weight="bold"),
                    ft.Text("Em desenvolvimento: Formulário de homologação (Nome, CPF/CNPJ, etc.)."),
                ]
            ),
        )