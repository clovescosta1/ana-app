import time

class TaskExecutor:
    def __init__(self, wp, learning, shadow):
        self.wp = wp
        self.learning = learning
        self.shadow = shadow
        self.running = True
        self.last_action = "None"
        self.start_time = time.time()

    def get_uptime(self):
        return round(time.time() - self.start_time, 2)

    def pause(self):
        self.running = False
        self.last_action = "Paused"

    def run(self, task="default"):
        if not self.running:
            return "Ana está pausada."
        if task == "default":
            post_id = self.wp.create_post("Post automático", "Conteúdo gerado pela Ana.", [])
            self.last_action = f"Post criado {post_id}"
            self.learning.log_action("auto_post", {"id": post_id})
            return f"Post criado com ID {post_id}"
        elif task == "shadow":
            data = self.shadow.scan("https://exemplo-concorrente.com")
            self.learning.log_action("shadow_scan", data)
            self.last_action = "Shadow scan concluído"
            return "Shadow scan executado"
