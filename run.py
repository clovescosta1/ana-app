from flask import Flask, request

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

if __name__ == "__main__":
    app.run()
