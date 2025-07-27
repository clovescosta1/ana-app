import os
<<<<<<< HEAD

SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_here'
=======
from flask import Flask, render_template_string

# Define a classe de configuração
class Config:
    """
    Classe de configuração para o aplicativo Flask.
    Ela recupera informações sensíveis como SECRET_KEY e DATABASE_URL
    de variáveis de ambiente para melhor segurança e flexibilidade.
    Se as variáveis de ambiente não estiverem definidas, ela usa valores padrão.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-muito-importante-para-mudar'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
   {% extends "base.html" %}

{% block content %}
<h2>Login</h2>
<form method="POST" action="{{ url_for('auth.login') }}">
    {{ form.hidden_tag() }}
    <div>
        <label>Email:</label>
        <input type="email" name="email" required>
    </div>
    <div>
        <label>Senha:</label>
        <input type="password" name="password" required>
    </div>
    <button type="submit">Entrar</button>
</form>
{% endblock %}
>>>>>>> 9b5a5907ae3115f2057f08419bf74521c0cf48a4
