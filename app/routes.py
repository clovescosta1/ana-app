from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>AnaSync está rodando!</h1><p>O painel estará disponível aqui em breve.</p>"

if __name__ == "__main__":
    app.run()
