import logging

logging.basicConfig(
    filename="klyn.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("KLYN automation started")
logging.info("Processing customer order")
logging.warning("Customer phone number missing")
logging.error("Invoice generation failed")