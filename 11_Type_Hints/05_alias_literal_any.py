from typing import Any, Literal


# Type aliases
type OrderID = str

type OrderStatus = Literal[
    "Ready",
    "Processing",
    "Delivered",
    "Pending"
]

type OrderData = dict[str, Any]


def update_order_status(
    order_id: OrderID,
    status: OrderStatus
) -> str:
    return (
        f"Order {order_id} changed to {status}"
    )


def display_order(order: OrderData) -> None:
    print("Order ID:", order["order_id"])
    print("Customer:", order["customer"])
    print("Quantity:", order["quantity"])
    print("Amount: ₹", order["amount"], sep="")
    print("Ready:", order["is_ready"])


ready_order: OrderData = {
    "order_id": "AO45821",
    "customer": "Ravi",
    "quantity": 3,
    "amount": 1750.0,
    "is_ready": True
}


status_message: str = update_order_status(
    order_id="AO45821",
    status="Ready"
)


print(status_message)
print()

display_order(ready_order)