import requests

PAGE_ID = "COLE_O_ID_DA_PAGINA"
PAGE_ACCESS_TOKEN = "COLE_O_TOKEN_DE_ACESSO_DA_PAGINA"

def post_image_to_page(image_url, message):
    url = f"https://graph.facebook.com/{PAGE_ID}/photos"
    payload = {
        "url": image_url,
        "caption": message,
        "access_token": PAGE_ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    print(response.json())

# Exemplo de uso
post_image_to_page(
    "https://www.exemplo.com/imagem.jpg",
    "Publicação com imagem via REST API do Facebook!"
)
