from typing import Literal, NotRequired, TypedDict


type OrderStatus = Literal[
    "Ready",
    "Processing",
    "Delivered",
    "Pending"
]


class LaundryOrder(TypedDict):
    order_id: str
    customer: str
    quantity: int
    price_per_item: float
    status: OrderStatus
    phone: NotRequired[str]


def calculate_order_total(
    order: LaundryOrder
) -> float:
    return (
        order["quantity"]
        * order["price_per_item"]
    )


def display_order(
    order: LaundryOrder
) -> None:
    total: float = calculate_order_total(order)

    print("Order ID:", order["order_id"])
    print("Customer:", order["customer"])
    print("Status:", order["status"])
    print("Total: ₹", total, sep="")

    phone: str | None = order.get("phone")

    if phone is not None:
        print("Phone:", phone)
    else:
        print("Phone: Not provided")


order_one: LaundryOrder = {
    "order_id": "AO45821",
    "customer": "Ravi",
    "quantity": 3,
    "price_per_item": 85.0,
    "status": "Ready",
    "phone": "9876543210"
}


order_two: LaundryOrder = {
    "order_id": "AO33396",
    "customer": "Suresh",
    "quantity": 2,
    "price_per_item": 150.0,
    "status": "Processing"
}


display_order(order_one)

print()

display_order(order_two)