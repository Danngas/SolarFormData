import flet as ft
from src.pages.navbar import ModernNavBar
from src.pages.topbar import TopBar
from src.pages.dashboard import Dashboard
from src.pages.form import Form
from src.pages.configuracao import Configuracoes
from src.pages.perfil import Perfil

def main(page: ft.Page):
    page.title = "SolarFormData"
    page.bgcolor = "#ffffff"  # Fundo branco
    page.horizontal_alignment = ft.MainAxisAlignment.START  # Alinha à esquerda
    page.vertical_alignment = ft.MainAxisAlignment.START  # Alinha ao topo
    page.padding = 0  # Remove padding padrão da página
    page.window_width = 1280  # Tamanho inicial da janela
    page.window_height = 720
    page.window_min_width = 400  # Tamanho mínimo
    page.window_min_height = 300

    # Referência para o content_container
    content_container_ref = ft.Ref[ft.Container]()

    # Calcula dimensões iniciais
    navbar_width = 200  # Expandida inicialmente
    content_width = page.width - navbar_width  # Largura restante menos navbar
    content_height = page.height - 60  # Altura menos TopBar

    # Container para conteúdo
    content_container = ft.Container(
        ref=content_container_ref,
        width=content_width,
        height=content_height,
        bgcolor="#ffffff",
        animate_opacity=300,
        opacity=1,
        content=Dashboard().build(),
    )

    # Função de navegação
    def navigate(route):
        content_container.opacity = 0
        content_container.update()
        
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
        
        content_container.opacity = 1
        content_container.update()

    # Cria navbar
    navbar = ModernNavBar(on_navigate=navigate)
    
    # Função para detectar clique no botão de menu e atualizar dimensões
    def on_menu_click(e):
        nonlocal navbar_width, content_width
        navbar_width = 200 if navbar.expanded else 60
        content_width = page.width - navbar_width
        if content_container_ref.current:
            content_container_ref.current.width = content_width
            content_container_ref.current.update()

    # Adiciona GestureDetector ao botão de menu
    for control in navbar.build().content.controls:
        if isinstance(control, ft.Container) and isinstance(control.content, ft.Icon) and control.content.name == ft.icons.MENU:
            control.on_click = on_menu_click
            break

    # Função para atualizar dimensões ao redimensionar
    def on_resize(e):
        nonlocal content_width, content_height, navbar_width
        navbar_width = 200 if navbar.expanded else 60
        content_width = page.width - navbar_width
        content_height = page.height - 60
        if content_container_ref.current:
            content_container_ref.current.width = content_width
            content_container_ref.current.height = content_height
            content_container_ref.current.update()

    page.on_resize = on_resize

    # Cria topbar
    topbar = TopBar(page=page, user_name="Daniel Silva de Souza", company="Flex Solar")

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                topbar.build(),
                ft.Row(
                    controls=[
                        navbar.build(),
                        content_container,
                    ],
                    alignment=ft.MainAxisAlignment.START,  # Alinha à esquerda
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH,  # Estica verticalmente
                    spacing=0,  # Sem espaçamento interno
                    expand=True,  # Ocupa toda a altura restante
                ),
            ],
            spacing=0,  # Sem espaçamento interno
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            expand=True,  # Ocupa toda a altura da página
        )
    )

ft.app(target=main)