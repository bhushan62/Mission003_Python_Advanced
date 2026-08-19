from contextlib import contextmanager, ExitStack
from pathlib import Path


FOLDER = Path(__file__).parent

INPUT_FILE = FOLDER / "09.orders_input.txt"
READY_FILE = FOLDER / "09.ready_orders.txt"
ERROR_FILE = FOLDER / "09.order_errors.txt"


# Create raw practice data
INPUT_FILE.write_text(
    "AO10001|Ravi|Ready|850\n"
    "AO10002|Suresh|Processing|1200\n"
    "BAD1003|Anjali|Ready|1750\n"
    "AO10004|Kiran|Ready|invalid\n"
    "AO10005|Lakshmi|Ready|2200\n",
    encoding="utf-8"
)


@contextmanager
def open_processing_files():
    print("Opening KLYN processing files")

    try:
        with ExitStack() as stack:
            input_file = stack.enter_context(
                open(INPUT_FILE, "r", encoding="utf-8")
            )

            ready_file = stack.enter_context(
                open(READY_FILE, "w", encoding="utf-8")
            )

            error_file = stack.enter_context(
                open(ERROR_FILE, "w", encoding="utf-8")
            )

            yield input_file, ready_file, error_file

    finally:
        print("All KLYN processing files closed")


def parse_order(order_line):
    parts = order_line.strip().split("|")

    if len(parts) != 4:
        raise ValueError("Order must contain four fields")

    order_id, customer, status, amount = parts

    if not (
        order_id.startswith("AO")
        and len(order_id) == 7
        and order_id[2:].isdigit()
    ):
        raise ValueError("Invalid order ID")

    return {
        "order_id": order_id,
        "customer": customer,
        "status": status,
        "amount": float(amount)
    }


ready_count = 0
ready_revenue = 0
error_count = 0


with open_processing_files() as files:
    input_file, ready_file, error_file = files

    for line_number, order_line in enumerate(
        input_file,
        start=1
    ):
        try:
            order = parse_order(order_line)

            if order["status"].casefold() == "ready":
                ready_file.write(
                    f'{order["order_id"]}|'
                    f'{order["customer"]}|'
                    f'{order["amount"]:.2f}\n'
                )

                ready_count += 1
                ready_revenue += order["amount"]

                print(
                    "Ready order:",
                    order["order_id"]
                )

        except (ValueError, IndexError) as error:
            error_file.write(
                f"Line {line_number}: {error}\n"
            )

            error_count += 1

            print(
                f"Line {line_number} rejected:",
                error
            )


print("\nPROCESSING SUMMARY")
print("=" * 40)
print("Ready orders:", ready_count)
print("Ready revenue: ₹", ready_revenue, sep="")
print("Rejected lines:", error_count)