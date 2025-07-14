from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "AnaSync rodando!"
@app.route("/status")
def status():
    return {"status": "online", "nome": "AnaSync", "versão": "1.0"}
@app.route("/ana")
def ana():
    return {
        "nome": "Ana Cortez",
        "versão": "1.0",
        "função": "Gerar vídeos, postar em redes e vender como afiliada"
    }

if __name__ == "__main__":
    app.run()
