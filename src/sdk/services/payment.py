from .base import BaseService


class PaymentService(BaseService):
    def __init__(self, secret_key, access_token, webhook_gateway, success_redirect_gateway, error_redirect_gateway) -> None:
        super().__init__(secret_key, access_token)

        self.webhook_gateway = webhook_gateway
        self.success_redirect_gateway = success_redirect_gateway
        self.error_redirect_gateway = error_redirect_gateway

    def create(self):
        pass

    def capture(self):
        pass

    def pay(self): #https://docs.payze.io/reference/post_v2-payment-pay
        pass

    def get_payments(self):
        pass

    def receipt(self):
        pass

    def refund(self):
        pass

    def get_refunds(self):
        pass

    def split(self):
        pass

    def get_splits(self):
        pass

    def cancel_splits(self):
        pass
