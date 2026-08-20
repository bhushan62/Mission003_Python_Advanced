# A lambda is a small anonymous function.
# Syntax:
# lambda parameters: returned_expression


# Regular pricing: quantity × price
regular_price = lambda quantity, price: quantity * price


# Express pricing: regular price × 2
express_price = lambda quantity, price: quantity * price * 2


# Calculate both bills.
regular_bill = regular_price(3, 85.0)
express_bill = express_price(3, 85.0)


print("Regular bill: ₹", regular_bill, sep="")
print("Express bill: ₹", express_bill, sep="")


print("\nUSING LAMBDA AS A FUNCTION ARGUMENT")
print("=" * 40)


def process_order(
    order_id: str,
    quantity: int,
    price_per_item: float,
    pricing_function
) -> float:
    """Calculate an order using the supplied pricing function."""

    # Execute the lambda function received through the parameter.
    final_amount = pricing_function(quantity, price_per_item)

    print("Order ID:", order_id)
    print("Final amount: ₹", final_amount, sep="")

    return final_amount


# Pass a lambda directly without creating a separate function.
# Express service costs twice the regular service price.
process_order(
    order_id="AO33396",
    quantity=4,
    price_per_item=85.0,
    pricing_function=lambda quantity, price: quantity * price * 2
)




