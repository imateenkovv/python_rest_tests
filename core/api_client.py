import requests
from core.config import BASE_URL, BASE_HEADERS


class ApiClient:
    def __init__(self, base_url=BASE_URL, headers=BASE_HEADERS):
        self.base_url = base_url
        self.headers = {'x-api-key': f'{headers}'}

    def get(self, endpoint, **kwargs):
        url = f'{self.base_url}{endpoint}'
        return requests.get(url, headers=self.headers, **kwargs)

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, headers=self.headers, json=json or data)

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, headers=self.headers)
