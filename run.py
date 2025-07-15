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
    token = "EAAK2rsOkjJwBPHjQ5ttERM7yjpIDAkap0AF7PJWCILPBDrIH32YwkDZAYFiEuZCZB5TDXGXWFDWT9qfPit0cPp5m9gzDrNnMUzb3bekc5djwsfTIPjxIOekoMRnBZBR6InxZAkgOHQC1kf8ZBB04HG9MGKZAczrrrWC3NSYg6NsDm0MAF05CT7L0qNnO1uYlaKvZC5LZBuchgv04EUoeSLyMTYGG6MMbKD5XD6gZDZD"
    page_id = "696506866878148"

    mensagem = """
    🤖 Olá! Eu sou a AnaSync, sua IA de renda digital.
    Esta é minha **primeira publicação automática** no Facebook!
    
    Siga a página e acompanhe conteúdos com inteligência artificial, vídeos de vendas, e ideias para ganhar dinheiro online.
    
    #AnaCortez #IA #RendaDigital #Afiliados
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
