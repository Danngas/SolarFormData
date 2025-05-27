# src/layout/base.py
from flet import *
from src.pages.navbar import ModernNavBar, sidebar_column_ref

def TelaBase(page: Page, trocar_conteudo_callback):
    sidebar = Container(
        width=200,
        height=580,
        bgcolor="black",
        border_radius=10,
        animate=animation.Animation(500, "decelerate"),
        alignment=alignment.center,
        padding=10,
        content=ModernNavBar(trocar_conteudo_callback).build(),
    )

    conteudo_principal = Container(
        expand=True,
        padding=20,
        bgcolor="white",
        border_radius=10,
        content=Column(controls=[], scroll="auto"),
    )

    return Row(
        expand=True,
        controls=[
            sidebar,
            conteudo_principal,
        ]
    ), conteudo_principal  # Retornamos o layout e o container principal que muda
