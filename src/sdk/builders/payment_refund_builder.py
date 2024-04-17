from src.sdk.schemas.order import Order
from src.sdk.schemas.payment import PaymentRefund


class PaymentRefundBuilder:
    def __init__(self, transaction_id: str, amount: float) -> None:
        self.transaction_id = transaction_id
        self.amount = amount

    def with_idempotency_key(self, idempotency_key: str):
        self._idempotency_key = idempotency_key
        return self

    def with_order(self, order: Order):
        self._order = order
        return self

    def with_extra_attributes(self, extra: dict):
        self._extra_attributes = extra
        return self

    def build(self):
        return PaymentRefund(
            # Mandatory fields
            transactionId=self.transaction_id,
            amount=self.amount,
            # Optional fields
            idempotencyKey=(
                self._idempotency_key if hasattr(self, "_idempotency_key") else ""
            ),
            orderData=self._order if hasattr(self, "_order") else None,
            extraAttributes=(
                self._extra_attributes if hasattr(self, "_extra_attributes") else None
            ),
        )
