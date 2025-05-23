# modules
import flet
from flet import *
from functools import partial
import time

# Sidebar Class


class ModernNavBar(UserControl):
    def __init__(self, func):
        self.func = func
        super().__init__()

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
                            value=initials,  # aqui muda para o usuario
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
                                animate_opacity=200
                            )

                        ]
                    )
                ]
            )
        )

    # now for the main sidebar e adicionar icones

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
                            shape={
                                "": RoundedRectangleBorder(radius=7),

                            },
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
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment="center",
                controls=[
                    self.UserData("DS", "Flexx Solar",
                                  "Técnico de Cadastro Solar"),
                    # mudar para transparent


                    # minimizar e expandir navbar
                    Container(
                        width=24,
                        height=24,
                        bgcolor="bluegrey800",
                        border_radius=8,
                        on_click=partial(self.func),
                    ),

                    Divider(height=5, color="Transparent"),
                    self.ContainedIcon(icons.SEARCH, "Pesquisar"),
                    self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Dashhboard"),
                    self.ContainedIcon(icons.BAR_CHART, "Revenue"),

                    # Divider(height=5, color="White54"),  # mudar para transparent
                    self.ContainedIcon(icons.NOTIFICATIONS, "Perfil"),
                    self.ContainedIcon(
                        icons.PIE_CHART_OUTLINE_ROUNDED, "Configuracoes"),
                    self.ContainedIcon(
                        icons.FAVORITE_ROUNDED, "Configuracoes"),
                    self.ContainedIcon(icons.WALLET_ROUNDED, "Sair"),
                    Divider(height=5, color="white24"),
                    self.ContainedIcon(icons.LOGOUT_ROUNDED, "Sair"),

                ]
            ),

        )


# main function
def main(page: Page):
    # title
    page.title = 'Flet Modern Sidebar'

    # alignemnts
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def AnimateSidebar(e):
        if page.controls[0].width != 62:
            page.controls[0].width = 62
            page.controls[0].update()
        
        else:
            page.controls[0].width = 200
            page.controls[0].update()
            time.sleep(0.2)
                
            for item in(
                page.controls[0]
                .content.controls[0]
                .content.controls[0]
                .content.controls[1]
                .controls[:]
            ):
                item.opacity = 1
                item.update()
            
            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items,Container):
                    items.content.controls[1].opacity = 1
                    items.content.update()    
               
    
    # add class to page
    page.add(
        Container(
            width=200,
            height=580,
            bgcolor="black",
            border_radius=10,
            animate=animation.Animation(500, "decelerate"),  # animate
            alignment=alignment.center,
            padding=10,
            content=ModernNavBar(AnimateSidebar),
        )

    )

    page.update()


flet.app(target=main)
