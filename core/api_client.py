import requests
from core.config import BASE_URL, BASE_HEADERS
from rich.json import JSON
from core.logger import logger, colorize_status
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


class ApiClient:
    def __init__(self, base_url=BASE_URL, headers=BASE_HEADERS):
        self.base_url = base_url
        self.headers = {'x-api-key': f'{headers}'}

    def _log_request(self, method, url, **kwargs):
        #Разделитель в виде панели
        console.print(Panel.fit("NEW REQUEST"))

        text = Text()
        text.append("➡️  ", style="bold cyan")
        text.append(f"{method} ", style="bold white")
        text.append(f"{url}", style="link " + url)
        console.print(text)

        if "headers" in kwargs:
            console.print(f"[grey50]Headers:[/grey50] {kwargs['headers']}")
        if "json" in kwargs:
            console.print(f"[grey50]JSON:[/grey50] {kwargs['json']}")
        if "params" in kwargs:
            console.print(f"[grey50]Params:[/grey50] {kwargs['params']}")

    def _log_response(self, response):
        status_colored = colorize_status(response.status_code)
        console.print(f"⬅️  [white]Status:[/white] {status_colored}")

        try:
            response_json = response.json()
            console.print(JSON.from_data(response_json))
        except Exception:
            console.print("[yellow]Ответ не в JSON формате[/yellow]")
            console.print(response.text)

    def get(self, endpoint, **kwargs):
        url = f'{self.base_url}{endpoint}'
        self._log_request("GET", url, **kwargs)
        response = requests.get(url, headers=self.headers, **kwargs)
        self._log_response(response)
        return response

    def post(self, endpoint, json=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self._log_request("POST", url, json=json)
        response = requests.post(url, headers=self.headers, json=json, **kwargs)
        self._log_response(response)
        return response

    def put(self, endpoint, json=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self._log_request("PUT", url, json=json)
        response = requests.put(url, headers=self.headers, json=json, **kwargs)
        self._log_response(response)
        return response

    def patch(self, endpoint, json=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self._log_request("PATCH", url, json=json)
        response = requests.patch(url, headers=self.headers, json=json, **kwargs)
        self._log_response(response)
        return response

    def delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self._log_request("DELETE", url, **kwargs)
        response = requests.delete(url, headers=self.headers, **kwargs)
        self._log_response(response)
        return response
