import time
from functools import lru_cache


# lru_cache remembers the result for each service.
# If the same service is requested again, Python returns
# the stored result instead of executing the function again.
@lru_cache(maxsize=10)
def get_service_price(service: str) -> float:
    print(f"Fetching price for {service}...")

    # Simulate a slow database or API request.
    time.sleep(2)

    service_prices = {
        "shirt": 85.0,
        "trouser": 100.0,
        "saree": 250.0,
        "bedsheet": 180.0,
    }

    return service_prices.get(service.casefold(), 0.0)


print("=" * 40)
print("FIRST REQUEST")
print("=" * 40)

# First call takes approximately two seconds.
shirt_price = get_service_price("shirt")
print("Shirt price: ₹", shirt_price, sep="")


print("\n" + "=" * 40)
print("SECOND REQUEST")
print("=" * 40)

# The same argument was already processed.
# The saved result is returned immediately.
shirt_price = get_service_price("shirt")
print("Shirt price: ₹", shirt_price, sep="")


print("\n" + "=" * 40)
print("DIFFERENT SERVICE")
print("=" * 40)

# This is a new argument, so the function runs again.
saree_price = get_service_price("saree")
print("Saree price: ₹", saree_price, sep="")


print("\n" + "=" * 40)
print("CALCULATE LAUNDRY BILL")
print("=" * 40)


def calculate_bill(
    service: str,
    quantity: int
) -> float:
    # Obtain the price, possibly from the cache.
    price_per_item = get_service_price(service)

    return quantity * price_per_item


bill = calculate_bill(
    service="shirt",
    quantity=4
)

print("Final bill: ₹", bill, sep="")


print("\nCACHE INFORMATION")

# hits: results returned from the cache
# misses: calls that required executing the function
# currsize: number of results currently stored
print(get_service_price.cache_info())