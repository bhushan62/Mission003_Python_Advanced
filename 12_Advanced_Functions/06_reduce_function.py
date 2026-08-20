# Import reduce because it is not a built-in function.
from functools import reduce


# ==========================================
# LAUNDRY ORDERS
# ==========================================

orders = [
    {
        "order_id": "AO45821",
        "customer": "Ravi",
        "status": "Ready",
        "quantity": 3,
        "amount": 1750.0
    },
    {
        "order_id": "AO33396",
        "customer": "Suresh",
        "status": "Processing",
        "quantity": 2,
        "amount": 1200.0
    },
    {
        "order_id": "AO98765",
        "customer": "Anjali",
        "status": "Ready",
        "quantity": 4,
        "amount": 2200.0
    }
]


# ==========================================
# EXAMPLE 1: CALCULATE TOTAL REVENUE
# ==========================================

# reduce() combines all order amounts into one final value.
#
# First execution:
# 0 + 1750 = 1750
#
# Second execution:
# 1750 + 1200 = 2950
#
# Third execution:
# 2950 + 2200 = 5150

total_revenue = reduce(
    lambda current_total, order:
        current_total + order["amount"],
    orders,
    0.0
)

print("Total revenue: ₹", total_revenue, sep="")


# ==========================================
# EXAMPLE 2: CALCULATE TOTAL GARMENTS
# ==========================================

# Start from 0 and add each order's quantity.
total_garments = reduce(
    lambda current_total, order:
        current_total + order["quantity"],
    orders,
    0
)

print("Total garments:", total_garments)


# ==========================================
# EXAMPLE 3: FIND THE HIGHEST-VALUE ORDER
# ==========================================

# Compare two orders and retain the one
# containing the larger amount.
highest_value_order = reduce(
    lambda current_order, next_order:
        current_order
        if current_order["amount"] >= next_order["amount"]
        else next_order,
    orders
)

print("\nHIGHEST-VALUE ORDER")
print("=" * 40)
print("Order ID:", highest_value_order["order_id"])
print("Customer:", highest_value_order["customer"])
print(
    "Amount: ₹",
    highest_value_order["amount"],
    sep=""
)


# ==========================================
# EXAMPLE 4: FILTER + REDUCE
# ==========================================

# Step 1: Keep only Ready orders.
ready_orders = filter(
    lambda order: order["status"] == "Ready",
    orders
)

# Step 2: Add the revenue of those Ready orders.
ready_order_revenue = reduce(
    lambda current_total, order:
        current_total + order["amount"],
    ready_orders,
    0.0
)

print(
    "\nReady-order revenue: ₹",
    ready_order_revenue,
    sep=""
)