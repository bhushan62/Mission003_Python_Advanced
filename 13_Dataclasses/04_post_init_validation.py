from dataclasses import dataclass, field


@dataclass
class LaundryOrder:
    # Required fields
    order_id: str
    customer: str
    service: str
    quantity: int
    price_per_item: float

    # Default field
    status: str = "Processing"

    # This field is calculated automatically.
    # init=False means we do not provide it while creating the object.
    total_amount: float = field(init=False)

    def __post_init__(self) -> None:
        """
        Runs automatically after the dataclass creates the object.

        It cleans the provided values, validates them,
        and calculates the final amount.
        """

        # Remove unnecessary spaces.
        self.order_id = self.order_id.strip().upper()
        self.customer = self.customer.strip().title()
        self.service = self.service.strip().title()
        self.status = self.status.strip().title()

        # Validate the order ID.
        if not self.order_id.startswith("AO"):
            raise ValueError("Order ID must begin with AO")

        if len(self.order_id) != 7:
            raise ValueError(
                "Order ID must contain AO followed by 5 digits"
            )

        if not self.order_id[2:].isdigit():
            raise ValueError(
                "Characters after AO must be digits"
            )

        # Validate the customer's name.
        if not self.customer:
            raise ValueError("Customer name cannot be empty")

        # Validate quantity and price.
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if self.price_per_item <= 0:
            raise ValueError("Price must be greater than zero")

        # Calculate and store the total automatically.
        self.total_amount = (
            self.quantity * self.price_per_item
        )

    def display(self) -> None:
        """Display the processed laundry order."""

        print("=" * 40)
        print("KLYN LAUNDRY ORDER")
        print("=" * 40)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print("Price per item: ₹", self.price_per_item, sep="")
        print("Total amount: ₹", self.total_amount, sep="")
        print("Status:", self.status)


print("VALID ORDER")

valid_order = LaundryOrder(
    order_id="  ao45821  ",
    customer="  ravi kumar  ",
    service="shirt",
    quantity=3,
    price_per_item=85.0
)

valid_order.display()


print("\nINVALID ORDER")

try:
    invalid_order = LaundryOrder(
        order_id="BO33396",       # Invalid prefix
        customer="Suresh Babu",
        service="Dry Cleaning",
        quantity=2,
        price_per_item=150.0
    )

    invalid_order.display()

except ValueError as error:
    print("=" * 40)
    print("ORDER REJECTED")
    print("=" * 40)
    print("Reason:", error)


print("\nINVALID QUANTITY")

try:
    quantity_error_order = LaundryOrder(
        order_id="AO98765",
        customer="Anjali Devi",
        service="Saree",
        quantity=0,               # Invalid quantity
        price_per_item=250.0
    )

except ValueError as error:
    print("=" * 40)
    print("ORDER REJECTED")
    print("=" * 40)
    print("Reason:", error)
    