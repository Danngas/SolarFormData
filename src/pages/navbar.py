from flet import *
from functools import partial

# Referências globais para manipular o container da sidebar e a coluna interna
sidebar_ref = Ref[Container]()
sidebar_column_ref = Ref[Column]()

class ModernNavBar:
    def __init__(self, func):
        self.func = func
        self.expanded = True  # Estado inicial da navbar: expandida (True) ou recolhida (False)

        # ====== PALETA DE CORES ======
        # Altere essas cores para mudar visualmente toda a navbar
        self.color_blue = "#005e9b"               # Cor azul usada para ícones e texto no modo normal (expandido)
        self.color_orange = "#ff8c0d"             # Cor laranja para destaque (hover)
        self.color_blue_light = "#4a90e2"         # Azul claro (não usado muito neste código)
        self.color_gray_dark = "#333333"          # Cinza escuro para texto em estado normal
        self.color_gray_medium = "#7d7d7d"        # Cinza médio para textos secundários
        self.color_gray_light = "#d3d3d3"         # Cinza claro usado para divisor (divider)
        self.color_white = "#ffffff"               # Cor branca para texto e ícones sobre fundo escuro
        self.color_black_soft = "#121212"          # Preto suave (não usado diretamente aqui)
        
        # Cores de fundo da navbar para os estados expandido e recolhido
        self.color_navbar_bg_expanded = "#e7eaf0"  # Fundo claro da navbar quando expandida
        self.color_navbar_bg_collapsed = "#005e9b" # Fundo azul escuro quando recolhida (modo compacto)

        self.color_orange_hover = "#4caf50"        # Cor laranja clara para hover (passar o mouse em cima)
        self.color_error = "#f44336"                # Cor vermelha para erros (não usada aqui)
        self.color_success = "#4caf50"              # Cor verde para sucesso (não usada aqui)

    # Função que controla o efeito hover (mouse em cima de um item)
    def HighLight(self, e):
        if e.data == 'true':  # Se está em hover (true)
            e.control.bgcolor = self.color_orange_hover  # Fundo laranja claro para destaque
            e.control.update()
            # Ícone e texto ficam brancos para contraste sobre o fundo laranja
            e.control.content.controls[0].icon_color = self.color_white
            if len(e.control.content.controls) > 1:
                e.control.content.controls[1].color = self.color_white
                e.control.content.update()
        else:  # Quando o mouse sai (hover falso)
            e.control.bgcolor = None  # Fundo transparente no modo normal
            e.control.update()
            # Ícone azul e texto cinza escuro
            e.control.content.controls[0].icon_color = self.color_blue
            if len(e.control.content.controls) > 1:
                e.control.content.controls[1].color = self.color_gray_dark
                e.control.content.update()

    # Cria o bloco de dados do usuário na navbar (iniciais, nome e descrição)
    def UserData(self, initials: str, name: str, description: str):
        return Container(
            visible=self.expanded,          # Visível só quando expandida
            animate_opacity=300,            # Animação de opacidade suave
            opacity=1 if self.expanded else 0,
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor=self.color_blue,  # Fundo azul para círculo das iniciais
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold",
                            color=self.color_white,  # Texto branco para iniciais
                        ),
                    ),
                    Column(
                        spacing=1,
                        alignment="center",
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200,
                                color=self.color_blue       # Nome em azul
                            ),
                            Text(
                                value=description,
                                size=10,
                                weight='w400',
                                color=self.color_gray_medium,  # Descrição em cinza médio
                                opacity=1,
                                animate_opacity=200,
                            )
                        ]
                    )
                ]
            )
        )

    # Cria um item da navbar com ícone e texto
    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),   # Efeito hover
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color=self.color_blue,  # Ícone azul no modo expandido
                        style=ButtonStyle(
                            shape={"": RoundedRectangleBorder(radius=7)},
                            overlay_color={"": "Transparent"},  # Sem overlay padrão
                        ),
                    ),
                    Text(
                        value=text,
                        color=self.color_gray_dark,  # Texto cinza escuro
                        size=12,
                        visible=self.expanded,       # Texto visível só no modo expandido
                        animate_opacity=300,
                        opacity=1 if self.expanded else 0
                    ),
                ]
            ),
        )

    # Função que alterna o estado da sidebar (expandida/recolhida)
    def toggle_sidebar(self, e):
        self.expanded = not self.expanded  # Inverte o estado

        sidebar = sidebar_ref.current
        column = sidebar_column_ref.current

        # Ajusta a largura da sidebar
        sidebar.width = 200 if self.expanded else 60

        # Muda a cor de fundo conforme estado da sidebar
        sidebar.bgcolor = self.color_navbar_bg_expanded if self.expanded else self.color_navbar_bg_collapsed

        # Atualiza cor dos ícones para garantir contraste com o fundo
        for control in column.controls:
            # Cada item da navbar é um Container com Row contendo IconButton e Text
            if isinstance(control, Container) and isinstance(control.content, Row):
                icon_button = control.content.controls[0]
                if isinstance(icon_button, IconButton):
                    # Ícones azuis no modo expandido, brancos no modo recolhido
                    icon_button.icon_color = self.color_blue if self.expanded else self.color_white
                    icon_button.update()

        # Ajusta o ícone do botão de menu (toggle) para ficar visível
        menu_button = column.controls[1]  # Geralmente o segundo item é o botão menu
        if isinstance(menu_button, Container) and isinstance(menu_button.content, Icon):
            menu_button.content.color = self.color_blue if self.expanded else self.color_white
            menu_button.update()

        sidebar.update()

        # Mostra/esconde texto dos itens da navbar conforme estado expandido ou recolhido
        for control in column.controls:
            if isinstance(control, Container):
                if isinstance(control.content, Row) and len(control.content.controls) > 1:
                    if isinstance(control.content.controls[1], Text):
                        # Controla visibilidade e opacidade do texto do item da navbar
                        control.content.controls[1].visible = self.expanded
                        control.content.controls[1].opacity = 1 if self.expanded else 0
                        control.content.update()
                if control.content and isinstance(control.content, Column):
                    # Ajusta visibilidade e opacidade dos textos da seção UserData
                    for txt in control.content.controls:
                        txt.visible = self.expanded
                        txt.opacity = 1 if self.expanded else 0
                    control.content.update()
        column.update()

    # Monta a sidebar completa (navbar)
    def build(self):
        return Container(
            ref=sidebar_ref,
            width=200,
            bgcolor=self.color_navbar_bg_expanded,  # Fundo inicial expandido
            animate=Animation(duration=300, curve="easeInOut"),
            padding=10,
            content=Column(
                ref=sidebar_column_ref,
                alignment=MainAxisAlignment.START,
                horizontal_alignment="center",
                controls=[
                    self.UserData("DS", "Flexx Solar", "Técnico de Cadastro Solar"),  # Dados do usuário
                    Container(
                        width=24,
                        height=24,
                        bgcolor=self.color_blue,            # Fundo azul do botão menu
                        border_radius=8,
                        alignment=alignment.center,
                        on_click=self.toggle_sidebar,
                        animate=Animation(duration=300, curve="easeInOut"),
                        content=Icon(icons.MENU, size=16, color=self.color_white),  # Ícone branco do menu
                    ),
                    Divider(height=10, color="transparent"),  # Espaço entre itens
                    self.ContainedIcon(icons.SEARCH, "Pesquisar"),
                    self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Dashboard"),
                    self.ContainedIcon(icons.BAR_CHART, "Revenue"),
                    self.ContainedIcon(icons.NOTIFICATIONS, "Perfil"),
                    self.ContainedIcon(icons.PIE_CHART_OUTLINE_ROUNDED, "Configurações"),
                    self.ContainedIcon(icons.FAVORITE_ROUNDED, "Favoritos"),
                    self.ContainedIcon(icons.WALLET_ROUNDED, "Carteira"),
                    Divider(height=10, color=self.color_gray_light),
                    self.ContainedIcon(icons.LOGOUT_ROUNDED, "Sair"),
                ]
            )
        )
