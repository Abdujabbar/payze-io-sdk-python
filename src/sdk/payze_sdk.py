import os

from .services.account import AccountService
from .services.payment import PaymentService
from .services.payout import PayoutService


class PayzeSDK:
    def __init__(
        self,
        base_url=None,
        access_token=None,
        secret_key=None,
        webhook_gateway=None,
        success_redirect_gateway=None,
        error_redirect_gateway=None,
    ) -> None:
        self._api_base_url = os.getenv(
            "API_BASE_URL", base_url
        )  # https://payze.io/v2/api/
        self._access_token = os.getenv("ACCESS_TOKEN", access_token)
        self._secret_key = os.getenv("SECRET_KEY", secret_key)
        self._webhook_gateway = os.getenv("WEBHOOK_GATEWAY", webhook_gateway)
        self._success_redirect_gateway = os.getenv(
            "SUCCESS_REDIRECT_GATEWAY", success_redirect_gateway
        )
        self._error_redirect_gateway = os.getenv(
            "ERROR_REDIRECT_GATEWAY", error_redirect_gateway
        )

        self.account = AccountService(
            self._api_base_url, self._secret_key, self._access_token
        )
        self.payment = PaymentService(
            self._api_base_url,
            self._secret_key,
            self._access_token,
            self._webhook_gateway,
            self._success_redirect_gateway,
            self._error_redirect_gateway,
        )
        self.payout = PayoutService(
            self._api_base_url, self._secret_key, self._access_token
        )

    def set_access_token(self, token):
        self.account.set_access_token(token)
        self.payment.set_access_token(token)
        self.payout.set_access_token(token)

    def set_secret_key(self, secret_key):
        self.account.set_secret_key(secret_key)
        self.payment.set_secret_key(secret_key)
        self.payout.set_secret_key(secret_key)
