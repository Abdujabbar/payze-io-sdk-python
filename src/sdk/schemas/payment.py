from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
from .order import Order


class Hooks(BaseModel):
    webhookGateway: str
    successRedirectGateway: str
    errorRedirectGateway: str


class CardPayment(BaseModel):
    preauthorized: bool
    tokenize_card: bool
    apply_pay: bool


class ShareLink(BaseModel):
    email: Optional[str]
    sms_phone: Optional[str]


class PayoutAccount(BaseModel):
    iban: str
    owner_name: str
    owner_personal_id: str
    owner_tax_id: str


class PayoutSplit(BaseModel):
    amount: float
    payout_account: PayoutAccount
    delay_payout_days: int
    description: str


class PaymentSource(Enum):
    card = "Card"
    iban = "IBan"


class MetaData(BaseModel):
    channel: str
    order: Order
    extra_attributes: dict


class Payment(BaseModel):
    source: str
    amount: float
    currency: str
    hooks: Hooks
    language: Optional[str]
    idempotency_key: Optional[str]
    card_payment: Optional[CardPayment]
    metadata: Optional[MetaData]
    payout_split: Optional[PayoutSplit]
    share_link: Optional[ShareLink]
    token: Optional[str]
