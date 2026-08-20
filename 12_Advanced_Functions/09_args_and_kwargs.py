# ==========================================
# 09_args_and_kwargs.py
# ==========================================


# ==========================================
# PART 1: *args
# ==========================================

print("=" * 45)
print("*ARGS - MULTIPLE POSITIONAL ARGUMENTS")
print("=" * 45)


def calculate_garment_total(*prices: float) -> float:
    # *args collects all positional values into a tuple.
    print("Received prices:", prices)

    return sum(prices)


total_amount = calculate_garment_total(
    85.0,     # Shirt
    150.0,    # Trouser
    200.0     # Saree
)

print("Total amount: ₹", total_amount, sep="")


# ==========================================
# PART 2: LOOPING THROUGH *args
# ==========================================

print("\n" + "=" * 45)
print("GARMENTS USING *ARGS")
print("=" * 45)


def display_garments(*garments: str) -> None:
    # garments is a tuple containing every garment.
    for serial_number, garment in enumerate(
        garments,
        start=1
    ):
        print(f"{serial_number}. {garment}")


display_garments(
    "Shirt",
    "Trouser",
    "Saree",
    "Bedsheet"
)


# ==========================================
# PART 3: **kwargs
# ==========================================

print("\n" + "=" * 45)
print("**KWARGS - MULTIPLE KEYWORD ARGUMENTS")
print("=" * 45)


def display_order_details(**details: object) -> None:
    # **kwargs collects keyword arguments into a dictionary.
    print("Received details:", details)

    for key, value in details.items():
        # Convert order_id into Order Id for display.
        clean_key = key.replace("_", " ").title()

        print(f"{clean_key}: {value}")


display_order_details(
    order_id="AO45821",
    customer="Ravi",
    status="Ready",
    service="Dry Cleaning",
    amount=850.0
)


# ==========================================
# PART 4: NORMAL ARGUMENT + *args + **kwargs
# ==========================================

print("\n" + "=" * 45)
print("COMPLETE KLYN LAUNDRY ORDER")
print("=" * 45)


def create_laundry_order(
    customer: str,
    *garments: str,
    **details: object
) -> dict[str, object]:

    # customer receives the first normal argument.
    # garments receives additional positional arguments.
    # details receives all keyword arguments.

    order: dict[str, object] = {
        "customer": customer,
        "garments": list(garments),
        **details
    }

    return order


laundry_order = create_laundry_order(
    "Ravi",             # Normal argument
    "Shirt",            # Goes into *garments
    "Trouser",
    "Saree",
    order_id="AO45821",  # Goes into **details
    status="Ready",
    amount=850.0
)


print("Order ID:", laundry_order["order_id"])
print("Customer:", laundry_order["customer"])
print("Garments:", laundry_order["garments"])
print("Status:", laundry_order["status"])
print("Amount: ₹", laundry_order["amount"], sep="")


# ==========================================
# PART 5: CUSTOMER NOTIFICATION
# ==========================================

print("\n" + "=" * 45)
print("CUSTOMER NOTIFICATION")
print("=" * 45)


def create_notification(
    customer: str,
    **order_details: object
) -> str:

    order_id = order_details.get(
        "order_id",
        "Not provided"
    )

    status = order_details.get(
        "status",
        "Unknown"
    )

    amount = order_details.get(
        "amount",
        0
    )

    return (
        f"Dear {customer}, your order {order_id} "
        f"is {status}. Amount: ₹{amount}"
    )


message = create_notification(
    "Ravi",
    order_id="AO45821",
    status="Ready",
    amount=850.0
)

print(message)