from functools import lru_cache, partial, reduce
from typing import Callable


# ============================================================
# SAMPLE LAUNDRY DATA
# ============================================================

orders = [
    {
        "order_id": "AO45821",
        "customer": "Ravi Kumar",
        "garment": "shirt",
        "quantity": 3,
        "status": "Ready",
    },
    {
        "order_id": "AO33396",
        "customer": "Suresh Babu",
        "garment": "saree",
        "quantity": 2,
        "status": "Processing",
    },
    {
        "order_id": "AO98765",
        "customer": "Anjali Devi",
        "garment": "trouser",
        "quantity": 4,
        "status": "Ready",
    },
]


def heading(title: str) -> None:
    """Print a formatted heading."""

    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


# ============================================================
# 1. FIRST-CLASS FUNCTIONS
# A function can be stored inside a variable.
# ============================================================

heading("1. FIRST-CLASS FUNCTIONS")


def calculate_regular_bill(
    quantity: int,
    price_per_item: float,
) -> float:
    """Calculate a regular laundry bill."""

    return quantity * price_per_item


# Store the function itself. No parentheses are used here.
selected_pricing = calculate_regular_bill

# Call the function through the new variable.
regular_total = selected_pricing(
    quantity=3,
    price_per_item=85.0,
)

print("Regular total: ₹", regular_total, sep="")


# ============================================================
# 2. HIGHER-ORDER FUNCTIONS
# A function receives another function as an argument.
# ============================================================

heading("2. HIGHER-ORDER FUNCTIONS")


def calculate_regular_price(
    quantity: int,
    price: float,
) -> float:
    """Calculate the normal service price."""

    return quantity * price


def calculate_express_price(
    quantity: int,
    price: float,
) -> float:
    """Express service costs twice the regular price."""

    return quantity * price * 2


def process_order(
    order_id: str,
    quantity: int,
    price_per_item: float,
    pricing_function: Callable[[int, float], float],
) -> float:
    """Process an order using the supplied pricing function."""

    final_amount = pricing_function(
        quantity,
        price_per_item,
    )

    print("Order ID:", order_id)
    print("Final amount: ₹", final_amount, sep="")

    return final_amount


regular_bill = process_order(
    order_id="AO45821",
    quantity=3,
    price_per_item=85.0,
    pricing_function=calculate_regular_price,
)

express_bill = process_order(
    order_id="AO33396",
    quantity=3,
    price_per_item=85.0,
    pricing_function=calculate_express_price,
)


# ============================================================
# 3. LAMBDA FUNCTION
# Lambda creates a small anonymous function.
# ============================================================

heading("3. LAMBDA FUNCTION")

lambda_bill = process_order(
    order_id="AO98765",
    quantity=4,
    price_per_item=85.0,

    # Express price is twice the normal price.
    pricing_function=lambda quantity, price: quantity * price * 2,
)

print("Lambda express bill: ₹", lambda_bill, sep="")


# ============================================================
# 4. MAP()
# map() transforms every value in an iterable.
# ============================================================

heading("4. MAP FUNCTION")

quantities = [2, 3, 4, 5]
shirt_price = 85.0

# Calculate an amount for every quantity.
order_amounts = list(
    map(
        lambda quantity: quantity * shirt_price,
        quantities,
    )
)

print("Quantities:", quantities)
print("Order amounts:", order_amounts)

customer_names = [
    "   Ravi Kumar   ",
    " Suresh Babu ",
    "    Anjali Devi  ",
]

# Remove unnecessary spaces from every customer name.
clean_customer_names = list(
    map(
        lambda customer: customer.strip(),
        customer_names,
    )
)

print("Clean customer names:", clean_customer_names)


# ============================================================
# 5. FILTER()
# filter() keeps only values that pass a condition.
# ============================================================

heading("5. FILTER FUNCTION")

ready_orders = list(
    filter(
        lambda order: order["status"] == "Ready",
        orders,
    )
)

print("Ready orders:")

for order in ready_orders:
    print(
        "-",
        order["order_id"],
        "|",
        order["customer"],
    )


# ============================================================
# 6. REDUCE()
# reduce() combines multiple values into one final value.
# ============================================================

heading("6. REDUCE FUNCTION")

total_quantity = reduce(
    lambda current_total, order:
        current_total + order["quantity"],
    orders,
    0,
)

print("Total garments:", total_quantity)

amounts = [255.0, 900.0, 680.0]

total_revenue = reduce(
    lambda current_total, amount:
        current_total + amount,
    amounts,
    0.0,
)

print("Total revenue: ₹", total_revenue, sep="")


# ============================================================
# 7. CLOSURE
# The inner function remembers the outer function's variable.
# ============================================================

heading("7. CLOSURE")


def create_order_counter() -> Callable[[], int]:
    """Create an order counter using a closure."""

    order_count = 0

    def count_order() -> int:
        # Modify the variable belonging to the outer function.
        nonlocal order_count

        order_count += 1
        return order_count

    return count_order


count_processed_order = create_order_counter()

print("Processed order:", count_processed_order())
print("Processed order:", count_processed_order())
print("Processed order:", count_processed_order())


def create_price_calculator(
    multiplier: float,
) -> Callable[[int, float], float]:
    """Return a pricing function that remembers multiplier."""

    def calculate(
        quantity: int,
        price: float,
    ) -> float:
        return quantity * price * multiplier

    return calculate


regular_calculator = create_price_calculator(1)
express_calculator = create_price_calculator(2)

print(
    "Closure regular bill: ₹",
    regular_calculator(3, 85.0),
    sep="",
)

print(
    "Closure express bill: ₹",
    express_calculator(3, 85.0),
    sep="",
)


# ============================================================
# 8. FUNCTOOLS.PARTIAL
# partial() permanently fixes some function arguments.
# ============================================================

heading("8. FUNCTOOLS.PARTIAL")


def calculate_service_bill(
    quantity: int,
    price: float,
    multiplier: float,
) -> float:
    """Calculate the bill using the supplied multiplier."""

    return quantity * price * multiplier


# Fix multiplier at 1 for regular service.
regular_service = partial(
    calculate_service_bill,
    multiplier=1,
)

# Fix multiplier at 2 for express service.
express_service = partial(
    calculate_service_bill,
    multiplier=2,
)

print(
    "Regular service: ₹",
    regular_service(quantity=3, price=85.0),
    sep="",
)

print(
    "Express service: ₹",
    express_service(quantity=3, price=85.0),
    sep="",
)


def create_order_message(
    customer: str,
    order_id: str,
    status: str,
) -> str:
    """Create an order-status message."""

    return (
        f"Dear {customer}, your order "
        f"{order_id} is {status}."
    )


# Permanently fix the status as Ready.
create_ready_message = partial(
    create_order_message,
    status="Ready",
)

print(
    create_ready_message(
        customer="Ravi",
        order_id="AO45821",
    )
)


# ============================================================
# 9. *ARGS AND **KWARGS
# *args receives multiple positional arguments as a tuple.
# **kwargs receives keyword arguments as a dictionary.
# ============================================================

heading("9. ARGS AND KWARGS")


def calculate_multiple_prices(*prices: float) -> float:
    """Add any number of prices."""

    print("*args values:", prices)
    return sum(prices)


combined_price = calculate_multiple_prices(
    85.0,
    150.0,
    250.0,
)

print("Combined price: ₹", combined_price, sep="")


def display_order(**order_details: object) -> None:
    """Display any number of keyword order details."""

    print("**kwargs values:", order_details)

    for key, value in order_details.items():
        print(f"{key}: {value}")


display_order(
    order_id="AO45821",
    customer="Ravi Kumar",
    status="Ready",
    amount=255.0,
)


def create_complete_order(
    customer: str,
    *garments: str,
    **details: object,
) -> dict[str, object]:
    """Combine a customer, garments and extra information."""

    return {
        "customer": customer,
        "garments": list(garments),
        **details,
    }


complete_order = create_complete_order(
    "Ravi Kumar",
    "Shirt",
    "Trouser",
    "Saree",
    order_id="AO45821",
    status="Ready",
    amount=850.0,
)

print("Complete order:", complete_order)


# ============================================================
# 10. RECURSION
# A recursive function calls itself.
# It must have a base case to stop recursion.
# ============================================================

heading("10. RECURSION")


def count_orders(number: int) -> None:
    """Count orders backwards using recursion."""

    # Base case: stop when number reaches zero.
    if number == 0:
        print("All orders processed")
        return

    print("Processing order:", number)

    # Recursive case: call the function with a smaller number.
    count_orders(number - 1)


count_orders(5)


def calculate_total_garments(
    quantities: list[int],
) -> int:
    """Calculate total garments recursively."""

    # An empty list has a total of zero.
    if not quantities:
        return 0

    # Add the first number to the remaining list's total.
    return quantities[0] + calculate_total_garments(
        quantities[1:]
    )


garment_quantities = [3, 2, 1, 4]

print(
    "Recursive garment total:",
    calculate_total_garments(garment_quantities),
)


# ============================================================
# 11. FUNCTION ARGUMENT UNPACKING
# * unpacks lists and tuples.
# ** unpacks dictionaries.
# ============================================================

heading("11. FUNCTION ARGUMENT UNPACKING")


def calculate_bill(
    quantity: int,
    price: float,
) -> float:
    """Calculate a simple bill."""

    return quantity * price


bill_details = [3, 85.0]

# Same as calculate_bill(3, 85.0).
unpacked_bill = calculate_bill(*bill_details)

print("List-unpacked bill: ₹", unpacked_bill, sep="")


def show_notification(
    customer: str,
    order_id: str,
    status: str,
) -> None:
    """Display a customer notification."""

    print(
        f"Dear {customer}, your order "
        f"{order_id} is {status}."
    )


notification_details = (
    "Ravi",
    "AO45821",
    "Ready",
)

show_notification(*notification_details)


def show_order(
    order_id: str,
    customer: str,
    amount: float,
) -> None:
    """Display order information."""

    print("Order ID:", order_id)
    print("Customer:", customer)
    print("Amount: ₹", amount, sep="")


order_details = {
    "order_id": "AO33396",
    "customer": "Suresh",
    "amount": 300.0,
}

# Dictionary keys must match the parameter names.
show_order(**order_details)


# Combine multiple lists using unpacking.
morning_orders = ["AO10001", "AO10002"]
evening_orders = ["AO10003", "AO10004"]

combined_orders = [
    *morning_orders,
    *evening_orders,
]

print("Combined orders:", combined_orders)


# ============================================================
# 12. POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
#
# Parameters before / must be positional.
# Parameters after * must be keyword arguments.
# ============================================================

heading("12. POSITIONAL-ONLY AND KEYWORD-ONLY")


def calculate_advanced_bill(
    quantity: int,
    price: float,
    /,
    *,
    express: bool = False,
    discount: float = 0,
) -> float:
    """
    quantity and price are positional-only.

    express and discount are keyword-only.
    """

    total = quantity * price

    if express:
        # Express service costs twice the regular amount.
        total *= 2

    # Apply a percentage discount.
    total -= total * discount / 100

    return total


advanced_regular_bill = calculate_advanced_bill(
    3,
    85.0,
    express=False,
    discount=0,
)

advanced_express_bill = calculate_advanced_bill(
    3,
    85.0,
    express=True,
    discount=10,
)

print(
    "Advanced regular bill: ₹",
    advanced_regular_bill,
    sep="",
)

print(
    "Advanced express bill: ₹",
    advanced_express_bill,
    sep="",
)


# ============================================================
# 13. CACHING WITH LRU_CACHE
# A cached function remembers earlier results.
# ============================================================

heading("13. FUNCTION CACHING")


@lru_cache(maxsize=10)
def get_service_price(service: str) -> float:
    """Simulate retrieving a price from a database or API."""

    print(f"Fetching price for {service}...")

    price_list = {
        "shirt": 85.0,
        "trouser": 100.0,
        "saree": 250.0,
        "bedsheet": 200.0,
    }

    return price_list.get(service.casefold(), 0.0)


# First request: function executes normally.
shirt_price_one = get_service_price("shirt")

# Second request: result comes from the cache.
shirt_price_two = get_service_price("shirt")

# New service: function executes normally.
saree_price = get_service_price("saree")

print("First shirt price: ₹", shirt_price_one, sep="")
print("Second shirt price: ₹", shirt_price_two, sep="")
print("Saree price: ₹", saree_price, sep="")
print("Cache information:", get_service_price.cache_info())


# ============================================================
# 14. INTEGRATED KLYN ORDER PROCESSOR
# Combines filtering, mapping, reduce, caching and closures.
# ============================================================

heading("14. KLYN INTEGRATED ORDER PROCESSOR")


def is_valid_order(order: dict[str, object]) -> bool:
    """Validate the basic order information."""

    order_id = order.get("order_id")
    customer = order.get("customer")
    quantity = order.get("quantity")
    garment = order.get("garment")

    return (
        isinstance(order_id, str)
        and order_id.startswith("AO")
        and len(order_id) == 7
        and isinstance(customer, str)
        and bool(customer.strip())
        and isinstance(quantity, int)
        and quantity > 0
        and isinstance(garment, str)
    )


def calculate_order_amount(
    order: dict[str, object],
) -> float:
    """Calculate the amount of one validated order."""

    garment = str(order["garment"])
    quantity = int(order["quantity"])

    price = get_service_price(garment)

    return quantity * price


# Keep only valid orders.
valid_orders = list(
    filter(
        is_valid_order,
        orders,
    )
)

# Calculate the amount for every valid order.
valid_order_amounts = list(
    map(
        calculate_order_amount,
        valid_orders,
    )
)

# Add every calculated amount.
integrated_revenue = reduce(
    lambda current_total, amount:
        current_total + amount,
    valid_order_amounts,
    0.0,
)

print("Received orders:", len(orders))
print("Valid orders:", len(valid_orders))
print("Rejected orders:", len(orders) - len(valid_orders))
print("Order amounts:", valid_order_amounts)
print("Total revenue: ₹", integrated_revenue, sep="")

print("\nVALID ORDER DETAILS")

for number, (order, amount) in enumerate(
    zip(
        valid_orders,
        valid_order_amounts,
        strict=True,
    ),
    start=1,
):
    print("-" * 45)
    print("Order number:", number)
    print("Order ID:", order["order_id"])
    print("Customer:", order["customer"])
    print("Status:", order["status"])
    print("Amount: ₹", amount, sep="")


# ============================================================
# FINAL RESULT
# ============================================================

heading("ADVANCED FUNCTIONS FINAL TEST COMPLETED")

print("Concepts revised:")

concepts = [
    "First-class functions",
    "Higher-order functions",
    "Lambda",
    "map()",
    "filter()",
    "reduce()",
    "Closures and nonlocal",
    "functools.partial",
    "*args and **kwargs",
    "Recursion",
    "Argument unpacking",
    "Positional-only arguments",
    "Keyword-only arguments",
    "lru_cache",
    "Integrated order processing",
]

for number, concept in enumerate(concepts, start=1):
    print(f"{number}. {concept}")