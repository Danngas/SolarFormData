import flet as ft
from functools import partial

# Referências globais
sidebar_ref = ft.Ref[ft.Container]()
sidebar_column_ref = ft.Ref[ft.Column]()

class ModernNavBar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.expanded = True

        # Paleta de cores
        self.color_blue = "#005e9b"
        self.color_orange = "#ff8c0d"
        self.color_blue_light = "#4a90e2"
        self.color_gray_dark = "#333333"
        self.color_gray_medium = "#7d7d7d"
        self.color_gray_light = "#d3d3d3"
        self.color_white = "#ffffff"
        self.color_black_soft = "#121212"
        self.color_navbar_bg_expanded = "#e7eaf0"
        self.color_navbar_bg_collapsed = "#005e9b"
        self.color_orange_hover = "#4caf50"
        self.color_error = "#f44336"
        self.color_success = "#4caf50"

    def HighLight(self, e):
        if e.data == 'true':
            e.control.bgcolor = self.color_orange_hover
            e.control.update()
            e.control.content.controls[0].icon_color = self.color_white
            if len(e.control.content.controls) > 1:
                e.control.content.controls[1].color = self.color_white
                e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            icon_color = self.color_blue if self.expanded else self.color_white
            e.control.content.controls[0].icon_color = icon_color
            if len(e.control.content.controls) > 1:
                e.control.content.controls[1].color = self.color_gray_dark
                e.control.content.update()

    def UserData(self, initials: str, name: str, description: str):
        return ft.Container(
            visible=self.expanded,
            animate_opacity=300,
            opacity=1 if self.expanded else 0,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=42,
                        height=42,
                        bgcolor=self.color_blue,
                        alignment=ft.alignment.center,
                        border_radius=8,
                        content=ft.Text(
                            value=initials,
                            size=20,
                            weight="bold",
                            color=self.color_white,
                        ),
                    ),
                    ft.Column(
                        spacing=1,
                        alignment="center",
                        controls=[
                            ft.Text(
                                value=name,
                                size=11,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200,
                                color=self.color_blue
                            ),
                            ft.Text(
                                value=description,
                                size=10,
                                weight='w400',
                                color=self.color_gray_medium,
                                opacity=1,
                                animate_opacity=200,
                            )
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str, route: str):
        return ft.Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.page.go(route),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color=self.color_blue,
                        style=ft.ButtonStyle(
                            shape={"": ft.RoundedRectangleBorder(radius=7)},
                            overlay_color={"": "Transparent"},
                        ),
                    ),
                    ft.Text(
                        value=text,
                        color=self.color_gray_dark,
                        size=12,
                        visible=self.expanded,
                        animate_opacity=300,
                        opacity=1 if self.expanded else 0
                    ),
                ]
            ),
        )

    def toggle_sidebar(self, e):
        self.expanded = not self.expanded
        sidebar = sidebar_ref.current
        column = sidebar_column_ref.current
        sidebar.width = 200 if self.expanded else 60
        sidebar.bgcolor = self.color_navbar_bg_expanded if self.expanded else self.color_navbar_bg_collapsed

        # Atualiza UserData
        user_data = column.controls[0]
        if isinstance(user_data, ft.Container):
            user_data.visible = self.expanded
            user_data.opacity = 1 if self.expanded else 0
            user_data.update()

        # Atualiza cor dos ícones
        for control in column.controls:
            if isinstance(control, ft.Container) and isinstance(control.content, ft.Row):
                icon_button = control.content.controls[0]
                if isinstance(icon_button, ft.IconButton):
                    icon_button.icon_color = self.color_blue if self.expanded else self.color_white
                    icon_button.update()

        # Atualiza botão de menu
        menu_button = column.controls[1]
        if isinstance(menu_button, ft.Container) and isinstance(menu_button.content, ft.Icon):
            menu_button.content.color = self.color_blue if self.expanded else self.color_white
            menu_button.update()

        sidebar.update()

        # Ajusta visibilidade dos textos
        for control in column.controls:
            if isinstance(control, ft.Container):
                if isinstance(control.content, ft.Row) and len(control.content.controls) > 1:
                    if isinstance(control.content.controls[1], ft.Text):
                        control.content.controls[1].visible = self.expanded
                        control.content.controls[1].opacity = 1 if self.expanded else 0
                        control.content.update()
                if control.content and isinstance(control.content, ft.Column):
                    for txt in control.content.controls:
                        txt.visible = self.expanded
                        txt.opacity = 1 if self.expanded else 0
                    control.content.update()
        column.update()

    def build(self):
        return ft.Container(
            ref=sidebar_ref,
            width=200,
            bgcolor=self.color_navbar_bg_expanded,
            animate=ft.Animation(duration=300, curve="easeInOut"),
            padding=10,
            content=ft.Column(
                ref=sidebar_column_ref,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment="center",
                controls=[
                    self.UserData("DS", "Flexx Solar", "Técnico de Cadastro Solar"),
                    ft.Container(
                        width=24,
                        height=24,
                        bgcolor=self.color_blue,
                        border_radius=8,
                        alignment=ft.alignment.center,
                        on_click=self.toggle_sidebar,
                        animate=ft.Animation(duration=300, curve="easeInOut"),
                        content=ft.Icon(ft.icons.MENU, size=16, color="white"),
                    ),
                    ft.Divider(height=10, color="transparent"),
                    self.ContainedIcon(ft.icons.SEARCH, "Pesquisar", "/search"),
                    self.ContainedIcon(ft.icons.DASHBOARD_ROUNDED, "Dashboard", "/dashboard"),
                    self.ContainedIcon(ft.icons.BAR_CHART, "Revenue", "/revenue"),
                    self.ContainedIcon(ft.icons.NOTIFICATIONS, "Perfil", "/perfil"),
                    self.ContainedIcon(ft.icons.PIE_CHART_OUTLINE_ROUNDED, "Configurações", "/configuracoes"),
                    self.ContainedIcon(ft.icons.FAVORITE_ROUNDED, "Favoritos", "/favoritos"),
                    self.ContainedIcon(ft.icons.WALLET_ROUNDED, "Carteira", "/carteira"),
                    ft.Divider(height=10, color=self.color_gray_light),
                    self.ContainedIcon(ft.icons.LOGOUT_ROUNDED, "Sair", "/logout"),
                ]
            )
        )