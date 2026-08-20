# ============================================
# EXAMPLE 1: CALCULATE GARMENT PRICES
# ============================================

# Quantities of different orders.
quantities = [2, 3, 4, 5]

price_per_item = 85.0


# Apply this calculation to every quantity.
def calculate_amount(quantity: int) -> float:
    return quantity * price_per_item


# map() processes each quantity one by one.
# list() converts the map result into a visible list.
order_amounts = list(
    map(calculate_amount, quantities)
)

print("Quantities:", quantities)
print("Order amounts:", order_amounts)


# ============================================
# EXAMPLE 2: MAP WITH LAMBDA
# ============================================

regular_prices = [100.0, 200.0, 350.0, 500.0]


# Double every regular price for express service.
express_prices = list(
    map(
        lambda price: price * 2,
        regular_prices
    )
)

print("\nRegular prices:", regular_prices)
print("Express prices:", express_prices)


# ============================================
# EXAMPLE 3: CLEAN CUSTOMER NAMES
# ============================================

customer_names = [
    "  ravi kumar  ",
    "SURESH BABU",
    "  anjali devi"
]


# strip() removes outside spaces.
# title() converts the name to title case.
clean_names = list(
    map(
        lambda name: name.strip().title(),
        customer_names
    )
)

print("\nClean customer names:")

for customer in clean_names:
    print("-", customer)


# ============================================
# EXAMPLE 4: CREATE ORDER MESSAGES
# ============================================

order_ids = [
    "AO45821",
    "AO33396",
    "AO98765"
]


# Create one message for every order ID.
order_messages = list(
    map(
        lambda order_id: f"Order {order_id} is ready.",
        order_ids
    )
)

print("\nORDER MESSAGES")

for message in order_messages:
    print(message)