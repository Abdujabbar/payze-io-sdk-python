from typing import List
from pydantic import BaseModel, Field
from .address import Address


class OrderItemDetails(BaseModel):
    comission_info_tin: str = Field(..., "commissionInfoTin")
    comission_info_pinfl: str = Field(..., "comissionInfoPinfl")


class OrderItem(BaseModel):
    product_link: str
    product_image: str
    product_name: str
    product_code: str
    product_bar_code: str
    product_label: str
    package_code: str
    product_quantity: float
    price: float
    sum_price: float
    vat: float
    vat_percent: float
    discount: float
    additional_discount: float
    details: OrderItemDetails


class OrderDetails(BaseModel):
    latitude: float
    longitude: float
    taxi_vehicle_number: str = Field(..., "taxiVehicleNumber")
    taxi_tin: str = Field(..., "taxiTin")
    taxi_pinfl: str = Field(..., "taxiPinfl")


class Order(BaseModel):
    order_id: str
    order_items: List[OrderItem] = Field(..., alias="orderItems")
    details: OrderDetails = Field(..., "uzRegulatoryOrderDetails")
    billing_address: Address = Field(..., alias="billingAddress")
    shipping_address: Address = Field(..., alias="shippingAddress")
