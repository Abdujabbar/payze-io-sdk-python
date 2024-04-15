from .base import BaseService
from . import METHODS
from src.sdk.schemas.payment import (
    CardPayment,
    MetaData,
    PayoutSplit,
    ShareLink,
    PaymentCapture,
    PaymentCardData,
    PayoutSplitUpdate,
    PayoutCancelSplit,
)
from src.sdk.schemas.order import Order
from src.sdk.builders.payment_builder import PaymentBuilder, PaymentRefundBuilder


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
        source: str,
        amount: float,
        currency: str,
        idempotency_key: str = None,
        token: str = None,
        card_payment: CardPayment = None,
        metadata: MetaData = None,
        payout_split: PayoutSplit = None,
        share_link: ShareLink = None,
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
            path=METHODS.get("PaymentService.create"),
            payload=payment_builder.build().model_dump(),
        )

    def capture(self, transaction_id: str, amount: float):
        payment_capture = PaymentCapture(transaction_id=transaction_id, amount=amount)

        return self._http_client.put(
            path=METHODS.get("PaymentService.capture"),
            payload=payment_capture.model_dump(),
        )

    def pay(
        self,
        transaction_id: str,
        number: str,
        card_holder: str,
        expiration_date: str,
        security_number: str,
    ):
        payment_card_data = PaymentCardData(
            transactionId=transaction_id,
            number=number,
            cardHolder=card_holder,
            expirationDate=expiration_date,
            securityNumber=security_number,
        )

        return self._http_client.post(
            path=METHODS.get("PaymentService.pay"),
            payload=payment_card_data.model_dump(),
        )

    def get_payments(self, filter: str, top: int, skip: int, orderby: str):

        return self._http_client.get(
            path=METHODS.get("PaymentService.get_payments"),
            params={"$filter": filter, "$top": top, "$skip": skip, "$orderby": orderby},
        )

    def receipt(self, transaction_id: str):
        return self._http_client.get(
            path=METHODS.get("PaymentService.get_receipt"),
            params={"transactionId": transaction_id},
        )

    def refund(
        self,
        transaction_id: str,
        amount: float,
        idempotency_key: str = None,
        order_data: Order = None,
        extra_attributes: dict = None,
    ):
        payment_refund_builder = PaymentRefundBuilder(
            transaction_id=transaction_id, amount=amount
        )

        for key, value in (
            ("idempotency_key", idempotency_key),
            ("order_data", order_data),
            ("extra_attributes", extra_attributes),
        ):
            if value:
                getattr(payment_refund_builder, f"with_{key}")(value)

        return self._http_client.put(
            path=METHODS.get("PaymentService.refund"),
            payload=payment_refund_builder.build().model_dump(),
        )

    def get_refunds(self, transaction_id: str):
        return self._http_client.get(
            path=METHODS.get("PaymentService.get_refunds"),
            params={"transactionId": transaction_id},
        )

    def split(
        self, transaction_id: str, splits=list[PayoutSplit], idempotency_key: str = None
    ):
        payout_split_update = PayoutSplitUpdate(
            transaction_id=transaction_id, splits=splits, idempotencyKey=idempotency_key
        )

        return self._http_client.put(
            path=METHODS.get("PaymentService.split"),
            payload=payout_split_update.model_dump(),
        )

    def get_splits(
        self,
        payment_id: int,
        transaction_id: int,
        _filter: str,
        orderby: str,
        top: int,
        skip: int,
    ):
        return self._http_client.get(
            path=METHODS.get("PaymentService.get_splits"),
            params={
                "paymentId": payment_id,
                "TransactionId": transaction_id,
                "$filter": _filter,
                "$orderby": orderby,
                "$top": top,
                "$skip": skip,
            },
        )

    def cancel_splits(self, transaction_id: str):
        payout_cancel_split = PayoutCancelSplit(transaction_id=transaction_id)

        return self._http_client.put(
            path=METHODS.get("PaymentService.split.cancel"),
            payload=payout_cancel_split.model_dump(),
        )
