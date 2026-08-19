# Basic type hints for KLYN Laundry


order_id: str = "AO45821"
customer_name: str = "Ravi Kumar"
quantity: int = 3
bill_amount: float = 1750.00
is_ready: bool = True


services: list[str] = [
    "Dry Cleaning",
    "Wash and Iron",
    "Steam Iron"
]


customer_details: dict[str, str] = {
    "name": "Ravi Kumar",
    "city": "Eluru",
    "phone": "9876543210"
}


garment_counts: tuple[int, int, int] = (
    3,
    2,
    1
)


supported_statuses: set[str] = {
    "Ready",
    "Processing",
    "Delivered"
}


print("Order ID:", order_id)
print("Customer:", customer_name)
print("Quantity:", quantity)
print("Bill amount: ₹", bill_amount, sep="")
print("Ready:", is_ready)

print("Services:", services)
print("Customer details:", customer_details)
print("Garment counts:", garment_counts)
print("Supported statuses:", supported_statuses)