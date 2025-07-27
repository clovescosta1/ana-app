# Manual do Usuário - Aplicativo ViralVideoApp

## 1. Introdução

Bem-vindo ao ViralVideoApp! Este aplicativo permite gerenciar usuários, fazer upload de vídeos, obter sugestões de conteúdo viral e, para acesso completo, requer a ativação de uma chave de licença fornecida pelo administrador.

Este manual guiará você pelas funcionalidades principais, incluindo o processo de ativação de licença.

## 2. Pré-requisitos para Execução Local

Para executar este protótipo em sua máquina local, siga as instruções detalhadas na seção "Como Executar o MVP Localmente" do arquivo `README.md`.

## 3. Funcionalidades Principais

### 3.1. Registro de Conta

1.  Acesse a página inicial.
2.  Clique no botão "Registrar".
3.  Preencha o formulário com seu nome de usuário, email, senha e confirmação de senha.
4.  Clique em "Criar Conta".
5.  Você será redirecionado para a página de login.

### 3.2. Login

1.  Acesse a página de login.
2.  Insira seu email e senha cadastrados.
3.  Clique em "Login".
4.  Se você não tiver uma licença ativa, será direcionado para a página de ativação de licença.

### 3.3. Ativação de Licença

Após o login, se sua conta não possuir uma licença ativa ou se sua licença anterior expirou, você será direcionado para a página "Ativar Licença".

1.  Insira a chave de liberação fornecida pelo administrador no campo "Chave de Licença".
2.  Clique em "Ativar Chave".
3.  Se a chave for válida e ativada com sucesso, você verá uma mensagem de confirmação com a data de validade da sua licença e será redirecionado para a página inicial do aplicativo.
4.  Se houver algum erro (chave inválida, já utilizada, etc.), uma mensagem de erro será exibida.

### 3.4. Página Inicial (Logado e Licenciado)

Após o login e ativação da licença, a página inicial mostrará uma mensagem de boas-vindas e opções para:
*   **Fazer Upload de Vídeo**: Leva para a página de upload.
*   **Ver Meu Perfil**: Leva para a sua página de perfil.
*   **Status da Licença**: Leva para a página onde você pode verificar os detalhes da sua licença ativa.

### 3.5. Perfil do Usuário

Acessível pelo link "Perfil" na barra de navegação.

Nesta página, você pode:
*   Ver seu nome de usuário e email.
*   **Conectar Contas de Mídia Social (Simulado):** Funcionalidade para conectar com YouTube e Instagram (simulada no estado atual).

### 3.6. Status da Licença

Acessível pelo link "Status da Licença" na barra de navegação ou no perfil.

Nesta página, você pode visualizar:
*   O status atual da sua licença (Ativa, Expirada, Sem Licença).
*   A chave de licença que está ativa (se houver).
*   A data de ativação.
*   A data de expiração da sua licença.

### 3.7. Upload de Vídeo (Requer Licença Ativa)

1.  Acesse a página "Upload de Vídeo" pela barra de navegação.
2.  Opcionalmente, insira um título para o seu vídeo.
3.  Clique em "Escolher arquivo" e selecione um arquivo de vídeo do seu computador.
4.  Clique em "Enviar Vídeo".
5.  **Obter Sugestões de Conteúdo:** Antes ou depois de selecionar o arquivo, você pode inserir um título e clicar em "Obter Sugestões de Conteúdo" para receber ideias baseadas em análise de texto e tendências.

### 3.8. Meus Vídeos (Requer Licença Ativa)

Acessível pelo link "Meus Vídeos" na barra de navegação.

Nesta página, você verá uma lista dos vídeos que enviou.

### 3.9. Logout

1.  Clique no link "Logout" na barra de navegação.
2.  Você será desconectado e redirecionado para a página inicial.

## 4. Limitações Importantes

*   **Processamento de Vídeo e Publicação:** Muitas funcionalidades avançadas de processamento e publicação direta são simuladas ou simplificadas nesta versão.
*   **Segurança:** Medidas de segurança avançadas (além do básico para login e licenciamento) podem não estar totalmente implementadas.

## 5. Suporte

Para dúvidas ou problemas, consulte a documentação (`README.md`) ou o administrador do sistema.

