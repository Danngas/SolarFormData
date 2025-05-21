# Cronograma do Projeto SolarFormData

Este documento detalha o cronograma de desenvolvimento do projeto **SolarFormData**, um sistema web para coleta e gerenciamento de documentos de homologação de sistemas fotovoltaicos. O projeto visa otimizar o processo de 10-50 projetos por mês, substituindo o Google Forms com uma interface personalizada, automações (Google Drive, Sheets) e notificações automáticas.

## Objetivo
- Desenvolver um sistema web com Flet (Python + Flutter) que resolva os gargalos de:
  - Trabalho manual ao cobrar documentos faltantes.
  - Falta de personalização no processo atual.
- Prazo total estimado: **6-8 semanas** (início em 21/05/2025, entrega prevista entre 02/07/2025 e 16/07/2025).
- Divisão em 4 sprints, com entregáveis testáveis a cada etapa.

## Cronograma

### Sprint 1: Formulário Personalizado (Semanas 1-2, 21/05/2025 - 03/06/2025)
**Objetivo:** Criar o formulário web para coleta de dados e documentos, com design personalizado e validação de campos.

**Tarefas:**
- Configurar ambiente de desenvolvimento (Python, Flet, ambiente virtual).
- Desenvolver formulário com Flet, incluindo:
  - Campos do Google Forms atual: responsável (nome, e-mail), dados do cliente (nome, CPF/CNPJ, endereço, contato, upload RG/CNH), códigos (instalação e compensação dinâmica), contas de energia (upload múltiplo), especificações técnicas (kWh, inversores, placas, bateria).
  - Validação de campos obrigatórios (ex.: destacar campos não preenchidos).
  - Design com logo da empresa, cores (azul #007BFF, branco #FFFFFF, cinza #F0F4F8).
- Testar formulário localmente (`python main.py`).
- Versionar código no GitHub (`src/pages/form.py`).

**Entregáveis:**
- Formulário funcional rodando localmente.
- Código inicial em `src/pages/form.py`.
- Documentação básica em `docs/setup.md` (instruções de execução local).

**Duração:** 2 semanas.

---

### Sprint 2: Automação de Dados (Semanas 3-4, 04/06/2025 - 17/06/2025)
**Objetivo:** Integrar o formulário com Google Drive e Sheets para organização automática de arquivos e dados.

**Tarefas:**
- Configurar Google Drive API e Google Sheets API (credenciais em `token.json`).
- Implementar salvamento de arquivos no Google Drive:
  - Criar pastas por projeto (ex.: `Projetos/Cliente_Nome_Projeto_2025`).
  - Nomear arquivos automaticamente (ex.: `ClienteX_Proj001_ContaInstalacao.pdf`).
- Integrar Google Sheets:
  - Registrar envios numa planilha com colunas: Cliente, Projeto ID, E-mail, Status, Documentos Enviados/Faltantes, Data.
- Testar automações com envios simulados.
- Versionar código no GitHub (`src/services/drive.py`, `src/services/sheets.py`).

**Entregáveis:**
- Integração funcional com Google Drive e Sheets.
- Código em `src/services/drive.py` e `src/services/sheets.py`.
- Atualização em `docs/api_keys.md` com instruções para APIs.

**Duração:** 2 semanas.

---

### Sprint 3: Dashboard de Gerenciamento (Semanas 5-6, 18/06/2025 - 01/07/2025)
**Objetivo:** Criar um dashboard com login para gerenciar projetos, com visualização de status e filtros.

**Tarefas:**
- Desenvolver tela de login com Flet (e-mail/senha).
- Criar dashboard com:
  - Tabela de projetos (Cliente, Projeto ID, Status, Documentos Enviados/Faltantes, Data).
  - Filtros (ex.: "Pendentes", "Completos").
  - Página de detalhes por projeto (mostra arquivos e permite alterar status).
- Implementar acesso restrito ao dashboard.
- Testar dashboard localmente.
- Versionar código no GitHub (`src/pages/dashboard.py`, `src/pages/login.py`).

**Entregáveis:**
- Dashboard funcional rodando localmente.
- Código em `src/pages/dashboard.py` e `src/pages/login.py`.
- Testes iniciais em `tests/test_dashboard.py`.

**Duração:** 2 semanas.

---

### Sprint 4: Notificações e Implantação (Semanas 7-8, 02/07/2025 - 16/07/2025)
**Objetivo:** Adicionar notificações automáticas e hospedar o sistema para uso real.

**Tarefas:**
- Implementar notificações:
  - E-mails de confirmação com smtplib/SendGrid (ex.: "Recebemos seus documentos").
  - Lembretes para documentos faltantes após 3 dias.
  - (Opcional) Integração com Twilio para WhatsApp, se confirmado.
- Hospedar o sistema no Render ou Heroku.
- Testar com 1-2 empresas parceiras (envios reais).
- Ajustar bugs e melhorar usabilidade com base em feedback.
- Versionar código final no GitHub (`src/services/email.py`, `src/services/notifications.py`).

**Entregáveis:**
- Sistema hospedado (ex.: `suaempresa.flet.app`).
- Notificações funcionais (e-mail, opcionalmente WhatsApp).
- Documentação final em `docs/setup.md` e `docs/api_keys.md`.
- Relatório de testes com empresas parceiras.

**Duração:** 2 semanas.

## Marcos Principais
- **03/06/2025:** Formulário funcional localmente.
- **17/06/2025:** Automação com Google Drive e Sheets concluída.
- **01/07/2025:** Dashboard funcional com login.
- **16/07/2025:** Sistema hospedado, notificações ativas e testes com empresas parceiras.

## Observações
- **Flexibilidade:** O cronograma pode ser ajustado com base em feedback ou complexidade das integrações.
- **Testes:** Cada sprint inclui testes locais; testes reais com empresas ocorrem na Sprint 4.
- **Custo:** Hospedagem inicial grátis (Render/Heroku). Twilio (WhatsApp) tem custo (~R$0,10 por mensagem), a confirmar.
- **Documentação:** Cada sprint atualiza `docs/` com instruções claras.
- **Segurança:** Arquivos sensíveis (`token.json`, `credentials.json`) protegidos via `.gitignore`.

## Próximos Passos
- Configurar repositório com estrutura inicial (`src/`, `tests/`, `docs/`).
- Iniciar Sprint 1: desenvolvimento do formulário com Flet.
- Atualizar README com screenshots e links pessoais (LinkedIn, site da empresa).