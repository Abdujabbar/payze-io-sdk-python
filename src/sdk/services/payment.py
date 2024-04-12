from .base import BaseService
from src.sdk.builders.payment_builder import PaymentBuilder


class PaymentService(BaseService):
    def __init__(
        self,
        base_url,
        secret_key,
        access_token,
        webhook_gateway,
        success_redirect_gateway,
        error_redirect_gateway,
    ) -> None:
        super().__init__(base_url, secret_key, access_token)

        self.webhook_gateway = webhook_gateway
        self.success_redirect_gateway = success_redirect_gateway
        self.error_redirect_gateway = error_redirect_gateway

    def create(
        self,
        source,
        amount,
        currency,
        idempotency_key=None,
        token=None,
        card_payment=None,
        metadata=None,
        payout_split=None,
        share_link=None,
    ):
        payment_builder = PaymentBuilder(
            source,
            amount,
            currency,
            self.webhook_gateway,
            self.success_redirect_gateway,
            self.error_redirect_gateway,
        )

        for key, value in (
            ("idempotency_key", idempotency_key),
            ("token", token),
            ("card_payment", card_payment),
            ("metadata", metadata),
            ("payout_split", payout_split),
            ("share_link", share_link),
        ):
            if value:
                getattr(payment_builder, f"with_{key}")(value)

        return self._http_client.put(
            path="/payment", payload=payment_builder.build().model_dump()
        )

    def capture(self):
        pass

    def pay(self):
        pass

    def get_payments(self):
        pass

    def receipt(self):
        pass

    def refund(self):
        pass

    def get_refunds(self):
        pass

    def split(self):
        pass

    def get_splits(self):
        pass

    def cancel_splits(self):
        pass
