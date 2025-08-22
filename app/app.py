from flask import Flask, request, jsonify
from core.wordpress import WordPressManager
from core.learning import LearningCore
from core.shadow import ShadowModule
from core.tasks import TaskExecutor

app = Flask(__name__)

# === NÚCLEOS ===
wp = WordPressManager(
    url="https://jcdicaseconhecimentos.com.br",
    user="ana.cortez",
    app_pass="SUA_CHAVE_WORDPRESS_AQUI"
)
learning = LearningCore("models/memory.db")
shadow = ShadowModule()
executor = TaskExecutor(wp, learning, shadow)

# === ROTAS API ===

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "status": "online",
        "uptime": executor.get_uptime(),
        "last_action": executor.last_action
    })

@app.route("/api/post/create", methods=["POST"])
def create_post():
    data = request.json
    title = data.get("title")
    content = data.get("content")
    tags = data.get("tags", [])
    post_id = wp.create_post(title, content, tags)
    learning.log_action("post_created", {"title": title, "id": post_id})
    return jsonify({"success": True, "post_id": post_id})

@app.route("/api/learn", methods=["POST"])
def learn():
    data = request.json
    topic = data.get("topic")
    notes = data.get("notes")
    learning.learn(topic, notes)
    return jsonify({"success": True, "message": f"Ana aprendeu sobre {topic}"})

@app.route("/api/control/pause", methods=["POST"])
def pause():
    executor.pause()
    return jsonify({"success": True, "message": "Execução pausada."})

@app.route("/api/control/run", methods=["POST"])
def run():
    task = request.json.get("task", "default")
    result = executor.run(task)
    return jsonify({"success": True, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
