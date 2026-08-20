# ============================================
# RECURSION
# A recursive function calls itself.
# Every recursive function needs:
# 1. Base case — stops the function
# 2. Recursive case — calls itself again
# ============================================


def count_orders(number: int) -> None:
    """Count laundry orders using recursion."""

    # Base case:
    # Stop recursion when number becomes zero.
    if number == 0:
        print("All orders processed")
        return

    print("Processing order:", number)

    # Recursive case:
    # Call the same function with a smaller number.
    count_orders(number - 1)


count_orders(5)


print("\n" + "=" * 40)
print("CALCULATE TOTAL GARMENTS")
print("=" * 40)


def calculate_total(quantities: list[int]) -> int:
    """Calculate total garments recursively."""

    # Base case:
    # An empty list has a total of zero.
    if not quantities:
        return 0

    # Take the first quantity.
    first_quantity = quantities[0]

    # Send the remaining quantities back
    # into the same function.
    remaining_total = calculate_total(quantities[1:])

    return first_quantity + remaining_total


garment_quantities: list[int] = [3, 2, 1, 4]

total_garments: int = calculate_total(garment_quantities)

print("Quantities:", garment_quantities)
print("Total garments:", total_garments)


print("\n" + "=" * 40)
print("ORDER-STATUS PROCESSING")
print("=" * 40)


orders: list[dict[str, str]] = [
    {"order_id": "AO45821", "status": "Ready"},
    {"order_id": "AO33396", "status": "Processing"},
    {"order_id": "AO98765", "status": "Delivered"},
]


def display_orders(
    order_list: list[dict[str, str]],
    index: int = 0
) -> None:
    """Display every order recursively."""

    # Base case:
    # Stop when the index reaches the list length.
    if index == len(order_list):
        print("Finished displaying orders")
        return

    current_order = order_list[index]

    print(
        current_order["order_id"],
        "|",
        current_order["status"]
    )

    # Process the next list position.
    display_orders(order_list, index + 1)


display_orders(orders)