import requests
from bs4 import BeautifulSoup

class ShadowModule:
    def scan(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        titles = [h.get_text() for h in soup.find_all("h2")]
        return {"url": url, "titles": titles}
