from collections.abc import Callable


type PriceCalculator = Callable[
    [int, float],
    float
]


def calculate_regular_price(
    quantity: int,
    price_per_item: float
) -> float:
    return quantity * price_per_item


def calculate_express_price(
    quantity: int,
    price_per_item: float
) -> float:
    regular_price: float = (
        quantity * price_per_item
    )

    return regular_price * 2


def process_order(
    quantity: int,
    price_per_item: float,
    pricing_function: PriceCalculator
) -> float:
    final_amount: float = pricing_function(
        quantity,
        price_per_item
    )

    return final_amount


regular_bill: float = process_order(
    quantity=3,
    price_per_item=85.0,
    pricing_function=calculate_regular_price
)


express_bill: float = process_order(
    quantity=3,
    price_per_item=85.0,
    pricing_function=calculate_express_price
)


print("Regular bill: ₹", regular_bill, sep="")
print("Express bill: ₹", express_bill, sep="")