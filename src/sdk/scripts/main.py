import os
from src.sdk.payze_sdk import PayzeSDK
from src.sdk.schemas.payment import PaymentSource
from src.sdk.schemas.payment import Hooks
from src.sdk.services.base import BaseService
from dotenv import load_dotenv

load_dotenv()


def main():
    base_service = BaseService(os.getenv("BASE_URL"), "123", "123")

    print(base_service.build_path_endpoint())
    # sdk = PayzeSDK(
    #     base_url=os.getenv("BASE_URL"),
    #     access_token=os.getenv("ACCESS_TOKEN"),
    #     secret_key=os.getenv("SECRET_KEY"),
    #     webhook_gateway=os.getenv("WEBHOOK_GATEWAY"),
    #     success_redirect_gateway=os.getenv("SUCCESS_REDIRECT_GATEWAY"),
    #     error_redirect_gateway=os.getenv("ERROR_REDIRECT_GATEWAY"),
    # )

    # res = sdk.payment.create("Card", 11, "USD")

    # print(res.status_code)

    # print(res.content)


if __name__ == "__main__":
    main()
