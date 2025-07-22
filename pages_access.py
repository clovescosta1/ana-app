import requests

ACCESS_TOKEN = "EAAK2rsOkjJwBPNF0y8HvoxFc804GW43B1Ds5MZAJxvisK14na0uomgUcEIqv8jApC7ZCk2dZCXwStd1ZA8NaZBVXFL9Wa3eoDf5mRvouwHIP2E5CNfvfSAdMu84vxEBW8lMZBY7ZBPZCyO62XBXtoE0VC5xvZAFcfPm8s600iZATFRVkePjvwaP15T8WcRPGIihaTMV2hhplrViuBe8LsWEHe8SV56KHmGAVCH"

def get_pages():
    url = f"https://graph.facebook.com/me/accounts?access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    for page in data['data']:
        print(f"Page Name: {page['name']}, ID: {page['id']}, Access Token: {page['access_token']}")
