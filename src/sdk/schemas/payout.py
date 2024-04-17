from pydantic import BaseModel, Field


class Payout(BaseModel):
    amount: float
    currency: str
    bank_account_id: int = Field(..., alias="bankAccountId")
