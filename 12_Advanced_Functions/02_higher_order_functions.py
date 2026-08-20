# This function calculates a regular laundry bill.
def calculate_regular_price(
    quantity: int,
    price_per_item: float
) -> float:
    return quantity * price_per_item


# This function calculates an express laundry bill.
# Express service costs twice the regular amount.
def calculate_express_price(
    quantity: int,
    price_per_item: float
) -> float:
    regular_amount = quantity * price_per_item
    return regular_amount * 2


# This is a higher-order function.
# It receives another function through pricing_function.
def process_order(
    order_id: str,
    quantity: int,
    price_per_item: float,
    pricing_function
) -> float:

    # Call the function received through pricing_function.
    final_amount = pricing_function(
        quantity,
        price_per_item
    )

    print("Order ID:", order_id)
    print("Quantity:", quantity)
    print("Final amount: ₹", final_amount, sep="")

    # Send the calculated amount back to the caller.
    return final_amount


print("REGULAR ORDER")
print("=" * 40)

# Pass calculate_regular_price as an argument.
# There are no parentheses because we are passing the function itself.
regular_bill = process_order(
    order_id="AO45821",
    quantity=3,
    price_per_item=85.0,
    pricing_function=calculate_regular_price
)


print("\nEXPRESS ORDER")
print("=" * 40)

# The same process_order function can use different pricing logic.
express_bill = process_order(
    order_id="AO33396",
    quantity=3,
    price_per_item=85.0,
    pricing_function=calculate_express_price
)