from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
from .order import Order


class Hooks(BaseModel):
    webhook_gateway: str = Field(..., alias="webhookGateway")
    success_redirect_gateway: str = Field(..., alias="successRedirectGateway")
    error_redirect_gateway: str = Field(..., alias="errorRedirectGateway")


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
    payout_account: PayoutAccount = Field(..., alias="payoutAccount")
    delay_payout_days: int = Field(..., alias="delayPayoutDays")
    description: str


class PaymentSource(Enum):
    card = "Card"
    iban = "IBan"


class MetaData(BaseModel):
    channel: str
    order: Order
    extra_attributes: dict = Field(..., "extraAttributes")


class Payment(BaseModel):
    source: PaymentSource
    amount: float
    currency: str
    hooks: Hooks
    language: Optional[str]
    idempotency_key: Optional[str] = Field(..., "idempotencyKey")
    card_payment: Optional[CardPayment] = Field(..., "cardPayment")
    metadata: Optional[MetaData]
    payout_split: Optional[PayoutSplit] = Field(..., "payoutSplit")
    share_link: Optional[ShareLink] = Field(..., "shareLink")
    token: Optional[str]
