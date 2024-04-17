from typing import Optional

from src.sdk.schemas.order import Order
from src.sdk.schemas.payment import (
    CardPayment,
    Hooks,
    MetaData,
    Payment,
    PaymentRefund,
    PaymentSource,
    PayoutSplit,
    ShareLink,
)


class PaymentBuilder:
    def __init__(
        self,
        source: str,
        amount: float,
        currency: str,
        webhook_gateway: Optional[str],
        success_redirect_gateway: Optional[str],
        error_redirect_gateway: Optional[str],
    ) -> None:
        self._source = PaymentSource(source).value
        self._amount = amount
        self._currency = currency
        self._hooks = Hooks(
            webhookGateway=webhook_gateway,
            successRedirectGateway=success_redirect_gateway,
            errorRedirectGateway=error_redirect_gateway,
        )

    def with_metadata(self, metadata: MetaData):
        self._metadata = metadata
        return self

    def with_payout_split(self, payout_split: PayoutSplit):
        self._payout_split = payout_split
        return self

    def with_card_payment(self, card_payment: CardPayment):
        self._card_payment = card_payment
        return self

    def with_language(self, language: str):
        self._language = language
        return self

    def with_share_link(self, share_link: ShareLink):
        self._share_link = share_link
        return self

    def with_idempotency_key(self, idempotency_key: str):
        self._idempotency_key = idempotency_key
        return self

    def with_token(self, token):
        self._token = token
        return self

    def build(self) -> Payment:
        """
        Builds a payment object based on the builder's settings.

        Returns:
            Payment: The payment object.
        """
        return Payment(
            # Mandatory fields
            source=self._source,
            amount=self._amount,
            currency=self._currency,
            hooks=self._hooks,
            # Optional fields
            metadata=self._metadata if hasattr(self, "_metadata") else None,
            payout_split=self._payout_split if hasattr(self, "_payout_split") else None,
            card_payment=self._card_payment if hasattr(self, "_card_payment") else None,
            language=self._language if hasattr(self, "_language") else None,
            share_link=self._share_link if hasattr(self, "_share_link") else None,
            idempotency_key=(
                self._idempotency_key if hasattr(self, "_idempotency_key") else None
            ),
            token=self._token if hasattr(self, "_token") else None,
        )
