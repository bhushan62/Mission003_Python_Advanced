from dataclasses import dataclass, field


@dataclass
class LaundryOrder:
    order_id: str
    customer: str

    # Each order receives its own new empty list.
    # Never use garments: list[str] = [] in a dataclass.
    garments: list[str] = field(default_factory=list)

    # Each order also receives its own dictionary.
    service_prices: dict[str, float] = field(default_factory=dict)

    status: str = "Processing"

    def add_garment(
        self,
        garment: str,
        price: float
    ) -> None:
        """Add a garment and its price to this order."""

        self.garments.append(garment)
        self.service_prices[garment] = price

    def calculate_total(self) -> float:
        """Calculate the total price of all garments."""

        return sum(self.service_prices.values())

    def display_order(self) -> None:
        """Display the complete laundry order."""

        print("=" * 40)
        print("KLYN LAUNDRY ORDER")
        print("=" * 40)
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Garments:", self.garments)
        print("Service prices:", self.service_prices)
        print("Status:", self.status)
        print(
            "Total amount: ₹",
            self.calculate_total(),
            sep=""
        )


# Create the first order.
order_one = LaundryOrder(
    order_id="AO45821",
    customer="Ravi Kumar"
)

# Add garments to the first order.
order_one.add_garment("Shirt", 85.0)
order_one.add_garment("Trouser", 150.0)


# Create a second order.
order_two = LaundryOrder(
    order_id="AO33396",
    customer="Suresh Babu"
)

# Add a garment only to the second order.
order_two.add_garment("Saree", 250.0)


print("FIRST ORDER")
order_one.display_order()

print("\nSECOND ORDER")
order_two.display_order()


# Confirm that both orders have separate lists.
print("\nSEPARATE LIST CHECK")
print("First-order garments:", order_one.garments)
print("Second-order garments:", order_two.garments)
print(
    "Are both garment lists the same object?",
    order_one.garments is order_two.garments
)