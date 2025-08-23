# Importa as bibliotecas necessárias para o Flask e para fazer requisições HTTP
from flask import Flask, render_template, request, jsonify
import requests
import os

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota principal do aplicativo
@app.route("/")
def home():
    return "<h1>AnaSync está rodando!</h1><p>A rota de automação está disponível em /automation.</p>"

# Rota para a automação de publicação
@app.route("/automation", methods=["POST"])
def automate_post():
    # 1. Recebe os dados da requisição (JSON)
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({"error": "Tópico não fornecido."}), 400

    # 2. Configura a requisição para o WordPress
    # URL do seu site WordPress. Troque por sua URL real.
    wordpress_url = "https://ana-app-9ts1.onrender.com"
    # Endereço do endpoint da API REST do seu plugin
    endpoint = f"{wordpress_url}/wp-json/anasync-completo/v1/command"
    # Sua chave de API secreta. Mantenha isso seguro!
    api_key = os.environ.get("ANASYNC_API_KEY", "SUA_CHAVE_SECRETA_AQUI")

    # Payload (corpo da requisição) que será enviado para o WordPress
    payload = {
        "action": "create_and_publish",
        "topic": data['topic']
    }

    # Headers (cabeçalhos) para autenticação e tipo de conteúdo
    headers = {
        "Content-Type": "application/json",
        "X-AnaSync-API-Key": api_key
    }

    # 3. Faz a requisição HTTP POST para o WordPress
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()  # Lança um erro para códigos de status 4xx/5xx
        return jsonify(response.json()), 200
    except requests.exceptions.RequestException as e:
        # Lida com erros de requisição
        return jsonify({"error": f"Erro ao conectar com o WordPress: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
