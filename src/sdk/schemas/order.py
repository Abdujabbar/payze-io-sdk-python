from typing import List, Optional
from pydantic import BaseModel, Field
from .address import Address


class OrderItemDetails(BaseModel):
    comission_info_tin: str = Field(..., alias="commissionInfoTin")
    comission_info_pinfl: str = Field(..., alias="comissionInfoPinfl")


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
    taxi_vehicle_number: str = Field(..., alias="taxiVehicleNumber")
    taxi_tin: str = Field(..., alias="taxiTin")
    taxi_pinfl: str = Field(..., alias="taxiPinfl")


class Order(BaseModel):
    order_id: str
    order_items: Optional[List[OrderItem]] = Field(..., alias="orderItems")
    details: OrderDetails = Field(..., alias="uzRegulatoryOrderDetails")
    billing_address: Address = Field(..., alias="billingAddress")
    shipping_address: Address = Field(..., alias="shippingAddress")
