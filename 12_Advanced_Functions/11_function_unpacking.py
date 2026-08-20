# ==========================================
# FUNCTION UNPACKING
# ==========================================
#
# *  unpacks a list or tuple into positional arguments.
# ** unpacks a dictionary into keyword arguments.


# ==========================================
# EXAMPLE 1: UNPACK A LIST USING *
# ==========================================

def calculate_bill(
    quantity: int,
    price_per_item: float
) -> float:
    """Calculate the total laundry bill."""

    return quantity * price_per_item


# The list contains the two arguments required by calculate_bill().
bill_details = [3, 85.0]

# This:
# calculate_bill(*bill_details)
#
# becomes:
# calculate_bill(3, 85.0)

total_bill = calculate_bill(*bill_details)

print("=" * 40)
print("LIST UNPACKING")
print("=" * 40)
print("Bill details:", bill_details)
print("Total bill: ₹", total_bill, sep="")


# ==========================================
# EXAMPLE 2: UNPACK A TUPLE USING *
# ==========================================

def create_order_message(
    order_id: str,
    customer: str,
    status: str
) -> str:
    """Create an order-status message."""

    return (
        f"Dear {customer}, your order "
        f"{order_id} is {status}."
    )


# Tuple values must be in the same order as the parameters.
order_details = (
    "AO45821",
    "Ravi",
    "Ready"
)

# The tuple is unpacked into three positional arguments.
message = create_order_message(*order_details)

print("\n" + "=" * 40)
print("TUPLE UNPACKING")
print("=" * 40)
print(message)


# ==========================================
# EXAMPLE 3: UNPACK A DICTIONARY USING **
# ==========================================

def process_order(
    order_id: str,
    customer: str,
    quantity: int,
    price_per_item: float,
    status: str
) -> dict:
    """Process and return a complete laundry order."""

    amount = quantity * price_per_item

    return {
        "order_id": order_id,
        "customer": customer,
        "quantity": quantity,
        "price_per_item": price_per_item,
        "status": status,
        "amount": amount
    }


order_data = {
    "order_id": "AO33396",
    "customer": "Suresh",
    "quantity": 2,
    "price_per_item": 150.0,
    "status": "Processing"
}

# Dictionary keys are matched with function parameter names.
#
# process_order(**order_data)
#
# becomes:
# process_order(
#     order_id="AO33396",
#     customer="Suresh",
#     quantity=2,
#     price_per_item=150.0,
#     status="Processing"
# )

processed_order = process_order(**order_data)

print("\n" + "=" * 40)
print("DICTIONARY UNPACKING")
print("=" * 40)
print("Order ID:", processed_order["order_id"])
print("Customer:", processed_order["customer"])
print("Quantity:", processed_order["quantity"])
print("Status:", processed_order["status"])
print("Amount: ₹", processed_order["amount"], sep="")


# ==========================================
# EXAMPLE 4: COMBINE EXISTING COLLECTIONS
# ==========================================

morning_orders = [
    "AO10001",
    "AO10002"
]

evening_orders = [
    "AO10003",
    "AO10004"
]

# * extracts every value from both lists
# and places them inside a new list.
all_orders = [
    *morning_orders,
    *evening_orders
]

print("\n" + "=" * 40)
print("COMBINED ORDERS")
print("=" * 40)

for order_id in all_orders:
    print("Order:", order_id)


# ==========================================
# EXAMPLE 5: COMBINE DICTIONARIES
# ==========================================

basic_order = {
    "order_id": "AO98765",
    "customer": "Anjali"
}

additional_details = {
    "status": "Ready",
    "amount": 1750.0
}

# ** extracts all key-value pairs and creates one dictionary.
complete_order = {
    **basic_order,
    **additional_details
}

print("\n" + "=" * 40)
print("COMPLETE ORDER")
print("=" * 40)
print(complete_order)