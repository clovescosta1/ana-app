# Guia do Administrador - Aplicativo ViralVideoApp

## 1. Introdução

Bem-vindo ao Painel Administrativo do ViralVideoApp! Este guia destina-se aos administradores do sistema e descreve como gerenciar usuários, chaves de licença e outras configurações do aplicativo.

## 2. Acesso ao Painel Administrativo

1.  Certifique-se de que sua conta de usuário está configurada com permissões de administrador.
2.  Faça login no aplicativo com suas credenciais de administrador.
3.  Acesse o painel administrativo navegando para a URL `/admin` (ex: `http://localhost:5000/admin`).

## 3. Funcionalidades do Painel Administrativo

O painel administrativo oferece as seguintes funcionalidades principais:

### 3.1. Dashboard Principal (`/admin`)

*   Fornece uma visão geral e links para as principais seções de gerenciamento.

### 3.2. Gerenciar Licenças (`/admin/licenses`)

Nesta seção, você pode:
*   **Visualizar Todas as Chaves de Licença:** Uma lista paginada de todas as chaves de licença existentes no sistema, incluindo:
    *   A string da chave (`key_string`).
    *   O período de validade em dias (`validity_period_days`).
    *   O status atual da chave (`AVAILABLE`, `ACTIVE`, `EXPIRED`, `REVOKED`).
    *   A data de criação (`created_at`).
    *   O ID do usuário associado (se `ACTIVE` ou `EXPIRED`).
    *   A data de ativação (`activated_at`).
    *   A data de expiração (`expires_at`).
*   **Filtrar/Buscar Chaves:** (Funcionalidade futura potencial) Poderia incluir filtros por status, data, etc.

### 3.3. Gerar Novas Chaves de Licença (`/admin/licenses/generate`)

Permite criar novos lotes de chaves de licença:
1.  **Quantidade:** Insira o número de chaves que deseja gerar.
2.  **Validade (dias):** Defina por quantos dias a licença será válida após a ativação (ex: 30, 90, 365).
3.  Clique em "Gerar Chaves".
4.  O sistema criará as chaves com o status `AVAILABLE` e as listará na seção "Gerenciar Licenças". Uma mensagem de sucesso ou erro será exibida.

### 3.4. Revogar uma Chave de Licença

Na página "Gerenciar Licenças" (`/admin/licenses`):
1.  Localize a chave que deseja revogar na lista.
2.  Clique no botão "Revogar" associado a essa chave.
3.  Confirme a ação (se aplicável).
4.  O status da chave será alterado para `REVOKED`, e o usuário associado (se houver) perderá o acesso ao tentar usar o aplicativo ou funcionalidades protegidas.

### 3.5. Gerenciar Usuários (`/admin/users`)

Nesta seção, você pode:
*   **Visualizar Todos os Usuários:** Uma lista paginada de todos os usuários registrados no sistema, exibindo informações como ID, nome de usuário e email.
*   **Verificar Status da Licença do Usuário:** (Funcionalidade futura potencial) Poderia integrar a exibição do status da licença diretamente na lista de usuários ou em uma página de detalhes do usuário.

### 3.6. Atribuir Chave a um Usuário (`/admin/licenses/assign`)

Esta funcionalidade permite que um administrador atribua e ative diretamente uma chave `AVAILABLE` para um usuário específico:
1.  **Selecionar Chave:** Escolha uma chave com status `AVAILABLE` de uma lista suspensa ou insira a string da chave.
2.  **Selecionar Usuário:** Escolha um usuário (por email ou ID) de uma lista suspensa ou insira o email do usuário.
3.  Clique em "Atribuir e Ativar Chave".
4.  Se a chave e o usuário forem válidos e a chave estiver disponível, ela será ativada para o usuário, e seu status mudará para `ACTIVE`. A data de expiração será calculada com base no período de validade da chave.

## 4. Considerações de Segurança e Boas Práticas

*   **Credenciais de Administrador:** Mantenha as credenciais de administrador seguras e não as compartilhe.
*   **Monitoramento:** (Funcionalidade futura potencial) Implementar logs detalhados de ações administrativas pode ser útil para auditoria.
*   **Backup:** Garanta que o banco de dados do aplicativo seja regularmente sauvegardado.

## 5. Suporte

Para dúvidas ou problemas com o painel administrativo, consulte a documentação técnica do projeto ou o desenvolvedor responsável.

