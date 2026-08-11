import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

try:
    amount = 500
    customers = 0

    average = amount / customers

except ZeroDivisionError:
    logging.exception("Failed to calculate average customer billing")