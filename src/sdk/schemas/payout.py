from pydantic import BaseModel, Field, PositiveFloat


class Payout(BaseModel):
    amount: PositiveFloat
    currency: str
    bank_account_id: int = Field(..., alias="bankAccountId")
