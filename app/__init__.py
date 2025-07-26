from flask import Flask, render_template, request
import requests

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "AnaSync rodando!"

    @app.route("/painel")
    def painel():
        senha = request.args.get("senha")
        if senha != "sua_senha_aqui":  # Troque por sua senha
            return "Acesso negado", 403
        return render_template("painel.html")

    @app.route("/publicar")
    def publicar_post():
        dados = {
            "title": "Post automático da Ana",
            "content": "Esse post foi publicado pelo sistema AnaSync.",
            "status": "publish"
        }
        resposta = requests.post(
            "https://SEUSITE.com/wp-json/wp/v2/posts",
            json=dados,
            auth=("ana-renda-digital", "AnaCortez@2024!")
        )
        return f"Status: {resposta.status_code}"

    return app
