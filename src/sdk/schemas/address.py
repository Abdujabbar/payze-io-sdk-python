from pydantic import BaseModel, Field


class Address(BaseModel):
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    city: str
    country: str
    line1: str
    line2: str
    postal_code: str = Field(..., alias="postalCode")
    state: str
    phone_number: str = Field(..., alias="phoneNumber")
    personal_id: str = Field(..., alias="personalId")
    tax_id: str = Field(..., alias="taxId")
