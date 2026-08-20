from dataclasses import dataclass, field, asdict, replace
from pathlib import Path
from typing import ClassVar
import json


# JSON file will be created beside this Python file.
JSON_FILE = Path(__file__).with_name("13.klyn_orders.json")


# ==================================================
# CUSTOMER DATACLASS
# ==================================================

@dataclass(slots=True)
class Customer:
    name: str
    phone: str
    city: str

    def __post_init__(self) -> None:
        # Remove unwanted spaces from customer data.
        self.name = self.name.strip()
        self.phone = self.phone.strip()
        self.city = self.city.strip()

        # Validate customer name.
        if not self.name:
            raise ValueError("Customer name cannot be empty")

        # Validate Indian mobile number.
        if not (
            len(self.phone) == 10
            and self.phone.isdigit()
            and self.phone[0] in "6789"
        ):
            raise ValueError("Invalid customer phone number")


# ==================================================
# GARMENT DATACLASS
# ==================================================

@dataclass(slots=True)
class GarmentItem:
    garment: str
    quantity: int
    price_per_item: float

    def __post_init__(self) -> None:
        self.garment = self.garment.strip().title()

        if not self.garment:
            raise ValueError("Garment name cannot be empty")

        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if self.price_per_item <= 0:
            raise ValueError("Price must be greater than zero")

    @property
    def total(self) -> float:
        # Calculate the amount for this garment.
        return self.quantity * self.price_per_item


# ==================================================
# PAYMENT DATACLASS
# ==================================================

@dataclass(slots=True)
class Payment:
    method: str = "Pending"
    status: str = "Unpaid"
    amount_paid: float = 0.0

    def __post_init__(self) -> None:
        self.method = self.method.strip().upper()
        self.status = self.status.strip().title()

        if self.amount_paid < 0:
            raise ValueError("Amount paid cannot be negative")


# ==================================================
# LAUNDRY ORDER DATACLASS
# ==================================================

@dataclass(slots=True)
class LaundryOrder:
    order_id: str
    customer: Customer

    # Each order receives its own independent list.
    items: list[GarmentItem] = field(default_factory=list)

    payment: Payment = field(default_factory=Payment)
    status: str = "Processing"
    express: bool = False

    # These fields are calculated automatically.
    subtotal: float = field(init=False)
    final_amount: float = field(init=False)

    # ClassVar belongs to the class, not individual objects.
    store_name: ClassVar[str] = "KLYN Laundry & Dry Cleaning"

    def __post_init__(self) -> None:
        self.order_id = self.order_id.strip().upper()
        self.status = self.status.strip().title()

        # Validate order ID: AO followed by five digits.
        if not (
            self.order_id.startswith("AO")
            and len(self.order_id) == 7
            and self.order_id[2:].isdigit()
        ):
            raise ValueError(
                "Order ID must contain AO followed by five digits"
            )

        valid_statuses = {
            "Processing",
            "Ready",
            "Delivered",
            "Cancelled"
        }

        if self.status not in valid_statuses:
            raise ValueError("Invalid order status")

        # Calculate the original bill.
        self.subtotal = sum(item.total for item in self.items)

        # Express orders cost twice the regular price.
        multiplier = 2 if self.express else 1
        self.final_amount = self.subtotal * multiplier

    @property
    def total_garments(self) -> int:
        # Count the total number of garments.
        return sum(item.quantity for item in self.items)

    @property
    def balance(self) -> float:
        # Do not allow a negative balance.
        return max(
            self.final_amount - self.payment.amount_paid,
            0.0
        )

    def display(self) -> None:
        print("=" * 50)
        print(self.store_name)
        print("=" * 50)

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
                f"× ₹{item.price_per_item} = ₹{item.total}"
            )

        print("\nTotal garments:", self.total_garments)
        print("Subtotal: ₹", self.subtotal, sep="")
        print("Final amount: ₹", self.final_amount, sep="")
        print("Amount paid: ₹", self.payment.amount_paid, sep="")
        print("Balance: ₹", self.balance, sep="")
        print("Payment status:", self.payment.status)


# ==================================================
# CREATE THE FIRST ORDER
# ==================================================

customer_one = Customer(
    name="  Ravi Kumar  ",
    phone="9876543210",
    city="Eluru"
)

order_one = LaundryOrder(
    order_id="AO45821",
    customer=customer_one,
    items=[
        GarmentItem(
            garment="shirt",
            quantity=3,
            price_per_item=85.0
        ),
        GarmentItem(
            garment="trouser",
            quantity=2,
            price_per_item=150.0
        )
    ],
    payment=Payment(
        method="UPI",
        status="Paid",
        amount_paid=555.0
    ),
    status="Ready"
)


# ==================================================
# CREATE AN EXPRESS ORDER
# ==================================================

customer_two = Customer(
    name="Suresh Babu",
    phone="8765432109",
    city="Vijayawada"
)

order_two = LaundryOrder(
    order_id="AO33396",
    customer=customer_two,
    items=[
        GarmentItem(
            garment="saree",
            quantity=2,
            price_per_item=250.0
        )
    ],
    status="Processing",
    express=True
)


orders = [order_one, order_two]


# ==================================================
# DISPLAY THE ORDERS
# ==================================================

for order in orders:
    order.display()
    print()


# ==================================================
# CREATE AN UPDATED COPY
# ==================================================

# replace() creates a new object without modifying order_two.
ready_order = replace(
    order_two,
    status="Ready"
)

print("\nUPDATED COPY")
ready_order.display()

print(
    "\nOriginal second-order status:",
    order_two.status
)

print(
    "Updated-copy status:",
    ready_order.status
)


# ==================================================
# SAVE ORDERS AS JSON
# ==================================================

# asdict() recursively converts nested dataclasses.
orders_as_dictionaries = [
    asdict(order)
    for order in orders
]

with open(
    JSON_FILE,
    "w",
    encoding="utf-8"
) as json_file:
    json.dump(
        orders_as_dictionaries,
        json_file,
        indent=4,
        ensure_ascii=False
    )

print("\nJSON file saved:", JSON_FILE.name)


# ==================================================
# READ THE JSON FILE
# ==================================================

with open(
    JSON_FILE,
    "r",
    encoding="utf-8"
) as json_file:
    loaded_orders = json.load(json_file)

print("\nORDERS LOADED FROM JSON")

for order_data in loaded_orders:
    print(
        order_data["order_id"],
        "|",
        order_data["customer"]["name"],
        "| ₹",
        order_data["final_amount"],
        sep=""
    )


print("\nKLYN DATACLASS PROJECT COMPLETED")