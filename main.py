import flet
from flet import *
from functools import partial
import time

# Ref global para a coluna da sidebar
sidebar_column_ref = Ref[Column]()

# Sidebar Class
class ModernNavBar:
    def __init__(self, func):
        self.func = func

    def HighLight(self, e):
        if e.data == 'true':
            e.control.bgcolor = "white10"
            e.control.update()
            e.control.content.controls[0].icon_color = 'white'
            e.control.content.controls[1].color = 'white'
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = 'white54'
            e.control.content.controls[1].color = 'white'
            e.control.content.update()

    def UserData(self, initials: str, name: str, description: str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor="bluegrey900",
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold",
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
                                animate_opacity=200
                            ),
                            Text(
                                value=description,
                                size=10,
                                weight='w400',
                                color="white54",
                                opacity=1,
                                animate_opacity=200,
                            )
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="white54",
                        style=ButtonStyle(
                            shape={"": RoundedRectangleBorder(radius=7)},
                            overlay_color={"": "Transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=12,
                        opacity=1,
                        animate_opacity=200,
                    ),
                ]
            ),
        )

    def build(self):
        return Column(  # <- Adicionamos o Ref aqui
            ref=sidebar_column_ref,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment="center",
            controls=[
                self.UserData("DS", "Flexx Solar", "Técnico de Cadastro Solar"),
                Container(
                    width=24,
                    height=24,
                    bgcolor="bluegrey800",
                    border_radius=8,
                    on_click=partial(self.func),
                ),
                Divider(height=5, color="Transparent"),
                self.ContainedIcon(icons.SEARCH, "Pesquisar"),
                self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Dashboard"),
                self.ContainedIcon(icons.BAR_CHART, "Revenue"),
                self.ContainedIcon(icons.NOTIFICATIONS, "Perfil"),
                self.ContainedIcon(icons.PIE_CHART_OUTLINE_ROUNDED, "Configurações"),
                self.ContainedIcon(icons.FAVORITE_ROUNDED, "Favoritos"),
                self.ContainedIcon(icons.WALLET_ROUNDED, "Carteira"),
                Divider(height=5, color="white24"),
                self.ContainedIcon(icons.LOGOUT_ROUNDED, "Sair"),
            ]
        )

# main function
def main(page: Page):
    page.title = 'Flet Modern Sidebar'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def AnimateSidebar(e):
        sidebar_container = page.controls[0]
        sidebar_column = sidebar_column_ref.current  # Obtendo Column via ref

        if sidebar_container.width != 62:
            sidebar_container.width = 62
            sidebar_container.update()

            # Esconder textos
            user_data_column = sidebar_column.controls[0].content.controls[1]
            for item in user_data_column.controls:
                item.opacity = 0
                item.update()

            # Esconder texto dos ícones do menu
            for item in sidebar_column.controls[3:]:
                if isinstance(item, Container) and isinstance(item.content, Row):
                    item.content.controls[1].opacity = 0
                    item.content.update()

        else:
            sidebar_container.width = 200
            sidebar_container.update()
            time.sleep(0.2)

            # Mostrar textos novamente
            user_data_column = sidebar_column.controls[0].content.controls[1]
            for item in user_data_column.controls:
                item.opacity = 1
                item.update()

            for item in sidebar_column.controls[3:]:
                if isinstance(item, Container) and isinstance(item.content, Row):
                    item.content.controls[1].opacity = 1
                    item.content.update()

    sidebar = Container(
        width=200,
        height=580,
        bgcolor="black",
        border_radius=10,
        animate=animation.Animation(500, "decelerate"),
        alignment=alignment.center,
        padding=10,
        content=ModernNavBar(AnimateSidebar).build(),
    )

    page.add(sidebar)
    page.update()

flet.app(target=main)
