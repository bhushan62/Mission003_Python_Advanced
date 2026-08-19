from typing import Literal, TypedDict


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
    amount: float
    status: OrderStatus


def validate_order(order: dict[str, object]) -> list[str]:
    errors: list[str] = []

    order_id = order.get("order_id")
    customer = order.get("customer")
    quantity = order.get("quantity")
    amount = order.get("amount")
    status = order.get("status")

    if not isinstance(order_id, str):
        errors.append("Order ID must be a string")
    elif not order_id.startswith("AO"):
        errors.append("Order ID must begin with AO")

    if not isinstance(customer, str):
        errors.append("Customer name must be a string")
    elif not customer.strip():
        errors.append("Customer name cannot be empty")

    if (
        not isinstance(quantity, int)
        or isinstance(quantity, bool)
        or quantity <= 0
    ):
        errors.append("Quantity must be a positive integer")

    if (
        not isinstance(amount, (int, float))
        or isinstance(amount, bool)
        or amount < 0
    ):
        errors.append("Amount must be a positive number")

    valid_statuses: set[str] = {
        "Ready",
        "Processing",
        "Delivered",
        "Pending"
    }

    if status not in valid_statuses:
        errors.append("Invalid order status")

    return errors


valid_order: dict[str, object] = {
    "order_id": "AO45821",
    "customer": "Ravi",
    "quantity": 3,
    "amount": 1750.0,
    "status": "Ready"
}

invalid_order: dict[str, object] = {
    "order_id": "BO33396",
    "customer": "",
    "quantity": "three",
    "amount": -500,
    "status": "Waiting"
}


orders: list[dict[str, object]] = [
    valid_order,
    invalid_order
]


for order in orders:
    print("=" * 45)
    print("Checking order:", order.get("order_id"))

    validation_errors = validate_order(order)

    if validation_errors:
        print("Order rejected")

        for error in validation_errors:
            print("-", error)
    else:
        print("Order accepted")