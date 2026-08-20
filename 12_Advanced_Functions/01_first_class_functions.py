# This function calculates the normal laundry bill.
# quantity: number of garments
# price_per_item: cleaning charge for one garment
# return: final calculated amount
def calculate_regular_bill(
    quantity: int,
    price_per_item: float
) -> float:
    return quantity * price_per_item


# We are storing the function itself in another variable.
# No parentheses means the function is NOT executed here.
selected_pricing = calculate_regular_bill


# Here we call the stored function using parentheses.
# selected_pricing now behaves like calculate_regular_bill.
regular_total = selected_pricing(
    quantity=3,
    price_per_item=85.0
)


# Display the calculated bill.
print("Regular total: ₹", regular_total)