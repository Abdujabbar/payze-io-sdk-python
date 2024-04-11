class BaseService:
    def __init__(self, secret_key, access_token) -> None:
        self._secret_key = secret_key
        self._access_token = access_token

    def set_access_token(self, token):
        self._access_token = token

    def set_secret_key(self, secret_key):
        self._secret_key = secret_key
