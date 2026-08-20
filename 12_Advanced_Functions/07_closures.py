# ==========================================
# ADVANCED FUNCTIONS: CLOSURES
# ==========================================


def create_price_calculator(service_charge: float):
    """
    The outer function receives and stores service_charge.
    """

    # This inner function remembers service_charge.
    def calculate_bill(
        quantity: int,
        price_per_item: float
    ) -> float:

        regular_amount = quantity * price_per_item
        final_amount = regular_amount + service_charge

        return final_amount

    # Return the function itself—do not use parentheses here.
    return calculate_bill


# Create separate calculators with different remembered charges.
regular_calculator = create_price_calculator(
    service_charge=0
)

express_calculator = create_price_calculator(
    service_charge=200
)


regular_bill = regular_calculator(
    quantity=4,
    price_per_item=85.0
)

express_bill = express_calculator(
    quantity=4,
    price_per_item=85.0
)


print("Regular bill: ₹", regular_bill, sep="")
print("Express bill: ₹", express_bill, sep="")



#non-local

print("\n" + "=" * 40)
print("CLOSURE WITH NONLOCAL")
print("=" * 40)


def create_order_counter():
    # This variable belongs to the outer function.
    order_count = 0

    def count_order() -> int:
        # nonlocal allows us to modify the outer variable.
        nonlocal order_count

        order_count += 1
        return order_count

    return count_order


# The returned function remembers order_count.
count_processed_order = create_order_counter()


print("Processed order:", count_processed_order())
print("Processed order:", count_processed_order())
print("Processed order:", count_processed_order())