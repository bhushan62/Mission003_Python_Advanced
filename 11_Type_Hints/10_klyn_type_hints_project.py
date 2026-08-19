from collections.abc import Callable
from typing import Literal, NotRequired, TypedDict


# Exact permitted status values
type OrderStatus = Literal[
    "Ready",
    "Processing",
    "Delivered",
    "Pending"
]


# Type of a notification function
type NotificationFunction = Callable[[str], None]


# Structure of one laundry order
class LaundryOrder(TypedDict):
    order_id: str
    customer: str
    quantity: int
    price_per_item: float
    status: OrderStatus
    phone: NotRequired[str]


def validate_order(order: LaundryOrder) -> list[str]:
    """Validate the values inside a laundry order."""

    errors: list[str] = []

    if not order["order_id"].startswith("AO"):
        errors.append("Order ID must begin with AO")

    if not order["customer"].strip():
        errors.append("Customer name cannot be empty")

    if order["quantity"] <= 0:
        errors.append("Quantity must be greater than zero")

    if order["price_per_item"] < 0:
        errors.append("Price cannot be negative")

    return errors


def calculate_total(order: LaundryOrder) -> float:
    """Calculate the total bill amount."""

    return order["quantity"] * order["price_per_item"]


def prepare_ready_message(
    order: LaundryOrder
) -> str | None:
    """Return a message only when the order is ready."""

    if order["status"] != "Ready":
        return None

    total: float = calculate_total(order)

    return (
        f"Dear {order['customer']}, "
        f"your order {order['order_id']} is ready. "
        f"Amount: ₹{total}"
    )


def console_notification(message: str) -> None:
    """Display the notification in the terminal."""

    print("NOTIFICATION:", message)


def process_orders(
    orders: list[LaundryOrder],
    notification_function: NotificationFunction
) -> tuple[int, float]:
    """
    Validate and process orders.

    Returns:
        Number of valid orders and their total revenue.
    """

    valid_order_count: int = 0
    total_revenue: float = 0.0

    for order in orders:
        print("=" * 50)
        print("Order ID:", order["order_id"])

        errors: list[str] = validate_order(order)

        if errors:
            print("Order rejected")

            for error in errors:
                print("-", error)

            continue

        total: float = calculate_total(order)

        valid_order_count += 1
        total_revenue += total

        print("Customer:", order["customer"])
        print("Status:", order["status"])
        print("Quantity:", order["quantity"])
        print("Bill amount: ₹", total, sep="")

        message: str | None = prepare_ready_message(order)

        if message is not None:
            notification_function(message)
        else:
            print("Notification not required")

    return valid_order_count, total_revenue


laundry_orders: list[LaundryOrder] = [
    {
        "order_id": "AO45821",
        "customer": "Ravi",
        "quantity": 3,
        "price_per_item": 85.0,
        "status": "Ready",
        "phone": "9876543210"
    },
    {
        "order_id": "AO33396",
        "customer": "Suresh",
        "quantity": 2,
        "price_per_item": 150.0,
        "status": "Processing"
    },
    {
        "order_id": "BO98765",
        "customer": "",
        "quantity": -2,
        "price_per_item": 100.0,
        "status": "Pending"
    }
]


processed_count, revenue = process_orders(
    orders=laundry_orders,
    notification_function=console_notification
)


print("\n" + "=" * 50)
print("KLYN PROCESSING SUMMARY")
print("=" * 50)
print("Valid orders:", processed_count)
print("Total revenue: ₹", revenue, sep="")