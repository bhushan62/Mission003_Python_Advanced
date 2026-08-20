from functools import lru_cache, partial, reduce
from typing import Callable


print("=" * 55)
print("KLYN ADVANCED FUNCTIONS ORDER PROCESSOR")
print("=" * 55)


# =========================================================
# 1. CACHING SERVICE PRICES
# =========================================================

@lru_cache(maxsize=10)
def get_service_price(service: str) -> float:
    """
    Return the price of a laundry service.

    The result is cached. If the same service is requested
    again, Python returns the previously stored value.
    """

    print(f"Fetching price for {service}...")

    service_prices = {
        "shirt": 85.0,
        "trouser": 150.0,
        "saree": 250.0,
        "bedsheet": 200.0
    }

    return service_prices.get(service.casefold(), 0.0)


# =========================================================
# 2. POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
# =========================================================

def calculate_bill(
    quantity: int,
    price_per_item: float,
    /,                       # Values before / must be positional
    *,
    express: bool = False,   # Values after * must use keywords
    discount: float = 0
) -> float:
    """Calculate regular or express laundry bill."""

    total = quantity * price_per_item

    # Express service costs twice the regular amount.
    if express:
        total *= 2

    # Apply percentage discount.
    total -= total * discount / 100

    return total


# =========================================================
# 3. MAP FUNCTION — CLEAN ORDER DATA
# =========================================================

def clean_order(order: dict) -> dict:
    """Clean customer, service and status values."""

    # Copy the dictionary so the original data is unchanged.
    cleaned_order = order.copy()

    cleaned_order["customer"] = order["customer"].strip().title()
    cleaned_order["service"] = order["service"].strip().casefold()
    cleaned_order["status"] = order["status"].strip().title()

    return cleaned_order


# =========================================================
# 4. FILTER FUNCTION — VALIDATE ORDERS
# =========================================================

def is_valid_order(order: dict) -> bool:
    """Return True only when an order contains valid data."""

    valid_order_id = (
        isinstance(order["order_id"], str)
        and order["order_id"].startswith("AO")
        and len(order["order_id"]) == 7
        and order["order_id"][2:].isdigit()
    )

    valid_customer = bool(order["customer"])
    valid_quantity = order["quantity"] > 0
    valid_service = get_service_price(order["service"]) > 0

    return (
        valid_order_id
        and valid_customer
        and valid_quantity
        and valid_service
    )


# =========================================================
# 5. CLOSURE — REMEMBER PROCESSED ORDER COUNT
# =========================================================

def create_order_counter() -> Callable[[], int]:
    """Create a function that remembers its order count."""

    order_count = 0

    def count_order() -> int:
        nonlocal order_count

        order_count += 1
        return order_count

    return count_order


# Create one counter that remembers its state.
count_processed_order = create_order_counter()


# =========================================================
# 6. *ARGS AND **KWARGS — CREATE NOTIFICATION
# =========================================================

def create_notification(
    customer: str,
    *garments: str,
    **details: object
) -> str:
    """
    *garments receives multiple positional values.
    **details receives multiple keyword values.
    """

    garment_text = ", ".join(garments)

    return (
        f"Dear {customer}, your order {details['order_id']} "
        f"containing {garment_text} is {details['status']}. "
        f"Bill amount: ₹{details['amount']:.2f}"
    )


# =========================================================
# 7. PARTIAL — CREATE A PRECONFIGURED PRINT FUNCTION
# =========================================================

def display_notification(store_name: str, message: str) -> None:
    """Display a notification using the selected store name."""

    print(f"\n{store_name} NOTIFICATION")
    print(message)


# Store name is permanently supplied to this new function.
send_klyn_notification = partial(
    display_notification,
    "KLYN Laundry & Dry Cleaning"
)


# =========================================================
# 8. HIGHER-ORDER FUNCTION
# =========================================================

def process_order(
    order: dict,
    pricing_function: Callable[[int, float], float]
) -> dict:
    """
    Receive another function as an argument and use it
    to calculate the order amount.
    """

    price = get_service_price(order["service"])

    # pricing_function can contain regular or express logic.
    amount = pricing_function(
        order["quantity"],
        price
    )

    processed_order = order.copy()
    processed_order["amount"] = amount

    return processed_order


# =========================================================
# 9. RECURSION — DISPLAY ORDER IDs
# =========================================================

def display_order_ids(orders: list[dict], index: int = 0) -> None:
    """Display order IDs recursively."""

    # Base case: stop when every order is displayed.
    if index == len(orders):
        print("All valid order IDs displayed")
        return

    print("Order ID:", orders[index]["order_id"])

    # Recursive call using the next index.
    display_order_ids(orders, index + 1)


# =========================================================
# 10. SAMPLE KLYN ORDER DATA
# =========================================================

laundry_orders = [
    {
        "order_id": "AO45821",
        "customer": "  ravi kumar ",
        "service": " SHIRT ",
        "quantity": 3,
        "status": " ready ",
        "express": False,
        "discount": 0
    },
    {
        "order_id": "AO33396",
        "customer": "suresh babu",
        "service": "Saree",
        "quantity": 2,
        "status": "processing",
        "express": True,
        "discount": 10
    },
    {
        # Invalid prefix—this order will be rejected.
        "order_id": "BO98765",
        "customer": "Anjali",
        "service": "Trouser",
        "quantity": 2,
        "status": "Ready",
        "express": False,
        "discount": 0
    },
    {
        # Invalid quantity—this order will be rejected.
        "order_id": "AO11111",
        "customer": "Kiran",
        "service": "Bedsheet",
        "quantity": 0,
        "status": "Ready",
        "express": False,
        "discount": 0
    }
]


# =========================================================
# 11. CLEAN DATA USING MAP()
# =========================================================

cleaned_orders = list(
    map(clean_order, laundry_orders)
)


# =========================================================
# 12. VALIDATE DATA USING FILTER()
# =========================================================

valid_orders = list(
    filter(is_valid_order, cleaned_orders)
)


# =========================================================
# 13. PROCESS VALID ORDERS
# =========================================================

processed_orders: list[dict] = []

for order in valid_orders:

    # Select the required pricing logic.
    if order["express"]:
        pricing_strategy = lambda quantity, price: calculate_bill(
            quantity,
            price,
            express=True,
            discount=order["discount"]
        )
    else:
        pricing_strategy = lambda quantity, price: calculate_bill(
            quantity,
            price,
            express=False,
            discount=order["discount"]
        )

    processed_order = process_order(
        order,
        pricing_strategy
    )

    processed_orders.append(processed_order)

    current_count = count_processed_order()

    print("\n" + "=" * 55)
    print("PROCESSED ORDER NUMBER:", current_count)
    print("=" * 55)

    # Dictionary unpacking.
    print(
        "Order:",
        processed_order["order_id"],
        "| Customer:",
        processed_order["customer"],
        "| Amount: ₹",
        processed_order["amount"],
        sep=""
    )

    message = create_notification(
        processed_order["customer"],  # Normal positional argument
        processed_order["service"],   # Collected by *garments
        order_id=processed_order["order_id"],
        status=processed_order["status"],
        amount=processed_order["amount"]
    )

    send_klyn_notification(message)


# =========================================================
# 14. REDUCE — CALCULATE TOTAL REVENUE
# =========================================================

total_revenue = reduce(
    lambda current_total, order:
        current_total + order["amount"],
    processed_orders,
    0.0
)


# =========================================================
# 15. FINAL PROCESSING SUMMARY
# =========================================================

print("\n" + "=" * 55)
print("KLYN PROCESSING SUMMARY")
print("=" * 55)

print("Received orders:", len(laundry_orders))
print("Valid orders:", len(processed_orders))
print("Rejected orders:", len(laundry_orders) - len(processed_orders))
print("Total revenue: ₹", total_revenue, sep="")


print("\nVALID ORDER IDs")
display_order_ids(processed_orders)


print("\nCACHE INFORMATION")
print(get_service_price.cache_info())


print("\n" + "=" * 55)
print("KLYN ADVANCED FUNCTIONS PROJECT COMPLETED")
print("=" * 55)