import requests

def randomImage():
    requisição = requests.get("https://dog.ceo/api/breeds/image/random")
    result = requisição.json()
    return result["message"]