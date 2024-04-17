import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        return response.content
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro ao fazer requisição HTTP: {e}")
