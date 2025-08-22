import requests
import base64

class WordPressManager:
    def __init__(self, url, user, app_pass):
        self.url = f"{url}/wp-json/wp/v2"
        token = base64.b64encode(f"{user}:{app_pass}".encode())
        self.headers = {"Authorization": f"Basic {token.decode('utf-8')}"}

    def create_post(self, title, content, tags=[]):
        data = {
            "title": title,
            "content": content,
            "status": "publish",
            "tags": tags
        }
        r = requests.post(f"{self.url}/posts", headers=self.headers, json=data)
        if r.status_code == 201:
            return r.json()["id"]
        return None
