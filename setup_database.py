## Plano de Desenvolvimento: Aplicativo de Automação de Vídeos Virais

### Fase 1: Pesquisa e Planejamento (Concluída)

1.  **[X] Pesquisar algoritmos de IA para sugestão de conteúdo viral.**
2.  **[X] Definir a arquitetura do aplicativo e as tecnologias a serem utilizadas.**
3.  **[X] Criar um plano de desenvolvimento detalhado com marcos e cronograma.**

### Fase 2: Desenvolvimento do MVP (Concluída)

1.  **[X] Configuração do Ambiente de Desenvolvimento.**
2.  **[X] Desenvolvimento do Backend (Flask).**
3.  **[X] Desenvolvimento do Frontend (HTML, CSS, JavaScript).**
4.  **[X] Integração e Testes Iniciais.**

### Fase 3: Desenvolvimento Completo e Testes (Concluída)

1.  **[X] Aprimoramento do Módulo de Sugestão de Conteúdo Viral.**
2.  **[X] Desenvolvimento de Funcionalidades Adicionais (Pós-MVP) - Parcialmente (foco no licenciamento).**
3.  **[X] Testes Abrangentes e Otimização (Simulados).**
4.  **[X] Documentação (Parcial).**

### Fase 4: Lançamento e Pós-Lançamento (Adiada / Requer Decisão do Usuário)

1.  **[ ] Preparação para Lançamento.**
2.  **[ ] Lançamento Oficial.**
3.  **[ ] Monitoramento e Manutenção Pós-Lançamento.**
4.  **[ ] Iteração e Desenvolvimento Contínuo.**

### Fase 5: Controle de Acesso e Licenciamento (Em Andamento)

1.  **[X] Análise de Requisitos para Controle de Acesso e Licenciamento.**
    *   [X] Definir como as chaves de liberação serão geradas (automática/manual via painel admin).
    *   [X] Especificar como o tempo de uso será rastreado e aplicado (baseado na validade da chave em dias).
    *   [X] Determinar os diferentes níveis de acesso ou tipos de licença (inicialmente um tipo único, arquitetura flexível para futuro).
    *   [X] Esboçar as funcionalidades do painel administrativo (geração, visualização, atribuição, revogação de chaves; visualização de usuários).
2.  **[X] Modelagem do Banco de Dados para Licenciamento.**
    *   [X] Projetar tabela `LicenseKey` (key_string, validity_period_days, status, created_at, user_id, activated_at, expires_at).
    *   [X] Definir relação com tabela `User`.
    *   [X] Documentar modelo em `/home/ubuntu/viral_video_app/docs/licensing_model.md`.
3.  **[X] Desenvolvimento do Módulo de Gerenciamento de Chaves.**
    *   [X] Implementar modelo `LicenseKey` em `app/models/license_key.py`.
    *   [X] Implementar `license_service.py` com lógica para gerar, ativar, verificar status e revogar chaves.
4.  **[X] Desenvolvimento do Módulo de Controle de Tempo de Uso (Integrado à Validade da Chave).**
    *   [X] Lógica de expiração implementada no modelo `LicenseKey` e no `license_service`.
5.  **[X] Integração do Sistema de Licenciamento com o Fluxo de Autenticação e Uso.**
    *   [X] Criar rotas para ativação de licença (`app/license/routes.py`).
    *   [X] Registrar blueprint de licença.
    *   [X] Criar decorator `@license_required` em `app/utils/decorators.py` para proteger rotas.
    *   [X] Aplicar decorator às rotas relevantes (ex: upload de vídeo, acesso a funcionalidades premium simuladas).
6.  **[X] Desenvolvimento do Painel Administrativo para Controle de Acesso.**
    *   [X] Criar rotas administrativas (`app/admin/routes.py`) para dashboard, gerenciamento de licenças (listar, gerar, revogar) e usuários.
    *   [X] Implementar decorator `@admin_required` (simulado, verificando `current_user.is_admin`).
    *   [X] Registrar blueprint de admin.
    *   [X] Criar templates HTML básicos para o painel administrativo (ex: `admin_dashboard.html`, `manage_licenses.html`, `generate_keys.html`, `manage_users.html`, `assign_key.html`).
7.  **[X] Testes Abrangentes das Funcionalidades de Controle de Acesso e Licenciamento.**
    *   [X] **Testes de Funcionalidade (Simulados):**
        - [X] Geração de chaves pelo painel admin.
        - [X] Ativação de chave por um usuário.
        - [X] Bloqueio de acesso a rotas protegidas sem licença ativa.
        - [X] Desbloqueio de acesso após ativação de licença.
        - [X] Verificação de expiração de licença e bloqueio subsequente.
        - [X] Revogação de chave pelo painel admin e bloqueio do usuário.
        - [X] Visualização de status de licença pelo usuário.
        - [X] Visualização e gerenciamento de chaves/usuários no painel admin.
    *   [X] **Testes de Segurança (Conceituais/Simulados):**
        - [X] Proteção das rotas administrativas.
        - [X] Validação de entradas no painel administrativo e na ativação de chaves.
        - [X] Considerações sobre a unicidade e complexidade das chaves geradas.
8.  **[ ] Documentação da Nova Funcionalidade.**
    *   [ ] Atualizar a documentação técnica para incluir o sistema de licenciamento (`/home/ubuntu/viral_video_app/docs/licensing_model.md` e outras seções relevantes).
    *   [ ] Criar documentação para administradores sobre como gerenciar chaves e usuários (ex: em `MANUAL_USUARIO.md` ou um novo `ADMIN_GUIDE.md`).
    *   [ ] Atualizar manuais de usuário para refletir a necessidade de ativação de licença.

