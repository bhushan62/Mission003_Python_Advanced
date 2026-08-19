def calculate_total(
    amounts: list[float]
) -> float:
    return sum(amounts)


def find_ready_orders(
    order_statuses: dict[str, str]
) -> list[str]:
    ready_orders: list[str] = []

    for order_id, status in order_statuses.items():
        if status.casefold() == "ready":
            ready_orders.append(order_id)

    return ready_orders


def count_orders(
    ready: int,
    processing: int
) -> tuple[int, int]:
    return ready, processing


def get_supported_services() -> set[str]:
    return {
        "Dry Cleaning",
        "Wash and Iron",
        "Steam Iron"
    }


order_amounts: list[float] = [
    850.0,
    1200.0,
    1750.0
]


order_statuses: dict[str, str] = {
    "AO10001": "Ready",
    "AO10002": "Processing",
    "AO10003": "Ready"
}


total: float = calculate_total(order_amounts)

ready_orders: list[str] = find_ready_orders(
    order_statuses
)

order_counts: tuple[int, int] = count_orders(
    ready=2,
    processing=1
)

services: set[str] = get_supported_services()


print("Total revenue: ₹", total, sep="")
print("Ready orders:", ready_orders)
print("Order counts:", order_counts)
print("Services:", sorted(services))