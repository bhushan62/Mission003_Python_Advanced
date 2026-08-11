# import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("KLYN automation started")
# logging.warning("Customer phone number missing")
# logging.error("Invoice generation failed")


import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Connecting to KLYN database")
logging.info("KLYN automation started")
logging.warning("Customer phone number missing")
logging.error("Invoice generation failed")
logging.critical("Database connection completely failed")