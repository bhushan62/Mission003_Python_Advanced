from dataclasses import dataclass


# @dataclass tells Python to automatically create:
# 1. __init__() for storing values
# 2. __repr__() for displaying the object
# 3. __eq__() for comparing objects
@dataclass
class LaundryOrder:
    # These are the fields every laundry order contains.
    order_id: str
    customer: str
    service: str
    quantity: int
    price_per_item: float
    status: str


# Create the first LaundryOrder object.
# The generated __init__() receives and stores these values.
order_one = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar",
    service="Shirt",
    quantity=3,
    price_per_item=85.0,
    status="Ready",
)


# Create another independent order object.
order_two = LaundryOrder(
    order_id="AO33396",
    customer="Suresh Babu",
    service="Dry Cleaning",
    quantity=2,
    price_per_item=150.0,
    status="Processing",
)


# Dataclass objects can be printed directly.
# The automatically generated __repr__() produces a readable result.
print("FIRST ORDER")
print("=" * 40)
print(order_one)

print("\nSECOND ORDER")
print("=" * 40)
print(order_two)


# Access individual fields using object.field_name.
print("\nORDER DETAILS")
print("=" * 40)
print("Order ID:", order_one.order_id)
print("Customer:", order_one.customer)
print("Service:", order_one.service)
print("Quantity:", order_one.quantity)
print("Price per item: ₹", order_one.price_per_item, sep="")
print("Status:", order_one.status)


# Fields are mutable by default, so their values can be changed.
order_two.status = "Ready"

print("\nUPDATED ORDER")
print("=" * 40)
print("Order ID:", order_two.order_id)
print("Updated status:", order_two.status)


# Dataclasses automatically compare the field values of two objects.
order_three = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar",
    service="Shirt",
    quantity=3,
    price_per_item=85.0,
    status="Ready",
)

print("\nOBJECT COMPARISON")
print("=" * 40)
print("order_one equals order_three:", order_one == order_three)
print("order_one equals order_two:", order_one == order_two)