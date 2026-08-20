# ============================================
# POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
# ============================================


def process_order(
    order_id: str,       # Positional-only parameter
    /,                   # Everything before / must use position
    customer: str,       # Can be positional or keyword
    *,
    status: str,         # Everything after * must use keyword
    amount: float
) -> None:

    print("=" * 40)
    print("ORDER DETAILS")
    print("=" * 40)

    print("Order ID:", order_id)
    print("Customer:", customer)
    print("Status:", status)
    print("Amount: ₹", amount, sep="")


# Correct:
# order_id is supplied by position.
# status and amount are supplied using their names.
process_order(
    "AO45821",
    "Ravi",
    status="Ready",
    amount=1750.0
)


# ============================================
# PRACTICAL KLYN BILLING EXAMPLE
# ============================================


def calculate_bill(
    quantity: int,          # Positional-only
    price_per_item: float,  # Positional-only
    /,
    *,
    express: bool = False,  # Keyword-only
    discount: float = 0.0   # Keyword-only
) -> float:

    # Calculate the normal bill.
    total = quantity * price_per_item

    # Express service costs twice the normal amount.
    if express:
        total *= 2

    # Apply discount after calculating service cost.
    total -= total * discount / 100

    return total


regular_bill = calculate_bill(
    3,
    85.0,
    express=False,
    discount=0
)

express_bill = calculate_bill(
    3,
    85.0,
    express=True,
    discount=10
)

print("\n" + "=" * 40)
print("BILL RESULTS")
print("=" * 40)

print("Regular bill: ₹", regular_bill, sep="")
print("Express bill after discount: ₹", express_bill, sep="")


# ============================================
# INVALID EXAMPLES — KEEP COMMENTED
# ============================================

# Wrong: quantity is positional-only.
# calculate_bill(
#     quantity=3,
#     price_per_item=85.0,
#     express=True
# )

# Wrong: express is keyword-only.
# calculate_bill(3, 85.0, True, 10)