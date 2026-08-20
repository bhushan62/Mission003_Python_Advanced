from dataclasses import dataclass


# slots=True:
# - Prevents adding unexpected attributes.
# - Can reduce memory usage when creating many objects.
#
# kw_only=True:
# - Forces us to write parameter names while creating an object.
# - Makes large business objects easier to read and prevents argument mistakes.
@dataclass(slots=True, kw_only=True)
class LaundryOrder:
    order_id: str
    customer: str
    service: str
    quantity: int
    price_per_item: float
    status: str = "Processing"

    def __post_init__(self) -> None:
        """Validate the order immediately after object creation."""

        if not self.order_id.startswith("AO"):
            raise ValueError("Order ID must begin with AO")

        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if self.price_per_item <= 0:
            raise ValueError("Price must be greater than zero")

    @property
    def total_amount(self) -> float:
        """Calculate and return the total order amount."""
        return self.quantity * self.price_per_item

    def display(self) -> None:
        """Display the complete laundry order."""

        print("=" * 40)
        print("KLYN LAUNDRY ORDER")
        print("=" * 40)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print("Price per item: ₹", self.price_per_item, sep="")
        print("Status:", self.status)
        print("Total amount: ₹", self.total_amount, sep="")


# Because kw_only=True is enabled, every value must use its field name.
order_one = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar",
    service="Shirt",
    quantity=3,
    price_per_item=85.0,
    status="Ready"
)

order_one.display()


# Existing fields can still be changed because frozen=True was not used.
print("\nUPDATING AN EXISTING FIELD")
print("=" * 40)

order_one.status = "Delivered"

print("Updated status:", order_one.status)


# slots=True prevents us from creating an unknown field.
print("\nTRYING TO ADD AN UNKNOWN FIELD")
print("=" * 40)

try:
    # delivery_agent is not declared in the dataclass.
    order_one.delivery_agent = "Kiran"

except AttributeError as error:
    print("New attribute rejected")
    print("Reason:", error)


# This intentionally demonstrates the effect of kw_only=True.
print("\nPOSITIONAL ARGUMENT TEST")
print("=" * 40)

try:
    # This fails because kw_only=True requires named arguments.
    invalid_order = LaundryOrder(
        "AO33396",
        "Suresh Babu",
        "Saree",
        2,
        250.0
    )

except TypeError as error:
    print("Positional arguments rejected")
    print("Reason:", error)


# Correct keyword-only object creation.
print("\nSECOND VALID ORDER")
print("=" * 40)

order_two = LaundryOrder(
    order_id="AO33396",
    customer="Suresh Babu",
    service="Saree",
    quantity=2,
    price_per_item=250.0
)

order_two.display()