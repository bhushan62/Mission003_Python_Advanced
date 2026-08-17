import re

from itertools import islice
from pathlib import Path


DATA_FILE = Path(__file__).with_name(
    "klyn_orders_data.txt"
)

ORDER_PATTERN = re.compile(r"^AO\d{5}$")


def read_order_lines(file_path):
    """Read non-empty records one line at a time."""

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line_number, line in enumerate(
            file,
            start=1
        ):
            clean_line = line.strip()

            if clean_line:
                yield line_number, clean_line


def parse_orders(records):
    """Convert valid text records into dictionaries."""

    for line_number, line in records:

        try:
            order_id, customer, status, amount = (
                line.split("|")
            )

        except ValueError:
            print(
                f"Line {line_number} skipped: "
                "incorrect number of fields"
            )
            continue

        if not ORDER_PATTERN.fullmatch(order_id):
            print(
                f"Line {line_number} skipped: "
                f"invalid order ID {order_id}"
            )
            continue

        try:
            amount = int(amount)

        except ValueError:
            print(
                f"Line {line_number} skipped: "
                "amount must be a number"
            )
            continue

        yield {
            "order_id": order_id,
            "customer": customer.strip(),
            "status": status.strip(),
            "amount": amount
        }


def filter_orders_by_status(orders, required_status):
    """Yield only orders having the requested status."""

    for order in orders:

        if (
            order["status"].casefold()
            == required_status.casefold()
        ):
            yield order


def create_batches(items, batch_size):
    """Yield a small list containing each batch."""

    iterator = iter(items)

    while True:
        batch = list(
            islice(iterator, batch_size)
        )

        if not batch:
            break

        yield batch


def run_pipeline():
    order_lines = read_order_lines(DATA_FILE)

    parsed_orders = parse_orders(order_lines)

    ready_orders = filter_orders_by_status(
        parsed_orders,
        "Ready"
    )

    ready_batches = create_batches(
        ready_orders,
        batch_size=2
    )

    total_ready_orders = 0
    total_ready_revenue = 0

    print("=" * 50)
    print("KLYN READY-ORDER PROCESSING")
    print("=" * 50)

    for batch_number, batch in enumerate(
        ready_batches,
        start=1
    ):
        print(f"\nBATCH {batch_number}")

        for order in batch:
            print(
                f'{order["order_id"]} | '
                f'{order["customer"]} | '
                f'₹{order["amount"]}'
            )

            total_ready_orders += 1
            total_ready_revenue += order["amount"]

    print("\n" + "=" * 50)
    print("PROCESSING SUMMARY")
    print("=" * 50)

    print(
        "Total ready orders:",
        total_ready_orders
    )

    print(
        "Total ready revenue: ₹",
        total_ready_revenue,
        sep=""
    )


run_pipeline()