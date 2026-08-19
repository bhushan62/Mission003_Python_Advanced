from typing import TypeVar


T = TypeVar("T")


def get_first_item(
    items: list[T]
) -> T | None:
    if not items:
        return None

    return items[0]


def get_last_item(
    items: list[T]
) -> T | None:
    if not items:
        return None

    return items[-1]


order_ids: list[str] = [
    "AO10001",
    "AO10002",
    "AO10003"
]


order_amounts: list[float] = [
    850.0,
    1200.0,
    1750.0
]


empty_orders: list[str] = []


first_order: str | None = get_first_item(
    order_ids
)

last_order: str | None = get_last_item(
    order_ids
)

first_amount: float | None = get_first_item(
    order_amounts
)

missing_order: str | None = get_first_item(
    empty_orders
)


print("First order:", first_order)
print("Last order:", last_order)
print("First amount:", first_amount)
print("Missing order:", missing_order)