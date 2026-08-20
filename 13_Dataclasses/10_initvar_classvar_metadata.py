from dataclasses import dataclass, field, fields, InitVar
from typing import ClassVar


@dataclass
class LaundryOrder:
    # ClassVar belongs to the class, not to each order object.
    store_name: ClassVar[str] = "KLYN Laundry & Dry Cleaning"
    tax_percentage: ClassVar[float] = 5.0

    # Normal stored dataclass fields.
    order_id: str = field(
        metadata={
            "label": "Order ID",
            "required": True
        }
    )

    customer: str = field(
        metadata={
            "label": "Customer Name",
            "required": True
        }
    )

    service: str = field(
        metadata={
            "label": "Laundry Service",
            "required": True
        }
    )

    quantity: int = field(
        metadata={
            "label": "Quantity",
            "minimum": 1
        }
    )

    price_per_item: float = field(
        metadata={
            "label": "Price Per Item",
            "currency": "INR"
        }
    )

    status: str = field(
        default="Processing",
        metadata={
            "label": "Order Status"
        }
    )

    # InitVar is accepted during object creation,
    # but it is not stored as a regular dataclass field.
    discount_percentage: InitVar[float] = 0.0

    # These fields are calculated automatically.
    # The user cannot provide them while creating the object.
    subtotal: float = field(init=False)
    discount_amount: float = field(init=False)
    tax_amount: float = field(init=False)
    final_amount: float = field(init=False)

    def __post_init__(self, discount_percentage: float) -> None:
        """Validate the order and calculate its final amount."""

        # Validate order ID.
        if not self.order_id.startswith("AO"):
            raise ValueError("Order ID must begin with AO")

        # Validate customer name.
        if not self.customer.strip():
            raise ValueError("Customer name cannot be empty")

        # Validate quantity.
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        # Validate price.
        if self.price_per_item <= 0:
            raise ValueError("Price must be greater than zero")

        # Validate discount.
        if not 0 <= discount_percentage <= 100:
            raise ValueError(
                "Discount percentage must be between 0 and 100"
            )

        # Calculate the bill.
        self.subtotal = self.quantity * self.price_per_item

        self.discount_amount = (
            self.subtotal * discount_percentage / 100
        )

        amount_after_discount = (
            self.subtotal - self.discount_amount
        )

        self.tax_amount = (
            amount_after_discount * self.tax_percentage / 100
        )

        self.final_amount = round(
            amount_after_discount + self.tax_amount,
            2
        )

    def display(self) -> None:
        """Display the complete laundry order."""

        print("=" * 45)
        print(self.store_name)
        print("=" * 45)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print("Price per item: ₹", self.price_per_item, sep="")
        print("Status:", self.status)
        print("Subtotal: ₹", self.subtotal, sep="")
        print("Discount: ₹", self.discount_amount, sep="")
        print("Tax: ₹", self.tax_amount, sep="")
        print("Final amount: ₹", self.final_amount, sep="")


# Create the object before using fields(order_one).
order_one = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar",
    service="Shirt",
    quantity=3,
    price_per_item=85.0,
    status="Ready",
    discount_percentage=10
)

order_one.display()


# fields() returns the fields actually stored in the object.
stored_fields = [
    item.name
    for item in fields(order_one)
]

print("\nSTORED DATACLASS FIELDS")
print("=" * 45)

for field_name in stored_fields:
    print("-", field_name)


# discount_percentage is an InitVar.
# It is used by __post_init__(), but it is not stored.
print(
    "\nIs discount_percentage stored?",
    "discount_percentage" in stored_fields
)
# Expected: False


# ClassVar fields are also not stored inside each object.
print(
    "Is store_name stored?",
    "store_name" in stored_fields
)
# Expected: False


print("\nFIELD METADATA")
print("=" * 45)

for item in fields(order_one):
    print(
        item.name,
        "→",
        dict(item.metadata)
    )


print("\nPROGRAM COMPLETED")