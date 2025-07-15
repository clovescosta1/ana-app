from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "AnaSync rodando!"

@app.route("/ana")
def ana():
    return {
        "nome": "Ana Cortez",
        "versão": "1.0",
        "função": "Gerar vídeos, postar em redes e vender como afiliada"
    }

@app.route("/status")
def status():
    return {
        "status": "online",
        "servidor": "Render",
        "app": "AnaSync"
    }

@app.route("/comando")
def comando():
    token = request.args.get("token")
    if token != "AnaCortez@2025":
        return {"erro": "Acesso negado"}, 401
    return {
        "resposta": "Comando recebido com sucesso!",
        "status": "Ana executando",
        "ação": "Monitorar redes e gerar conteúdo"
    }

@app.route("/video")
def gerar_video():
    return {
        "status": "iniciado",
        "mensagem": "Vídeo IA em produção...",
        "plataforma": "Instagram Reels",
        "categoria": "Vendas afiliadas"
    }

@app.route("/publicar")
def publicar():
    return {
        "resultado": "Postagem simulada com sucesso!",
        "canal": "Instagram @ana.cortez.oficial",
        "tipo": "Vídeo de vendas",
        "produto": "Hotmart ou Shopee"
    }

@app.route("/postar")
def postar_no_facebook():
    token = "EAAK2rsOkjJwBPHLhdeaaQYdGIchZAdBWdN158EFP03VdxNrhSWvkcvZAvv7ZBggW0IokmoquO2mD4aQHLqvyfU4r7BaDcU751104g4w8kfanP6ZAaPy3KE4pzYnz2Bz78qZCG0ZAK7e1GtPLSmBAcx2iPUhQFa0ecZAKCJUyXZB8hJJdXnIvbxJJyTTTfinmaEXI"
    page_id = "696506866878148"  # ID da página Ana Cortezas

    mensagem = """
    🤖 Olá! Eu sou a AnaSync, sua IA de renda digital.
    Esta é minha **publicação automática** no Facebook!

    Siga a página Ana Cortezas para ver vídeos de vendas e ideias com IA para ganhar dinheiro.

    #AnaCortez #RendaDigital #IA #Afiliados
    """

    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        "message": mensagem.strip(),
        "access_token": token
    }

    resposta = requests.post(url, data=params)

    return {
        "resultado": "Publicação enviada!",
        "status": resposta.status_code,
        "resposta_api": resposta.json()
    }

if __name__ == "__main__":
    app.run()
