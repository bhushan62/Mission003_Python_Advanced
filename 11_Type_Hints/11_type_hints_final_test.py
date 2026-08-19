from typing import Literal, TypedDict


type OrderStatus = Literal[
    "Ready",
    "Processing",
    "Delivered"
]


class LaundryOrder(TypedDict):
    order_id: str
    customer: str
    quantity: int
    price_per_item: float
    status: OrderStatus


def calculate_total(order: LaundryOrder) -> float:
    return order["quantity"] * order["price_per_item"]


def find_ready_orders(
    orders: list[LaundryOrder]
) -> list[str]:

    ready_order_ids: list[str] = []

    for order in orders:
        if order["status"] == "Ready":
            ready_order_ids.append(order["order_id"])

    return ready_order_ids


def find_order(
    order_id: str,
    orders: list[LaundryOrder]
) -> LaundryOrder | None:

    for order in orders:
        if order["order_id"] == order_id:
            return order

    return None


laundry_orders: list[LaundryOrder] = [
    {
        "order_id": "AO45821",
        "customer": "Ravi",
        "quantity": 3,
        "price_per_item": 85.0,
        "status": "Ready"
    },
    {
        "order_id": "AO33396",
        "customer": "Suresh",
        "quantity": 2,
        "price_per_item": 150.0,
        "status": "Processing"
    },
    {
        "order_id": "AO98765",
        "customer": "Anjali",
        "quantity": 1,
        "price_per_item": 450.0,
        "status": "Ready"
    }
]


first_total: float = calculate_total(
    laundry_orders[0]
)

ready_orders: list[str] = find_ready_orders(
    laundry_orders
)

found_order: LaundryOrder | None = find_order(
    "AO45821",
    laundry_orders
)

missing_order: LaundryOrder | None = find_order(
    "AO99999",
    laundry_orders
)


print("=" * 45)
print("TYPE HINTS FINAL TEST")
print("=" * 45)

print("First order total: ₹", first_total, sep="")
print("Ready orders:", ready_orders)

print("\nFOUND ORDER")

if found_order is not None:
    print("Order ID:", found_order["order_id"])
    print("Customer:", found_order["customer"])
    print("Status:", found_order["status"])
else:
    print("Order was not found")


print("\nMISSING ORDER")

if missing_order is None:
    print("Order AO99999 was not found")
else:
    print("Order found:", missing_order)


print("\n" + "=" * 45)
print("TYPE HINTS CHAPTER COMPLETED")
print("=" * 45)