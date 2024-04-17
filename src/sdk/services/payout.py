from src.sdk.builders.payout_builder import PayoutBuilder

from . import METHODS
from .base import BaseService


class PayoutService(BaseService):
    def create(self, amount: float, currency: str, bank_account_id: int):
        payout_builder = PayoutBuilder(
            amount=amount, currency=currency, bank_account_id=bank_account_id
        )

        return self._http_client.post(
            path=METHODS.get("PayoutService.create"),
            payload=payout_builder.build().model_dump(by_alias=True),
        )

    def get_items(self, _filter: str, top: int, skip: int, orderby: str):

        return self._http_client.get(
            path=METHODS.get("PayoutService.get_items"),
            params={
                "$filter": _filter,
                "$top": top,
                "$skip": skip,
                "$orderby": orderby,
            },
        )
