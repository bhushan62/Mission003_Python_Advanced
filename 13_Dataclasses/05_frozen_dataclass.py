# Import dataclass to create the data model.
# FrozenInstanceError helps us catch attempts to modify a frozen object.
from dataclasses import dataclass, FrozenInstanceError


# frozen=True makes every object of this class immutable.
# Immutable means its field values cannot be changed after creation.
@dataclass(frozen=True)
class ServiceRate:
    service: str
    regular_price: float
    express_price: float

    def display(self) -> None:
        """Display the service-rate information."""

        print("=" * 40)
        print("KLYN SERVICE RATE")
        print("=" * 40)
        print("Service:", self.service)
        print("Regular price: ₹", self.regular_price, sep="")
        print("Express price: ₹", self.express_price, sep="")


# Create a frozen ServiceRate object.
shirt_rate = ServiceRate(
    service="Shirt",
    regular_price=85.0,
    express_price=170.0
)

# Reading the fields is allowed.
shirt_rate.display()


print("\nREADING VALUES")
print("=" * 40)
print("Service:", shirt_rate.service)
print("Regular price:", shirt_rate.regular_price)


print("\nTRYING TO CHANGE PRICE")
print("=" * 40)

try:
    # This is not allowed because the dataclass is frozen.
    shirt_rate.regular_price = 100.0

except FrozenInstanceError as error:
    print("Price modification rejected")
    print("Reason:", error)


# Because frozen dataclass objects are hashable,
# they can normally be stored inside a set.
service_rates = {
    ServiceRate("Shirt", 85.0, 170.0),
    ServiceRate("Trouser", 150.0, 300.0),
    ServiceRate("Saree", 250.0, 500.0),

    # This duplicate will not be added twice.
    ServiceRate("Shirt", 85.0, 170.0)
}


print("\nUNIQUE SERVICE RATES")
print("=" * 40)

for rate in service_rates:
    print(
        rate.service,
        "| Regular: ₹",
        rate.regular_price,
        "| Express: ₹",
        rate.express_price,
        sep=""
    )


print("\nPROGRAM COMPLETED")