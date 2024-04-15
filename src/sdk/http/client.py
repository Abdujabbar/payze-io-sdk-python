import requests


class HttpClient:
    def __init__(self, base_url, headers) -> None:
        self._headers = {
            "accept": "application/json",
            "content-type": "application/json",
        } | headers

        self._base_url = base_url

    def get(self, path="", headers=dict(), params=dict()):

        response = requests.get(
            f"{self._base_url}{path}", data=params, headers=self._headers | headers
        )

        return response

    def post(self, path="", headers=dict(), payload=dict()):
        response = requests.post(
            f"{self._base_url}{path}", json=payload, headers=self._headers | headers
        )

        return response

    def put(self, path="", headers=dict(), payload=dict()):
        response = requests.put(
            f"{self._base_url}{path}", json=payload, headers=self._headers | headers
        )
        return response
