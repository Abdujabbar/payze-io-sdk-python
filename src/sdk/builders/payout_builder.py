from src.sdk.schemas.payout import Payout


class PayoutBuilder:
    def __init__(self, amount: float, currency: str, bank_account_id: int) -> None:
        self._amount = amount
        self._currency = currency
        self._bank_account_id = bank_account_id

    def build(self):
        return Payout(
            amount=self._amount,
            currency=self._currency,
            bankAccountId=self._bank_account_id,
        )
