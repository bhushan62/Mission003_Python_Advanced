# ==========================================
# CONCEPT 5: filter()
# ==========================================
#
# filter() checks every item and keeps only
# the items for which the function returns True.
#
# Syntax:
# filter(condition_function, iterable)
#
# map()    -> transforms every item
# filter() -> selects matching items


# ==========================================
# EXAMPLE 1: FILTER READY ORDERS
# ==========================================

orders = [
    {
        "order_id": "AO45821",
        "customer": "Ravi",
        "status": "Ready",
        "amount": 1750.0
    },
    {
        "order_id": "AO33396",
        "customer": "Suresh",
        "status": "Processing",
        "amount": 1200.0
    },
    {
        "order_id": "AO98765",
        "customer": "Anjali",
        "status": "Ready",
        "amount": 850.0
    },
    {
        "order_id": "AO12345",
        "customer": "Kiran",
        "status": "Delivered",
        "amount": 2200.0
    }
]


# Return True only when the status is Ready.
def is_ready(order):
    return order["status"] == "Ready"


# filter() keeps only the Ready orders.
ready_orders = list(
    filter(is_ready, orders)
)

print("READY ORDERS")

for order in ready_orders:
    print(
        "-",
        order["order_id"],
        "|",
        order["customer"]
    )


# ==========================================
# EXAMPLE 2: FILTER HIGH-VALUE ORDERS
# ==========================================

# Keep orders whose amount is ₹1500 or more.
high_value_orders = list(
    filter(
        lambda order: order["amount"] >= 1500,
        orders
    )
)

print("\nHIGH-VALUE ORDERS")

for order in high_value_orders:
    print(
        "-",
        order["order_id"],
        "| ₹",
        order["amount"],
        sep=""
    )


# ==========================================
# EXAMPLE 3: FILTER VALID ORDER IDs
# ==========================================

order_ids = [
    "AO45821",
    "BO33396",
    "AO98765",
    "AO1234",
    "AO54321"
]


# A valid ID must begin with AO,
# contain exactly seven characters,
# and have five digits after AO.
def is_valid_order_id(order_id):
    return (
        len(order_id) == 7
        and order_id.startswith("AO")
        and order_id[2:].isdigit()
    )


valid_order_ids = list(
    filter(is_valid_order_id, order_ids)
)

print("\nVALID ORDER IDs")

for order_id in valid_order_ids:
    print("-", order_id)


# ==========================================
# EXAMPLE 4: FILTER ORDERS FOR NOTIFICATION
# ==========================================

# Send collection notifications only for Ready orders.
notification_orders = filter(
    lambda order: order["status"] == "Ready",
    orders
)

print("\nCOLLECTION NOTIFICATIONS")

for order in notification_orders:
    print(
        f"Dear {order['customer']}, "
        f"your order {order['order_id']} "
        f"is ready for collection."
    )