from pathlib import Path


FILE_PATH = Path(__file__).with_name("laundry_orders.txt")


def read_order_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


order_lines = read_order_lines(FILE_PATH)

print(next(order_lines))
print(next(order_lines))

def parse_orders(lines):
    for line in lines:
        order_id, customer, status, amount = line.split("|")

        yield {
            "order_id": order_id,
            "customer": customer,
            "status": status,
            "amount": int(amount)
        }

order_lines = read_order_lines(FILE_PATH)
parsed_orders = parse_orders(order_lines)

for order in parsed_orders:
    print(order)

def filter_orders_by_status(orders, required_status):
    for order in orders:
        if order["status"].casefold() == required_status.casefold():
            yield order

order_lines = read_order_lines(FILE_PATH)

parsed_orders = parse_orders(order_lines)

ready_orders = filter_orders_by_status(
    parsed_orders,
    "Ready"
)

for order in ready_orders:
    print(
        f'{order["order_id"]} | '
        f'{order["customer"]} | '
        f'₹{order["amount"]}'
    )