from dataclasses import dataclass


@dataclass
class LaundryOrder:
    # Required fields: values must be provided when creating an object.
    order_id: str
    customer: str
    service: str
    quantity: int
    price_per_item: float

    # Default field: used when no status is provided.
    # Default fields must come after required fields.
    status: str = "Processing"

    def calculate_total(self) -> float:
        """Calculate and return the complete order amount."""

        # self means the current LaundryOrder object.
        return self.quantity * self.price_per_item

    def mark_ready(self) -> None:
        """Change the current order status to Ready."""

        self.status = "Ready"

    def display_summary(self) -> None:
        """Display the current order details."""

        print("=" * 40)
        print("KLYN LAUNDRY ORDER")
        print("=" * 40)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print("Price per item: ₹", self.price_per_item, sep="")
        print("Total amount: ₹", self.calculate_total(), sep="")
        print("Status:", self.status)


# No status is given, so Python uses the default: Processing.
order_one = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar",
    service="Shirt",
    quantity=3,
    price_per_item=85.0
)

# Here we override the default status with Ready.
order_two = LaundryOrder(
    order_id="AO33396",
    customer="Suresh Babu",
    service="Dry Cleaning",
    quantity=2,
    price_per_item=150.0,
    status="Ready"
)


print("\nFIRST ORDER")
order_one.display_summary()

print("\nSECOND ORDER")
order_two.display_summary()


# Change order_one from Processing to Ready using its method.
print("\nUPDATING FIRST ORDER")
order_one.mark_ready()

print(
    order_one.order_id,
    "updated status:",
    order_one.status
)