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
    payout_account: PayoutAccount = Field(..., alias="payoutAccount")
    delay_payout_days: int = Field(..., alias="delayPayoutDays")
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


class PaymentCapture(BaseModel):
    transaction_id: str = Field(..., alias="transactionId")
    amount: float = Field(..., alias="amount")


class PaymentCardData(BaseModel):
    transaction_id: str = Field(..., alias="transactionId")
    number: str
    card_holder: str = Field(..., alias="cardHolder")
    expiration_date: str = Field(..., alias="expirationDate")
    security_number: str = Field(..., alias="securityNumber")


class PaymentRefund(BaseModel):
    transaction_id: str = Field(..., alias="transactionId")
    amount: float
    idempotency_key: Optional[str] = Field(..., alias="idempotencyKey")
    order_data: Optional[Order] = Field(..., alias="orderData")
    extra_attributes: Optional[dict] = Field(..., alias="extraAttributes")


class PayoutSplitUpdate(BaseModel):
    transaction_id: str
    splits: list[PayoutSplit]
    idempotency_key: str = Field(..., alias="idempotencyKey")


class PayoutCancelSplit(BaseModel):
    transaction_id: str
