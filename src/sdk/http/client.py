import requests

class HttpClient:
    def __init__(self) -> None:
        self._headers = {
            "accept": "application/json",
            "content-type": "application/*+json"
        }

    def set_header(self, headers):
        self._headers |= headers

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass