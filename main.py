import flet as ft
from src.pages.navbar import ModernNavBar
from src.pages.dashboard import Dashboard
from src.pages.form import Form
from src.pages.configuracoes import Configuracoes
from src.pages.perfil import Perfil

def main(page: ft.Page):
    page.title = "SolarFormData"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Container pra conteúdo
    content_container = ft.Container(
        width=600,
        height=580,
        animate_opacity=300,
        opacity=1,
        content=Dashboard().build(),  # Usa .build()
    )

    # Função de navegação
    def navigate(route):
        content_container.opacity = 0  # Inicia transição
        content_container.update()
        
        # Atualiza conteúdo com base na rota
        if route == "/dashboard":
            content_container.content = Dashboard().build()
        elif route == "/form":
            content_container.content = Form().build()
        elif route == "/configuracoes":
            content_container.content = Configuracoes().build()
        elif route == "/perfil":
            content_container.content = Perfil().build()
        else:
            content_container.content = ft.Text(f"Página {route} em desenvolvimento")
        
        content_container.opacity = 1  # Finaliza transição
        content_container.update()

    # Cria navbar com callback
    navbar = ModernNavBar(on_navigate=navigate)

    # Layout principal
    page.add(
        ft.Row(
            controls=[
                navbar.build(),  # Usa navbar.build()
                content_container,
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )



ft.app(target=main)