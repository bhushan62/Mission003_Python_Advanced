"""
DATACLASSES FINAL TEST
KLYN Laundry & Dry Cleaning

Concepts covered:
1. Basic dataclasses
2. Default values
3. Methods and properties
4. field() and default_factory
5. __post_init__ validation
6. Frozen dataclasses
7. Ordering dataclasses
8. Inheritance
9. asdict(), astuple(), replace()
10. slots=True and kw_only=True
11. InitVar, ClassVar and metadata
12. Nested dataclasses
13. JSON serialization and deserialization
"""

import json

from dataclasses import (
    InitVar,
    asdict,
    astuple,
    dataclass,
    field,
    fields,
    replace,
)
from pathlib import Path
from typing import ClassVar


# Save the JSON file beside this Python file.
JSON_FILE = Path(__file__).with_name(
    "14.klyn_dataclasses_final_test.json"
)


def heading(title: str) -> None:
    """Print a formatted heading."""

    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


# ==========================================================
# 1. FROZEN DATACLASS
# ==========================================================

@dataclass(frozen=True, slots=True)
class ServiceRate:
    """
    A frozen dataclass cannot be modified after creation.

    This is useful for service prices because an accidental
    price change should not be allowed.
    """

    service: str
    regular_price: float

    @property
    def express_price(self) -> float:
        """Express service costs twice the regular price."""

        return self.regular_price * 2


# ==========================================================
# 2. CUSTOMER DATACLASS
# ==========================================================

@dataclass(slots=True, kw_only=True)
class Customer:
    """
    slots=True:
        Prevents unknown attributes from being added.

    kw_only=True:
        Values must be provided using field names.
    """

    name: str
    phone: str
    city: str = "Eluru"

    def __post_init__(self) -> None:
        """Validate and clean customer information."""

        # Remove unwanted spaces from the customer name.
        self.name = " ".join(self.name.split())

        # Keep only digits in the phone number.
        self.phone = "".join(
            character
            for character in self.phone
            if character.isdigit()
        )

        # Remove the Indian country code when present.
        if len(self.phone) == 12 and self.phone.startswith("91"):
            self.phone = self.phone[2:]

        if not self.name:
            raise ValueError("Customer name cannot be empty")

        if len(self.phone) != 10:
            raise ValueError(
                "Phone number must contain exactly 10 digits"
            )

        if self.phone[0] not in "6789":
            raise ValueError(
                "Indian mobile number must begin with 6, 7, 8 or 9"
            )


# ==========================================================
# 3. GARMENT ITEM DATACLASS
# ==========================================================

@dataclass(slots=True, kw_only=True)
class GarmentItem:
    """Represent one garment type in an order."""

    garment: str = field(
        metadata={
            "label": "Garment Name",
            "required": True,
        }
    )

    quantity: int = field(
        metadata={
            "label": "Quantity",
            "minimum": 1,
        }
    )

    price_per_item: float = field(
        metadata={
            "label": "Price Per Item",
            "currency": "INR",
        }
    )

    def __post_init__(self) -> None:
        """Validate garment information."""

        self.garment = self.garment.strip().title()

        if not self.garment:
            raise ValueError("Garment name cannot be empty")

        if self.quantity <= 0:
            raise ValueError(
                "Garment quantity must be greater than zero"
            )

        if self.price_per_item <= 0:
            raise ValueError(
                "Garment price must be greater than zero"
            )

    @property
    def total(self) -> float:
        """Calculate the total price of this garment item."""

        return self.quantity * self.price_per_item


# ==========================================================
# 4. PAYMENT DATACLASS
# ==========================================================

@dataclass(slots=True, kw_only=True)
class Payment:
    """Store payment information."""

    method: str = "Pending"
    amount_paid: float = 0.0

    def __post_init__(self) -> None:
        """Validate payment amount."""

        self.method = self.method.strip().title()

        if self.amount_paid < 0:
            raise ValueError(
                "Amount paid cannot be negative"
            )


# ==========================================================
# 5. MAIN LAUNDRY ORDER DATACLASS
# ==========================================================

@dataclass(slots=True, kw_only=True)
class LaundryOrder:
    """Represent a complete KLYN laundry order."""

    # ClassVar belongs to the class, not each individual object.
    store_name: ClassVar[str] = (
        "KLYN Laundry & Dry Cleaning"
    )

    order_id: str = field(
        metadata={
            "label": "Order ID",
            "required": True,
        }
    )

    customer: Customer

    # default_factory creates a separate list for every order.
    items: list[GarmentItem] = field(
        default_factory=list
    )

    payment: Payment = field(
        default_factory=Payment
    )

    status: str = "Processing"
    express: bool = False

    # InitVar is accepted by __init__ but is not stored as a field.
    discount_percentage: InitVar[float] = 0.0

    # These fields are calculated after object creation.
    subtotal: float = field(
        init=False,
        default=0.0
    )

    discount_amount: float = field(
        init=False,
        default=0.0
    )

    final_amount: float = field(
        init=False,
        default=0.0
    )

    balance: float = field(
        init=False,
        default=0.0
    )

    def __post_init__(
        self,
        discount_percentage: float,
    ) -> None:
        """Validate the order and calculate its bill."""

        self.order_id = self.order_id.strip().upper()
        self.status = self.status.strip().title()

        if (
            not self.order_id.startswith("AO")
            or len(self.order_id) != 7
            or not self.order_id[2:].isdigit()
        ):
            raise ValueError(
                "Order ID must use the format AO12345"
            )

        valid_statuses = {
            "Processing",
            "Ready",
            "Delivered",
            "Cancelled",
        }

        if self.status not in valid_statuses:
            raise ValueError(
                f"Invalid order status: {self.status}"
            )

        if not self.items:
            raise ValueError(
                "An order must contain at least one garment"
            )

        if not 0 <= discount_percentage <= 100:
            raise ValueError(
                "Discount must be between 0 and 100"
            )

        # Add the total of every garment.
        self.subtotal = sum(
            item.total
            for item in self.items
        )

        # Express service costs twice the regular amount.
        if self.express:
            self.subtotal *= 2

        self.discount_amount = (
            self.subtotal
            * discount_percentage
            / 100
        )

        self.final_amount = (
            self.subtotal
            - self.discount_amount
        )

        self.balance = max(
            self.final_amount
            - self.payment.amount_paid,
            0.0,
        )

    @property
    def total_garments(self) -> int:
        """Return the total number of garments."""

        return sum(
            item.quantity
            for item in self.items
        )

    @property
    def payment_status(self) -> str:
        """Determine the payment status."""

        if self.payment.amount_paid <= 0:
            return "Unpaid"

        if self.payment.amount_paid < self.final_amount:
            return "Partially Paid"

        return "Paid"

    def update_status(self, new_status: str) -> None:
        """Safely update the order status."""

        valid_statuses = {
            "Processing",
            "Ready",
            "Delivered",
            "Cancelled",
        }

        cleaned_status = new_status.strip().title()

        if cleaned_status not in valid_statuses:
            raise ValueError(
                f"Invalid order status: {new_status}"
            )

        self.status = cleaned_status

    def display(self) -> None:
        """Display the complete order."""

        heading("KLYN LAUNDRY ORDER")

        print("Order ID:", self.order_id)
        print("Customer:", self.customer.name)
        print("Phone:", self.customer.phone)
        print("City:", self.customer.city)
        print("Status:", self.status)
        print("Express:", self.express)

        print("\nGARMENTS")

        for item in self.items:
            print(
                f"- {item.quantity} {item.garment} "
                f"× ₹{item.price_per_item} "
                f"= ₹{item.total}"
            )

        print("\nTotal garments:", self.total_garments)
        print("Subtotal: ₹", self.subtotal, sep="")
        print(
            "Discount: ₹",
            self.discount_amount,
            sep="",
        )
        print(
            "Final amount: ₹",
            self.final_amount,
            sep="",
        )
        print(
            "Amount paid: ₹",
            self.payment.amount_paid,
            sep="",
        )
        print("Balance: ₹", self.balance, sep="")
        print("Payment status:", self.payment_status)


# ==========================================================
# 6. DATACLASS INHERITANCE
# ==========================================================

@dataclass(slots=True, kw_only=True)
class PickupLaundryOrder(LaundryOrder):
    """Laundry order containing pickup information."""

    pickup_address: str = ""
    pickup_agent: str = "Not assigned"

    def display_pickup(self) -> None:
        """Display pickup information."""

        print("\nPICKUP DETAILS")
        print("Address:", self.pickup_address)
        print("Agent:", self.pickup_agent)


# ==========================================================
# 7. ORDERING DATACLASS
# ==========================================================

@dataclass(
    order=True,
    frozen=True,
    slots=True,
)
class OrderValue:
    """
    Objects are compared using amount.

    compare=False prevents order_id from affecting sorting.
    """

    amount: float
    order_id: str = field(compare=False)


# ==========================================================
# 8. JSON RECONSTRUCTION FUNCTIONS
# ==========================================================

def order_from_dictionary(
    order_data: dict,
) -> LaundryOrder:
    """Recreate nested dataclasses from a dictionary."""

    customer = Customer(
        **order_data["customer"]
    )

    items = [
        GarmentItem(**item_data)
        for item_data in order_data["items"]
    ]

    payment = Payment(
        **order_data["payment"]
    )

    # Calculated fields are not passed into __init__.
    return LaundryOrder(
        order_id=order_data["order_id"],
        customer=customer,
        items=items,
        payment=payment,
        status=order_data["status"],
        express=order_data["express"],
    )


# ==========================================================
# 9. CREATE SERVICE RATES
# ==========================================================

heading("FROZEN SERVICE RATES")

shirt_rate = ServiceRate(
    service="Shirt",
    regular_price=85.0,
)

saree_rate = ServiceRate(
    service="Saree",
    regular_price=250.0,
)

print(shirt_rate)
print("Express shirt price: ₹", shirt_rate.express_price, sep="")
print(saree_rate)
print("Express saree price: ₹", saree_rate.express_price, sep="")


# Demonstrate that a frozen dataclass cannot be modified.
try:
    shirt_rate.regular_price = 100.0
except Exception as error:
    print("\nFrozen price modification rejected")
    print("Reason:", error)


# ==========================================================
# 10. CREATE VALID ORDERS
# ==========================================================

customer_one = Customer(
    name="   Ravi     Kumar   ",
    phone="+91-98765 43210",
    city="Eluru",
)

order_one = LaundryOrder(
    order_id="AO45821",
    customer=customer_one,
    items=[
        GarmentItem(
            garment="shirt",
            quantity=3,
            price_per_item=85.0,
        ),
        GarmentItem(
            garment="trouser",
            quantity=2,
            price_per_item=150.0,
        ),
    ],
    payment=Payment(
        method="UPI",
        amount_paid=555.0,
    ),
    status="Ready",
    discount_percentage=0,
)

order_one.display()


# Create an express pickup order through inheritance.
customer_two = Customer(
    name="Suresh Babu",
    phone="8765432109",
    city="Vijayawada",
)

order_two = PickupLaundryOrder(
    order_id="AO33396",
    customer=customer_two,
    items=[
        GarmentItem(
            garment="saree",
            quantity=2,
            price_per_item=250.0,
        ),
    ],
    payment=Payment(),
    status="Processing",
    express=True,
    discount_percentage=0,
    pickup_address="Benz Circle, Vijayawada",
    pickup_agent="Kiran",
)

order_two.display()
order_two.display_pickup()


# ==========================================================
# 11. ASDICT, ASTUPLE AND REPLACE
# ==========================================================

heading("ASDICT")

order_dictionary = asdict(order_one)
print(order_dictionary)


heading("ASTUPLE")

order_tuple = astuple(order_one)
print(order_tuple)


heading("REPLACE")

# replace() creates a new object instead of editing the original.
ready_order_copy = replace(
    order_two,
    status="Ready",
)

print(
    "Original order status:",
    order_two.status,
)

print(
    "Copied order status:",
    ready_order_copy.status,
)

print(
    "Are they the same object?",
    order_two is ready_order_copy,
)


# ==========================================================
# 12. STORED FIELDS, INITVAR AND CLASSVAR
# ==========================================================

heading("DATACLASS FIELDS")

stored_fields = [
    item.name
    for item in fields(order_one)
]

for stored_field in stored_fields:
    print("-", stored_field)

print(
    "\nIs discount_percentage stored?",
    "discount_percentage" in stored_fields,
)

print(
    "Is store_name stored?",
    "store_name" in stored_fields,
)


# Display field metadata.
heading("FIELD METADATA")

for dataclass_field in fields(GarmentItem):
    print(
        dataclass_field.name,
        "→",
        dict(dataclass_field.metadata),
    )


# ==========================================================
# 13. SLOTS TEST
# ==========================================================

heading("SLOTS TEST")

try:
    order_one.delivery_agent = "Ramesh"
except AttributeError as error:
    print("Unknown attribute rejected")
    print("Reason:", error)


# ==========================================================
# 14. ORDERING TEST
# ==========================================================

heading("ORDER VALUE SORTING")

order_values = [
    OrderValue(
        amount=order_one.final_amount,
        order_id=order_one.order_id,
    ),
    OrderValue(
        amount=order_two.final_amount,
        order_id=order_two.order_id,
    ),
    OrderValue(
        amount=750.0,
        order_id="AO98765",
    ),
]

for order_value in sorted(order_values):
    print(
        order_value.order_id,
        "₹",
        order_value.amount,
    )

print(
    "\nCheapest order:",
    min(order_values).order_id,
)

print(
    "Highest-value order:",
    max(order_values).order_id,
)


# ==========================================================
# 15. VALIDATION TEST
# ==========================================================

heading("INVALID ORDER TEST")

try:
    invalid_order = LaundryOrder(
        order_id="BO12345",
        customer=Customer(
            name="Anjali",
            phone="9876543210",
        ),
        items=[
            GarmentItem(
                garment="Shirt",
                quantity=1,
                price_per_item=85.0,
            )
        ],
    )

except ValueError as error:
    print("Order rejected")
    print("Reason:", error)


# ==========================================================
# 16. JSON SERIALIZATION
# ==========================================================

heading("JSON SERIALIZATION")

orders_to_save = [
    asdict(order_one),
    asdict(order_two),
]

with open(
    JSON_FILE,
    "w",
    encoding="utf-8",
) as json_file:
    json.dump(
        orders_to_save,
        json_file,
        indent=4,
        ensure_ascii=False,
    )

print("JSON saved:", JSON_FILE.name)


# Read the JSON file.
with open(
    JSON_FILE,
    "r",
    encoding="utf-8",
) as json_file:
    loaded_order_dictionaries = json.load(json_file)


# Convert every dictionary back into a LaundryOrder.
loaded_orders = [
    order_from_dictionary(order_data)
    for order_data in loaded_order_dictionaries
]


heading("ORDERS LOADED FROM JSON")

for loaded_order in loaded_orders:
    print(
        loaded_order.order_id,
        "|",
        loaded_order.customer.name,
        "| ₹",
        loaded_order.final_amount,
        sep="",
    )


# Dataclasses compare their field values automatically.
heading("OBJECT COMPARISON")

print(
    "Original order equals loaded order:",
    order_one == loaded_orders[0],
)

print(
    "Are they the same object in memory?",
    order_one is loaded_orders[0],
)


# ==========================================================
# FINAL RESULT
# ==========================================================

heading("DATACLASSES FINAL TEST COMPLETED")

concepts = [
    "Basic dataclasses",
    "Default values",
    "Methods and properties",
    "field() and default_factory",
    "__post_init__ validation",
    "Frozen dataclasses",
    "Ordering",
    "Inheritance",
    "asdict(), astuple() and replace()",
    "slots=True and kw_only=True",
    "InitVar, ClassVar and metadata",
    "Nested dataclasses",
    "JSON serialization",
]

for number, concept in enumerate(
    concepts,
    start=1,
):
    print(f"{number}. {concept}")