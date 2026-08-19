def calculate_bill(
    quantity: int,
    price_per_item: float,
    discount_percentage: float = 0.0
) -> float:
    subtotal: float = quantity * price_per_item

    discount: float = (
        subtotal * discount_percentage / 100
    )

    final_amount: float = subtotal - discount

    return final_amount


def create_ready_message(
    order_id: str,
    customer: str
) -> str:
    message: str = (
        f"Hello {customer}, "
        f"your order {order_id} is ready."
    )

    return message


def display_message(message: str) -> None:
    print(message)


bill: float = calculate_bill(
    quantity=3,
    price_per_item=85.0,
    discount_percentage=10.0
)


ready_message: str = create_ready_message(
    order_id="AO45821",
    customer="Ravi"
)


print("Final bill: ₹", bill, sep="")

display_message(ready_message)