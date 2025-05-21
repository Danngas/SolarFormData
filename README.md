# SolarFormData

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flet](https://img.shields.io/badge/Flet-0.20+-green.svg)
![Google APIs](https://img.shields.io/badge/Google%20APIs-Drive%20|%20Sheets-orange.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

Um sistema web para coleta e gerenciamento de dados e documentos necessários à homologação de sistemas fotovoltaicos junto às concessionárias de energia elétrica. Desenvolvido para otimizar o processo de 10-50 projetos por mês, substituindo formulários genéricos com uma interface personalizada, automações (Google Drive, Sheets) e notificações automáticas.

Este projeto é público para demonstrar expertise em desenvolvimento de soluções para o setor de energia solar, integrando tecnologias modernas como **Flet (Python + Flutter)**, **Google Drive/Sheets APIs** e automações de processos. Ideal para empresas que buscam eficiência e profissionalismo no gerenciamento de projetos fotovoltaicos.

## 🎯 Objetivo

O sistema resolve dois problemas principais do processo atual (baseado em Google Forms):
- **Reduzir trabalho manual:** Automatiza a organização de arquivos, registro de dados e envio de lembretes para documentos faltantes.
- **Melhorar personalização:** Oferece uma interface com a identidade visual da empresa, aumentando a percepção de profissionalismo.

## ✨ Funcionalidades

- **Formulário Personalizado:**
  - Coleta dados do cliente (nome, CPF/CNPJ, endereço, contato), códigos de instalação/compensação, contas de energia e especificações técnicas (inversores, placas, kWh).
  - Upload de arquivos (PDF/imagem, máx. 10 MB) com validação de campos obrigatórios.
  - Interface responsiva com logo e cores da empresa.

- **Automação:**
  - Arquivos salvos no Google Drive em pastas organizadas (ex.: `Projetos/Cliente_Nome_Projeto_2025`).
  - Dados registrados automaticamente no Google Sheets (ex.: cliente, status, documentos enviados).
  - Nomenclatura padronizada para arquivos (ex.: `ClienteX_Proj001_ContaInstalacao.pdf`).

- **Dashboard de Gerenciamento:**
  - Tabela com todos os projetos (Cliente, Projeto ID, Status, Documentos Enviados/Faltantes, Data).
  - Filtros (ex.: "Pendentes") e detalhes por projeto (arquivos, status).
  - Acesso restrito com login.

- **Notificações Automáticas:**
  - Confirmação de envio por e-mail (ex.: "Recebemos seus documentos para o projeto XPTO").
  - Lembretes para documentos faltantes após 3 dias (e-mail, opcionalmente WhatsApp via Twilio).

- **Segurança:**
  - HTTPS para formulário e dashboard.
  - Permissões restritas no Google Drive.
  - Login seguro para o dashboard.

## 🛠 Tecnologias

- **Flet (Python + Flutter):** Interface web responsiva.
- **Google Drive API:** Armazenamento de arquivos.
- **Google Sheets API:** Registro de dados.
- **smtplib/SendGrid:** Envio de e-mails.
- **Twilio (opcional):** Notificações via WhatsApp.
- **Hospedagem:** Render ou Heroku (escalável, com plano grátis para testes).

## 📂 Estrutura do Repositório

```
SolarFormData/
├── src/                    # Código-fonte
│   ├── pages/              # Páginas da interface
│   │   ├── form.py         # Formulário de envio
│   │   ├── dashboard.py    # Dashboard de gerenciamento
│   │   └── login.py        # Tela de login
│   ├── services/           # Lógica de backend
│   │   ├── drive.py        # Integração com Google Drive
│   │   ├── sheets.py       # Integração com Google Sheets
│   │   ├── email.py        # Envio de e-mails
│   │   └── notifications.py # Lembretes (e-mail/WhatsApp)
│   └── assets/             # Arquivos estáticos
│       ├── logo.png        # Logo da empresa
│       └── styles.css      # Estilos personalizados
├── tests/                  # Testes automatizados
│   ├── test_form.py        # Testes do formulário
│   └── test_integrations.py # Testes das APIs
├── docs/                   # Documentação
│   ├── README.md           # Este arquivo
│   ├── setup.md            # Guia de configuração
│   └── api_keys.md         # Instruções para chaves de API
├── requirements.txt        # Dependências
├── .gitignore              # Ignora arquivos sensíveis (ex.: token.json)
└── main.py                 # Ponto de entrada do app
```

## 🚀 Como Configurar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu_usuario/SolarFormData.git
   ```
2. **Instale dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure APIs:**
   - Crie um projeto no Google Cloud para Drive e Sheets APIs. Veja `docs/api_keys.md`.
   - Configure e-mail (smtplib ou SendGrid) e, opcionalmente, Twilio para WhatsApp.
4. **Adicione assets:**
   - Coloque o logo da empresa em `src/assets/logo.png`.
   - (Opcional) Ajuste estilos em `src/assets/styles.css`.
5. **Rode localmente:**
   ```bash
   python main.py
   ```
6. **Hospede o app:**
   - Use Render ou Heroku (veja `docs/setup.md` para instruções).

## 📈 Benefícios do Projeto

- **Eficiência:** Reduz o tempo gasto cobrando documentos e organizando arquivos manualmente.
- **Profissionalismo:** Interface personalizada com a marca da empresa.
- **Escalabilidade:** Suporta 10-50 projetos por mês, com possibilidade de expansão.
- **Visibilidade:** Código aberto para demonstrar habilidades em Python, Flet e automações.

## 🌟 Sobre o Desenvolvedor

Este projeto foi desenvolvido para otimizar processos no setor de energia solar, refletindo expertise em:
- Desenvolvimento web com Python e Flet.
- Integração com APIs (Google Drive, Sheets, Twilio).
- Automação de fluxos de trabalho.
- Soluções personalizadas para negócios.

Conheça mais sobre meu trabalho:
- [LinkedIn](#) *(substitua pelo seu link)*
- [Site da Empresa](#) *(substitua pelo seu site, se houver)*
- [Outros Projetos](#) *(link para outros repositórios ou portfólio)*

## 🤝 Contribuições

Contribuições são bem-vindas! Para sugerir melhorias:
1. Faça um fork do repositório.
2. Crie uma branch: `git checkout -b minha-melhoria`.
3. Envie um pull request com uma descrição clara.

Por favor, siga o guia em `docs/CONTRIBUTING.md` (a ser criado).

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.

## 📞 Contato

Para dúvidas ou parcerias, entre em contato:
- E-mail: [seu_email@exemplo.com]
- WhatsApp: [seu_numero]
- GitHub Issues: [Crie uma issue](https://github.com/seu_usuario/SolarFormData/issues)
