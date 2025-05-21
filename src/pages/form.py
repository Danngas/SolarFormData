import flet as ft

def main(page: ft.Page):
    page.title = "SolarFormData - Formulário de Homologação"
    page.bgcolor = "#F0F4F8"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Estado para validação
    errors = {}

    # Função para validar campos obrigatórios
    def validate_field(field, value, label):
        if not value and field.required:
            errors[field] = f"{label} é obrigatório"
            field.border_color = ft.colors.RED
        else:
            errors.pop(field, None)
            field.border_color = "#007BFF"
        page.update()

    # Função para validar uploads
    def validate_upload(e: ft.FilePickerResultEvent, field, label):
        if not e.files and field.required:
            errors[field] = f"{label} é obrigatório"
            page.add(ft.Text(f"Erro: {label} é obrigatório", color=ft.colors.RED))
        elif e.files:
            file = e.files[0]
            if file.size > 10 * 1024 * 1024:  # 10 MB
                errors[field] = f"{label} excede 10 MB"
                page.add(ft.Text(f"Erro: {label} excede 10 MB", color=ft.colors.RED))
            elif not file.name.lower().endswith((".pdf", ".png", ".jpg", ".jpeg")):
                errors[field] = f"{label} deve ser PDF ou imagem"
                page.add(ft.Text(f"Erro: {label} deve ser PDF ou imagem", color=ft.colors.RED))
            else:
                errors.pop(field, None)
                page.add(ft.Text(f"Arquivo selecionado: {file.name}", color=ft.colors.GREEN))
        page.update()

    # Função de envio do formulário
    def submit_form(e):
        # Validar todos os campos obrigatórios
        for field, label in required_fields:
            validate_field(field, field.value, label)
        for picker, label in required_uploads:
            if not picker.result or not picker.result.files:
                errors[picker] = f"{label} é obrigatório"
                page.add(ft.Text(f"Erro: {label} é obrigatório", color=ft.colors.RED))
        if errors:
            page.add(ft.Text("Por favor, corrija os erros antes de enviar.", color=ft.colors.RED))
        else:
            page.add(ft.Text("Formulário enviado com sucesso!", color=ft.colors.GREEN))
        page.update()

    # Campos do formulário
    responsible_name = ft.TextField(
        label="Responsável pelo Envio", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(responsible_name, e.control.value, "Responsável pelo Envio")
    )
    responsible_email = ft.TextField(
        label="E-mail", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(responsible_email, e.control.value, "E-mail")
    )
    client_name = ft.TextField(
        label="Nome do Cliente/Nome Fantasia", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(client_name, e.control.value, "Nome do Cliente")
    )
    client_type = ft.Dropdown(
        label="Pessoa Física ou Jurídica", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        options=[
            ft.dropdown.Option("Física"),
            ft.dropdown.Option("Jurídica")
        ],
        on_change=lambda e: validate_field(client_type, e.control.value, "Tipo de Pessoa")
    )
    client_cpf_cnpj = ft.TextField(
        label="CPF/CNPJ", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(client_cpf_cnpj, e.control.value, "CPF/CNPJ")
    )
    client_address = ft.TextField(
        label="Endereço da Instalação", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(client_address, e.control.value, "Endereço")
    )
    client_contact = ft.TextField(
        label="Contato do Cliente", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(client_contact, e.control.value, "Contato")
    )
    client_id_upload = ft.FilePicker(on_result=lambda e: validate_upload(e, client_id_upload, "RG/CNH/Cartão CNPJ"))
    client_id_button = ft.ElevatedButton("Selecionar RG/CNH/Cartão CNPJ", bgcolor="#007BFF", color="#FFFFFF")
    installation_load = ft.TextField(
        label="Carga Instalada (kW)", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(installation_load, e.control.value, "Carga Instalada")
    )
    voltage_supply = ft.Dropdown(
        label="Tensão de Fornecimento", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        options=[
            ft.dropdown.Option("Monofásico 220"),
            ft.dropdown.Option("Bifásico 127/220"),
            ft.dropdown.Option("Trifásico 127/220"),
            ft.dropdown.Option("Trifásico 220/380")
        ],
        on_change=lambda e: validate_field(voltage_supply, e.control.value, "Tensão de Fornecimento")
    )
    client_classification = ft.Dropdown(
        label="Classificação do Cliente", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        options=[
            ft.dropdown.Option("B1 - Residencial"),
            ft.dropdown.Option("B1 - Residencial Baixa Renda"),
            ft.dropdown.Option("B1 - Residencial Baixa Renda Indígena e Quilombola"),
            ft.dropdown.Option("B2 - Rural / Cooperativa de Eletrificação Rural"),
            ft.dropdown.Option("B2 - Rural Irrigante / Serviço Público de Irrigação"),
            ft.dropdown.Option("B3 - Comercial, Serviços e Outras Atividades"),
            ft.dropdown.Option("B3 - Serviço Público de Água, Esgoto e Saneamento"),
            ft.dropdown.Option("B4A - Rede de Distribuição")
        ],
        on_change=lambda e: validate_field(client_classification, e.control.value, "Classificação do Cliente")
    )
    installation_code = ft.TextField(
        label="Código do Local de Instalação", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(installation_code, e.control.value, "Código do Local de Instalação")
    )
    compensation_codes = [
        ft.TextField(label=f"Código de Compensação {i+1}", bgcolor="#FFFFFF", border_color="#007BFF")
        for i in range(10)
    ]
    installation_account_upload = ft.FilePicker(
        on_result=lambda e: validate_upload(e, installation_account_upload, "Conta da Instalação")
    )
    installation_account_button = ft.ElevatedButton("Selecionar Conta da Instalação", bgcolor="#007BFF", color="#FFFFFF")
    compensation_account_uploads = [
        ft.FilePicker(on_result=lambda e, i=i: validate_upload(e, compensation_account_uploads[i], f"Conta da Compensação {i+1}"))
        for i in range(10)
    ]
    compensation_account_buttons = [
        ft.ElevatedButton(f"Selecionar Conta da Compensação {i+1}", bgcolor="#007BFF", color="#FFFFFF")
        for i in range(10)
    ]
    quotation_upload = ft.FilePicker(
        on_result=lambda e: validate_upload(e, quotation_upload, "Cotação do Sistema")
    )
    quotation_button = ft.ElevatedButton("Selecionar Cotação do Sistema", bgcolor="#FFFFFF", color="#007BFF")
    generation_kwh = ft.TextField(
        label="Geração em kWh", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(generation_kwh, e.control.value, "Geração em kWh")
    )
    inverter_1 = ft.TextField(
        label="Inversor 1 (Quantidade/Marca/Potência/Modelo)", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(inverter_1, e.control.value, "Inversor 1")
    )
    inverter_2 = ft.TextField(label="Inversor 2 (Quantidade/Marca/Potência/Modelo)", bgcolor="#FFFFFF", border_color="#007BFF")
    inverter_3 = ft.TextField(label="Inversor 3 (Quantidade/Marca/Potência/Modelo)", bgcolor="#FFFFFF", border_color="#007BFF")
    panels = ft.TextField(
        label="Placas (Marca/Modelo/Quantidade/kWp)", bgcolor="#FFFFFF", border_color="#007BFF", required=True,
        on_change=lambda e: validate_field(panels, e.control.value, "Placas")
    )
    battery = ft.TextField(label="Bateria (Quantidade/Modelo)", bgcolor="#FFFFFF", border_color="#007BFF")

    # Lista de campos obrigatórios
    required_fields = [
        (responsible_name, "Responsável pelo Envio"),
        (responsible_email, "E-mail"),
        (client_name, "Nome do Cliente"),
        (client_type, "Tipo de Pessoa"),
        (client_cpf_cnpj, "CPF/CNPJ"),
        (client_address, "Endereço"),
        (client_contact, "Contato"),
        (installation_load, "Carga Instalada"),
        (voltage_supply, "Tensão de Fornecimento"),
        (client_classification, "Classificação do Cliente"),
        (installation_code, "Código do Local de Instalação"),
        (generation_kwh, "Geração em kWh"),
        (inverter_1, "Inversor 1"),
        (panels, "Placas")
    ]
    required_uploads = [
        (client_id_upload, "RG/CNH/Cartão CNPJ"),
        (installation_account_upload, "Conta da Instalação")
    ]

    # Montar a interface
    page.add(
        ft.Image(src="assets/logo.png", width=150, height=50),  # Substitua por seu logo
        ft.Text("Formulário para Homologação de Sistemas Fotovoltaicos", size=24, weight=ft.FontWeight.BOLD, color="#007BFF"),
        ft.Text("Preencha todos os campos obrigatórios (*) com atenção.", size=16, color="#000000"),
        ft.Divider(),
        ft.Text("Responsável pelo Envio", size=18, weight=ft.FontWeight.BOLD),
        responsible_name,
        responsible_email,
        ft.Divider(),
        ft.Text("Dados do Cliente", size=18, weight=ft.FontWeight.BOLD),
        client_name,
        client_type,
        client_cpf_cnpj,
        client_address,
        client_contact,
        ft.Row([client_id_button, client_id_upload]),
        ft.Divider(),
        ft.Text("Dados da Instalação", size=18, weight=ft.FontWeight.BOLD),
        installation_load,
        voltage_supply,
        client_classification,
        ft.Divider(),
        ft.Text("Dados das Contas de Energia", size=18, weight=ft.FontWeight.BOLD),
        installation_code,
        *compensation_codes,
        ft.Row([installation_account_button, installation_account_upload]),
        *[ft.Row([compensation_account_buttons[i], compensation_account_uploads[i]]) for i in range(10)],
        ft.Divider(),
        ft.Text("Dados do Sistema Solar", size=18, weight=ft.FontWeight.BOLD),
        ft.Row([quotation_button, quotation_upload]),
        generation_kwh,
        inverter_1,
        inverter_2,
        inverter_3,
        panels,
        battery,
        ft.ElevatedButton("Enviar Formulário", bgcolor="#007BFF", color="#FFFFFF", on_click=submit_form)
    )

ft.app(target=main)