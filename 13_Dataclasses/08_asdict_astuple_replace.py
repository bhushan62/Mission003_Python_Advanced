# Import dataclass tools.
from dataclasses import dataclass, asdict, astuple, replace


@dataclass
class LaundryOrder:
    """Store one KLYN laundry order."""

    order_id: str
    customer: str
    service: str
    quantity: int
    price_per_item: float
    status: str = "Processing"

    @property
    def total_amount(self) -> float:
        """Calculate the complete order amount."""
        return self.quantity * self.price_per_item

    def display(self) -> None:
        """Display the order details."""
        print("=" * 40)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print("Price per item: ₹", self.price_per_item, sep="")
        print("Status:", self.status)
        print("Total amount: ₹", self.total_amount, sep="")


# Create the original order.
original_order = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar",
    service="Shirt",
    quantity=3,
    price_per_item=85.0,
    status="Processing"
)


print("\nORIGINAL DATACLASS")
original_order.display()


# asdict() converts the dataclass object into a dictionary.
order_dictionary = asdict(original_order)

print("\nDATACLASS TO DICTIONARY")
print("=" * 40)
print(order_dictionary)
print("Customer:", order_dictionary["customer"])


# astuple() converts the dataclass object into a tuple.
order_tuple = astuple(original_order)

print("\nDATACLASS TO TUPLE")
print("=" * 40)
print(order_tuple)
print("Order ID:", order_tuple[0])


# replace() creates a NEW dataclass object with selected changes.
# It does not modify the original object.
ready_order = replace(
    original_order,
    status="Ready"
)

print("\nNEW READY ORDER")
ready_order.display()


# Create another updated copy.
express_order = replace(
    original_order,
    order_id="AO33396",
    customer="Suresh Babu",
    quantity=2,
    price_per_item=170.0,
    status="Ready"
)

print("\nEXPRESS ORDER COPY")
express_order.display()


# Prove that the original object was not changed.
print("\nORIGINAL OBJECT CHECK")
print("=" * 40)
print("Original status:", original_order.status)
print("Ready-copy status:", ready_order.status)

print(
    "Are they the same object?",
    original_order is ready_order
)