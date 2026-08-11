import logging

# --------------------------------
# Logging configuration
# --------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# --------------------------------
# Sample KLYN orders
# --------------------------------

orders = [
    {"id": 101, "customer": "Ravi", "amount": 850},
    {"id": 102, "customer": "Anil", "amount": 0},
    {"id": 103, "customer": "Priya", "amount": 1250},
]


# --------------------------------
# Process each order
# --------------------------------

for order in orders:

    logging.info(
        f"Processing order {order['id']}"
    )

    if order["amount"] == 0:

        logging.warning(
            f"Order {order['id']} has zero amount"
        )

    else:

        logging.info(
            f"Order {order['id']} processed successfully"
        )