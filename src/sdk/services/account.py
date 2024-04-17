from typing import Optional

from . import METHODS
from .base import BaseService


class AccountService(BaseService):
    def get_company_balance(self, query: Optional[str]):

        return self._http_client.get(
            path=METHODS.get("AccountService.get_company_balance"),
            params={"query": query},
        )

    def get_bank_accounts(self, _filter: str, top: int, skip: int, orderby: str):
        return self._http_client.get(
            path=METHODS.get("AccountService.get_bank_accounts"),
            params={
                "$filter": _filter,
                "$top": top,
                "$skip": skip,
                "$orderby": orderby,
            },
        )
