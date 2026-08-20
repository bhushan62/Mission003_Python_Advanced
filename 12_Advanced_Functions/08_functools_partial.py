from functools import partial


# ==================================================
# BASE FUNCTION
# ==================================================

def calculate_bill(
    quantity: int,
    price_per_item: float,
    multiplier: float
) -> float:
    """Calculate the final laundry bill."""

    return quantity * price_per_item * multiplier


# ==================================================
# CREATE CUSTOMIZED FUNCTIONS
# ==================================================

# multiplier is permanently fixed at 1 for regular service.
regular_bill = partial(
    calculate_bill,
    multiplier=1.0
)


# multiplier is permanently fixed at 2 for express service.
express_bill = partial(
    calculate_bill,
    multiplier=2.0
)


# ==================================================
# USE THE CUSTOMIZED FUNCTIONS
# ==================================================

regular_total = regular_bill(
    quantity=4,
    price_per_item=85.0
)

express_total = express_bill(
    quantity=4,
    price_per_item=85.0
)


print("REGULAR SERVICE")
print("=" * 40)
print("Regular bill: ₹", regular_total, sep="")

print()

print("EXPRESS SERVICE")
print("=" * 40)
print("Express bill: ₹", express_total, sep="")


# ==================================================
# FIX THE PRICE OF A PARTICULAR GARMENT
# ==================================================

def calculate_service_bill(
    quantity: int,
    price_per_item: float
) -> float:
    """Calculate a bill using quantity and item price."""

    return quantity * price_per_item


# The shirt price is fixed at ₹85.
shirt_bill = partial(
    calculate_service_bill,
    price_per_item=85.0
)


shirt_total = shirt_bill(quantity=3)

print()
print("SHIRT SERVICE")
print("=" * 40)
print("3 shirts bill: ₹", shirt_total, sep="")


# ==================================================
# PREPARE A READY-ORDER MESSAGE
# ==================================================

def create_order_message(
    customer: str,
    order_id: str,
    status: str
) -> str:
    """Create a customer order-status message."""

    return (
        f"Dear {customer}, your order "
        f"{order_id} is {status}."
    )


# The status is permanently fixed as Ready.
create_ready_message = partial(
    create_order_message,
    status="Ready"
)


message = create_ready_message(
    customer="Ravi",
    order_id="AO45821"
)

print()
print("CUSTOMER NOTIFICATION")
print("=" * 40)
print(message)