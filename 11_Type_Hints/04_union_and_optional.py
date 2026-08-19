def calculate_service_charge(
    amount: int | float
) -> float:
    return float(amount) * 0.05


def find_order_amount(
    order_id: str,
    orders: dict[str, float]
) -> float | None:
    if order_id in orders:
        return orders[order_id]

    return None


def create_contact_message(
    customer: str,
    phone: str | None
) -> str:
    if phone is None:
        return (
            f"No phone number available for {customer}"
        )

    return (
        f"Contact {customer} at {phone}"
    )


order_amounts: dict[str, float] = {
    "AO10001": 850.0,
    "AO10002": 1200.0
}


service_charge: float = calculate_service_charge(
    1000
)

existing_amount: float | None = find_order_amount(
    "AO10001",
    order_amounts
)

missing_amount: float | None = find_order_amount(
    "AO99999",
    order_amounts
)


message_one: str = create_contact_message(
    customer="Ravi",
    phone="9876543210"
)

message_two: str = create_contact_message(
    customer="Suresh",
    phone=None
)


print("Service charge: ₹", service_charge, sep="")
print("Existing amount:", existing_amount)
print("Missing amount:", missing_amount)
print(message_one)
print(message_two)