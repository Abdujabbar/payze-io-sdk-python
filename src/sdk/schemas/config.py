from pydantic import BaseModel


class PayzeConfig(BaseModel):
    secret_key: str
    access_token: str
    webhook_gateway: str
    success_redirect_url: str
    error_redirect_url: str
