from src.sdk.http.client import HttpClient


class BaseService:
    def __init__(self, base_url, secret_key, access_token) -> None:
        self._secret_key = secret_key
        self._access_token = access_token
        self._http_client = HttpClient(
            base_url,
            {
                "authorization": f"{access_token}:{secret_key}",
                "user-agent": "python-app/v1",
            },
        )

    def set_access_token(self, token):
        self._access_token = token

    def set_secret_key(self, secret_key):
        self._secret_key = secret_key
