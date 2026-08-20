from dataclasses import dataclass


# ==================================================
# PARENT DATACLASS
# ==================================================

@dataclass
class LaundryOrder:
    """Store the common information for every laundry order."""

    order_id: str
    customer: str
    service: str
    quantity: int
    price_per_item: float
    status: str = "Processing"

    def __post_init__(self) -> None:
        """Validate the order immediately after creation."""

        if not self.order_id.startswith("AO"):
            raise ValueError("Order ID must begin with AO")

        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if self.price_per_item <= 0:
            raise ValueError("Price must be greater than zero")

    @property
    def total_amount(self) -> float:
        """Calculate the regular order amount."""

        return self.quantity * self.price_per_item

    def display(self) -> None:
        """Display the complete order information."""

        print("=" * 45)
        print("REGULAR LAUNDRY ORDER")
        print("=" * 45)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print("Price per item: ₹", self.price_per_item, sep="")
        print("Status:", self.status)
        print("Total amount: ₹", self.total_amount, sep="")


# ==================================================
# CHILD DATACLASS
# ==================================================

@dataclass
class ExpressLaundryOrder(LaundryOrder):
    """
    Inherit all fields and methods from LaundryOrder.

    Express service costs twice the regular price.
    """

    express_multiplier: float = 2.0

    def __post_init__(self) -> None:
        # Run the validation defined in the parent class.
        super().__post_init__()

        if self.express_multiplier < 1:
            raise ValueError(
                "Express multiplier must be at least 1"
            )

    @property
    def total_amount(self) -> float:
        """
        Override the parent's total_amount property.

        Regular amount:
        quantity * price_per_item

        Express amount:
        quantity * price_per_item * express_multiplier
        """

        regular_amount = (
            self.quantity * self.price_per_item
        )

        return regular_amount * self.express_multiplier

    def display(self) -> None:
        """Display the express-order information."""

        print("=" * 45)
        print("EXPRESS LAUNDRY ORDER")
        print("=" * 45)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Service:", self.service)
        print("Quantity:", self.quantity)
        print("Regular price: ₹", self.price_per_item, sep="")
        print("Express multiplier:", self.express_multiplier)
        print("Status:", self.status)
        print("Total amount: ₹", self.total_amount, sep="")


# ==================================================
# CREATE A REGULAR ORDER
# ==================================================

regular_order = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar",
    service="Shirt",
    quantity=3,
    price_per_item=85.0,
    status="Ready"
)


# ==================================================
# CREATE AN EXPRESS ORDER
# ==================================================

express_order = ExpressLaundryOrder(
    order_id="AO33396",
    customer="Suresh Babu",
    service="Shirt",
    quantity=3,
    price_per_item=85.0,
    status="Processing",
    express_multiplier=2.0
)


# ==================================================
# DISPLAY BOTH ORDERS
# ==================================================

regular_order.display()

print()

express_order.display()


# ==================================================
# INHERITANCE CHECK
# ==================================================

print("\n" + "=" * 45)
print("INHERITANCE CHECK")
print("=" * 45)

print(
    "Is regular_order a LaundryOrder?",
    isinstance(regular_order, LaundryOrder)
)

print(
    "Is express_order an ExpressLaundryOrder?",
    isinstance(express_order, ExpressLaundryOrder)
)

print(
    "Is express_order also a LaundryOrder?",
    isinstance(express_order, LaundryOrder)
)


# ==================================================
# COMPARE THE PRICES
# ==================================================

print("\n" + "=" * 45)
print("PRICE COMPARISON")
print("=" * 45)

print(
    "Regular bill: ₹",
    regular_order.total_amount,
    sep=""
)

print(
    "Express bill: ₹",
    express_order.total_amount,
    sep=""
)

print(
    "Extra express charge: ₹",
    express_order.total_amount
    - regular_order.total_amount,
    sep=""
)