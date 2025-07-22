import requests

PAGE_ID = "COLE_AQUI_O_ID_DA_SUA_PAGINA"
PAGE_ACCESS_TOKEN = "COLE_AQUI_O_ACCESS_TOKEN_DA_PAGINA"

def post_to_page(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {
        "message": message,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    print(response.json())

# Exemplo de uso
post_to_page("Publicação de teste feita via API!")
