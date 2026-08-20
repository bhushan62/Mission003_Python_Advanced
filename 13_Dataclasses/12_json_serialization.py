# Import tools for creating dataclasses.
from dataclasses import asdict, dataclass, field

# json converts Python data into JSON and JSON back into Python data.
import json

# Path helps us create the JSON file beside this Python file.

from pathlib import Path


# The JSON file will be created inside the current Dataclasses folder.

JSON_FILE = Path(__file__).with_name("12.klyn_order.json")


# ==================================================
# CUSTOMER DATACLASS
# ==================================================

@dataclass(slots=True, kw_only=True)
class Customer:
    """Store customer information."""

    name: str
    phone: str
    city: str


# ==================================================
# GARMENT DATACLASS
# ==================================================

@dataclass(slots=True, kw_only=True)
class GarmentItem:
    """Store one garment and its price information."""

    garment: str
    quantity: int
    price_per_item: float

    @property
    def total_amount(self) -> float:
        """Calculate the total price for this garment."""

        return self.quantity * self.price_per_item


# ==================================================
# PAYMENT DATACLASS
# ==================================================

@dataclass(slots=True, kw_only=True)
class Payment:
    """Store payment information."""

    method: str
    status: str
    amount_paid: float = 0.0


# ==================================================
# LAUNDRY ORDER DATACLASS
# ==================================================

@dataclass(slots=True, kw_only=True)
class LaundryOrder:
    """Store one complete laundry order."""

    order_id: str

    # Customer is another dataclass stored inside LaundryOrder.
    customer: Customer

    # Each order gets its own separate garment list.
    items: list[GarmentItem] = field(default_factory=list)

    # Payment is also a nested dataclass.
    payment: Payment

    status: str = "Processing"

    @property
    def total_garments(self) -> int:
        """Calculate the total quantity of all garments."""

        return sum(item.quantity for item in self.items)

    @property
    def bill_amount(self) -> float:
        """Calculate the total bill for all garments."""

        return sum(item.total_amount for item in self.items)


# ==================================================
# DISPLAY FUNCTION
# ==================================================

def display_order(order: LaundryOrder) -> None:
    """Display a complete laundry order."""

    print("=" * 50)
    print("KLYN LAUNDRY ORDER")
    print("=" * 50)

    print("Order ID:", order.order_id)
    print("Customer:", order.customer.name)
    print("Phone:", order.customer.phone)
    print("City:", order.customer.city)
    print("Status:", order.status)

    print("\nGARMENTS")

    for item in order.items:
        print(
            f"- {item.quantity} {item.garment} "
            f"× ₹{item.price_per_item} "
            f"= ₹{item.total_amount}"
        )

    print("\nTotal garments:", order.total_garments)
    print("Bill amount: ₹", order.bill_amount, sep="")
    print("Payment method:", order.payment.method)
    print("Payment status:", order.payment.status)
    print("Amount paid: ₹", order.payment.amount_paid, sep="")


# ==================================================
# DESERIALIZATION FUNCTION
# ==================================================

def create_order_from_dictionary(data: dict) -> LaundryOrder:
    """
    Convert a normal dictionary back into nested dataclass objects.

    JSON loading gives dictionaries and lists.
    Therefore, we must manually rebuild each dataclass.
    """

    # Convert the customer dictionary into a Customer object.
    customer = Customer(
        name=data["customer"]["name"],
        phone=data["customer"]["phone"],
        city=data["customer"]["city"]
    )

    # Convert every garment dictionary into a GarmentItem object.
    garments = [
        GarmentItem(
            garment=item["garment"],
            quantity=item["quantity"],
            price_per_item=item["price_per_item"]
        )
        for item in data["items"]
    ]

    # Convert the payment dictionary into a Payment object.
    payment = Payment(
        method=data["payment"]["method"],
        status=data["payment"]["status"],
        amount_paid=data["payment"]["amount_paid"]
    )

    # Build and return the complete LaundryOrder object.
    return LaundryOrder(
        order_id=data["order_id"],
        customer=customer,
        items=garments,
        payment=payment,
        status=data["status"]
    )


# ==================================================
# CREATE AN ORDER
# ==================================================

original_order = LaundryOrder(
    order_id="AO45821",

    customer=Customer(
        name="Ravi Kumar",
        phone="9876543210",
        city="Eluru"
    ),

    items=[
        GarmentItem(
            garment="Shirt",
            quantity=3,
            price_per_item=85.0
        ),
        GarmentItem(
            garment="Trouser",
            quantity=2,
            price_per_item=150.0
        ),
        GarmentItem(
            garment="Saree",
            quantity=1,
            price_per_item=250.0
        )
    ],

    payment=Payment(
        method="UPI",
        status="Paid",
        amount_paid=805.0
    ),

    status="Ready"
)


# ==================================================
# DISPLAY ORIGINAL ORDER
# ==================================================

print("\nORIGINAL DATACLASS OBJECT")
display_order(original_order)


# ==================================================
# SERIALIZATION: DATACLASS → DICTIONARY → JSON
# ==================================================

# asdict() recursively converts all nested dataclasses to dictionaries.
order_dictionary = asdict(original_order)

# json.dumps() converts the dictionary into formatted JSON text.
json_text = json.dumps(
    order_dictionary,
    indent=4,
    ensure_ascii=False
)

print("\nJSON TEXT")
print("=" * 50)
print(json_text)


# ==================================================
# SAVE JSON INTO A FILE
# ==================================================

# Write the JSON text into a UTF-8 file.
JSON_FILE.write_text(
    json_text,
    encoding="utf-8"
)

print("\nJSON FILE SAVED")
print("=" * 50)
print("File:", JSON_FILE.name)


# ==================================================
# READ JSON FROM THE FILE
# ==================================================

# Read JSON text from the file.
saved_json_text = JSON_FILE.read_text(
    encoding="utf-8"
)

# json.loads() converts JSON text back into Python dictionaries and lists.
loaded_dictionary = json.loads(saved_json_text)

print("\nLOADED DICTIONARY")
print("=" * 50)
print(loaded_dictionary)


# ==================================================
# DESERIALIZATION: DICTIONARY → DATACLASS
# ==================================================

loaded_order = create_order_from_dictionary(
    loaded_dictionary
)

print("\nRECREATED DATACLASS OBJECT")
display_order(loaded_order)


# ==================================================
# COMPARE BOTH OBJECTS
# ==================================================

# Dataclasses compare their field values automatically.
print("\nOBJECT COMPARISON")
print("=" * 50)
print(
    "Original order equals loaded order:",
    original_order == loaded_order
)

print(
    "Are they the same object in memory?",
    original_order is loaded_order
)


print("\nJSON SERIALIZATION COMPLETED")