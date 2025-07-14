from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "AnaSync rodando!"
@app.route("/status")
def status():
    return {"status": "online", "nome": "AnaSync", "versão": "1.0"}

if __name__ == "__main__":
    app.run()
