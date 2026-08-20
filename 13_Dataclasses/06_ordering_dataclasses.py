from dataclasses import dataclass, field


# order=True creates comparison methods automatically.
# It allows objects to be sorted using sorted().
@dataclass(order=True)
class LaundryOrder:
    # This field is checked first while comparing objects.
    # It is calculated automatically, so the user cannot provide it.
    sort_index: float = field(
        init=False,
        repr=False
    )

    order_id: str
    customer: str
    service: str
    quantity: int
    price_per_item: float
    status: str = "Processing"

    def __post_init__(self) -> None:
        # Validate quantity.
        if self.quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero"
            )

        # Validate price.
        if self.price_per_item <= 0:
            raise ValueError(
                "Price must be greater than zero"
            )

        # Calculate the value used for sorting.
        self.sort_index = self.total_amount

    @property
    def total_amount(self) -> float:
        # Calculate the complete order amount.
        return self.quantity * self.price_per_item

    def display(self) -> None:
        # Display the order details.
        print("=" * 45)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print(
            "Total amount: ₹",
            self.total_amount,
            sep=""
        )


# Create orders with different total amounts.
orders = [
    LaundryOrder(
        order_id="AO45821",
        customer="Ravi Kumar",
        service="Shirt",
        quantity=3,
        price_per_item=85.0
    ),
    LaundryOrder(
        order_id="AO33396",
        customer="Suresh Babu",
        service="Dry Cleaning",
        quantity=2,
        price_per_item=150.0
    ),
    LaundryOrder(
        order_id="AO98765",
        customer="Anjali Devi",
        service="Saree",
        quantity=3,
        price_per_item=250.0
    )
]


print("ORIGINAL ORDER LIST")
print("=" * 45)

for order in orders:
    print(
        order.order_id,
        "| ₹",
        order.total_amount,
        sep=""
    )


# sorted() uses sort_index because it is the first comparison field.
ascending_orders = sorted(orders)

print("\nLOWEST TO HIGHEST AMOUNT")
print("=" * 45)

for order in ascending_orders:
    print(
        order.order_id,
        "|",
        order.customer,
        "| ₹",
        order.total_amount,
        sep=""
    )


# reverse=True sorts from highest to lowest.
descending_orders = sorted(
    orders,
    reverse=True
)

print("\nHIGHEST TO LOWEST AMOUNT")
print("=" * 45)

for order in descending_orders:
    print(
        order.order_id,
        "|",
        order.customer,
        "| ₹",
        order.total_amount,
        sep=""
    )


# Comparison methods are created by order=True.
print("\nOBJECT COMPARISON")
print("=" * 45)

print(
    "Is first order cheaper than second?",
    orders[0] < orders[1]
)

print(
    "Is third order greater than second?",
    orders[2] > orders[1]
)


# min() and max() also use the generated comparison methods.
cheapest_order = min(orders)
highest_order = max(orders)

print("\nCHEAPEST ORDER")
cheapest_order.display()

print("\nHIGHEST-VALUE ORDER")
highest_order.display()
