import requests
from requests.exceptions import ConnectionError


def get_page(url):
    base_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        }
    try:
        response = requests.get(url, headers=base_headers)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
