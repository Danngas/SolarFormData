from flet import *  
import flet as ft  
from src.pages.navbar import ModernNavBar, sidebar_column_ref

# Função principal que o Flet vai rodar para montar a interface
def main(page: Page):
    # Título da janela
    page.title = "Sistema Solar"
    # Cor de fundo da página (background)
    page.bgcolor = "#e8edf3"  # Aqui você pode mudar a cor de fundo geral da aplicação
    # Permitir rolagem automática da página
    page.scroll = "auto"

    # Área principal onde o conteúdo da página será exibido (dentro da coluna)
    content_area = Column()
    # Controle do estado do menu (aberto ou fechado)
    menu_aberto = True

    # Função para trocar o conteúdo da área principal e controlar o menu lateral
    def trocar_conteudo(e):
        nonlocal menu_aberto
        print(f"Evento disparado por: {e.control}")

        # Se clicou no ícone do menu (botão de recolher/expandir a sidebar)
        if hasattr(e.control, "content") and isinstance(e.control.content, Icon) and e.control.content.name == icons.MENU:
            menu_aberto = not menu_aberto
            # Altera a largura da coluna da sidebar entre 200px (expandida) e 0px (recolhida)
            sidebar_column_ref.current.width = 200 if menu_aberto else 0
            sidebar_column_ref.current.update()
            return

        # Se clicou em algum item do menu
        if e.control.content and hasattr(e.control.content, "controls") and len(e.control.content.controls) > 1:
            # Pega o texto do item clicado, converte para minúsculas para identificar a página
            nome_pagina = e.control.content.controls[1].value.lower()
            print(f"Página selecionada: {nome_pagina}")
            # Limpa o conteúdo atual e adiciona uma mensagem com o nome da página selecionada
            content_area.controls.clear()
            content_area.controls.append(
                Text(f"Você está na página: {nome_pagina}", color="white")  # Texto exibido na área principal, cor branca
            )
            page.update()
        else:
            print("Elemento sem conteúdo acessível.")
            
           
                        

    # Cria o objeto ModernNavBar, passando a função trocar_conteudo para manipular eventos do menu
    nav = ModernNavBar(func=trocar_conteudo)

    # Monta a página adicionando uma linha com 3 controles:
    # 1. A navbar lateral
    # 2. Uma linha vertical divisória
    # 3. A área de conteúdo (expandida para ocupar o restante do espaço)
    page.add(
        Row(
            controls=[
                nav.build(),  # Monta e insere a navbar lateral
                VerticalDivider(width=1, color="black"),  # Linha divisória preta vertical
                Container(content=content_area, padding=20, expand=True)  # Área principal do conteúdo
            ]
        )
    )

# Inicializa o app Flet com a função main como alvo
ft.app(target=main)
