from dataclasses import asdict, dataclass, field


# ==================================================
# CUSTOMER DATACLASS
# Stores customer-related information.
# ==================================================

@dataclass(slots=True, kw_only=True)
class Customer:
    name: str
    phone: str
    city: str

    def __post_init__(self) -> None:
        # Remove unnecessary spaces from customer data.
        self.name = self.name.strip()
        self.phone = self.phone.strip()
        self.city = self.city.strip()

        # Customer name must not be empty.
        if not self.name:
            raise ValueError("Customer name cannot be empty")

        # Validate an Indian 10-digit mobile number.
        if (
            len(self.phone) != 10
            or not self.phone.isdigit()
            or self.phone[0] not in "6789"
        ):
            raise ValueError("Invalid customer phone number")


# ==================================================
# GARMENT ITEM DATACLASS
# Represents one garment/service inside an order.
# ==================================================

@dataclass(slots=True, kw_only=True)
class GarmentItem:
    garment: str
    quantity: int
    price_per_item: float

    def __post_init__(self) -> None:
        # Clean the garment name.
        self.garment = self.garment.strip().title()

        # Validate garment details.
        if not self.garment:
            raise ValueError("Garment name cannot be empty")

        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if self.price_per_item <= 0:
            raise ValueError("Price must be greater than zero")

    @property
    def total(self) -> float:
        # Calculate the total price for this garment.
        return self.quantity * self.price_per_item


# ==================================================
# PAYMENT DATACLASS
# Stores payment information for an order.
# ==================================================

@dataclass(slots=True, kw_only=True)
class Payment:
    method: str = "Cash"
    status: str = "Pending"
    amount_paid: float = 0.0

    def mark_as_paid(self, amount: float) -> None:
        # Update the payment after receiving money.
        self.amount_paid = amount
        self.status = "Paid"


# ==================================================
# LAUNDRY ORDER DATACLASS
#
# This is a nested dataclass because it contains:
#   1. A Customer object
#   2. A list of GarmentItem objects
#   3. A Payment object
# ==================================================

@dataclass(slots=True, kw_only=True)
class LaundryOrder:
    order_id: str
    customer: Customer

    # Every order receives its own separate item list.
    items: list[GarmentItem] = field(default_factory=list)

    # Every order receives its own Payment object.
    payment: Payment = field(default_factory=Payment)

    status: str = "Processing"

    def __post_init__(self) -> None:
        # Validate the order ID.
        if (
            not self.order_id.startswith("AO")
            or len(self.order_id) != 7
            or not self.order_id[2:].isdigit()
        ):
            raise ValueError("Order ID must use the format AO12345")

        # An order must contain at least one garment.
        if not self.items:
            raise ValueError("The order must contain at least one garment")

    @property
    def total_quantity(self) -> int:
        # Add the quantities of all garment items.
        return sum(item.quantity for item in self.items)

    @property
    def bill_amount(self) -> float:
        # Add the total prices of all garment items.
        return sum(item.total for item in self.items)

    def display(self) -> None:
        # Display complete nested order information.
        print("=" * 45)
        print("KLYN LAUNDRY ORDER")
        print("=" * 45)

        print("Order ID:", self.order_id)
        print("Customer:", self.customer.name)
        print("Phone:", self.customer.phone)
        print("City:", self.customer.city)
        print("Status:", self.status)

        print("\nGARMENTS")

        for item in self.items:
            print(
                f"- {item.quantity} {item.garment} "
                f"× ₹{item.price_per_item} = ₹{item.total}"
            )

        print("\nTotal garments:", self.total_quantity)
        print("Bill amount: ₹", self.bill_amount, sep="")
        print("Payment method:", self.payment.method)
        print("Payment status:", self.payment.status)
        print("Amount paid: ₹", self.payment.amount_paid, sep="")


# ==================================================
# CREATE THE NESTED OBJECTS
# ==================================================

customer = Customer(
    name="Ravi Kumar",
    phone="9876543210",
    city="Eluru"
)

shirt = GarmentItem(
    garment="shirt",
    quantity=3,
    price_per_item=85.0
)

trouser = GarmentItem(
    garment="trouser",
    quantity=2,
    price_per_item=150.0
)

payment = Payment(
    method="UPI"
)

order = LaundryOrder(
    order_id="AO45821",
    customer=customer,
    items=[shirt, trouser],
    payment=payment
)


# ==================================================
# DISPLAY THE INITIAL ORDER
# ==================================================

print("\nINITIAL ORDER")

order.display()


# ==================================================
# ACCESS NESTED VALUES
# Use dots to move from one object into another.
# ==================================================

print("\nACCESSING NESTED VALUES")
print("=" * 45)

print("Customer name:", order.customer.name)
print("Customer city:", order.customer.city)
print("First garment:", order.items[0].garment)
print("First garment total: ₹", order.items[0].total, sep="")
print("Payment method:", order.payment.method)


# ==================================================
# UPDATE NESTED OBJECTS
# ==================================================

# Update the order status.
order.status = "Ready"

# Mark the nested payment object as paid.
order.payment.mark_as_paid(order.bill_amount)

print("\nUPDATED ORDER")

order.display()


# ==================================================
# CONVERT THE COMPLETE NESTED ORDER TO A DICTIONARY
#
# asdict() recursively converts:
# LaundryOrder -> Customer -> GarmentItem -> Payment
# ==================================================

order_dictionary = asdict(order)

print("\nNESTED DICTIONARY")
print("=" * 45)

print(order_dictionary)

print("\nCustomer dictionary:")
print(order_dictionary["customer"])

print("\nGarment dictionaries:")

for garment in order_dictionary["items"]:
    print(garment)

print("\nNESTED DATACLASSES COMPLETED")