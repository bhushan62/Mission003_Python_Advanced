from functools import wraps


def handle_errors(
    exceptions,
    default_return=None
):
    def decorator(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            try:
                return original_function(
                    *args,
                    **kwargs
                )

            except exceptions as error:
                error_name = type(error).__name__

                print("=" * 40)
                print("OPERATION FAILED")
                print("Function:", original_function.__name__)
                print("Error type:", error_name)
                print("Reason:", error)
                print("=" * 40)

                return default_return

        return wrapper

    return decorator

@handle_errors(
    exceptions=(
        KeyError,
        ValueError,
        TypeError
    ),
    default_return=0
)
def calculate_order_amount(order):
    quantity = int(order["quantity"])
    price = float(order["price"])

    return quantity * price

valid_order = {
    "order_id": "AO45821",
    "quantity": 3,
    "price": 85
}


invalid_quantity_order = {
    "order_id": "AO33396",
    "quantity": "three",
    "price": 85
}


missing_price_order = {
    "order_id": "AO98765",
    "quantity": 4
}

valid_total = calculate_order_amount(
    valid_order
)

print("Valid order total: ₹", valid_total, sep="")

print()


invalid_total = calculate_order_amount(
    invalid_quantity_order
)

print(
    "Invalid order total: ₹",
    invalid_total,
    sep=""
)

print()


missing_total = calculate_order_amount(
    missing_price_order
)

print(
    "Missing-price order total: ₹",
    missing_total,
    sep=""
)

