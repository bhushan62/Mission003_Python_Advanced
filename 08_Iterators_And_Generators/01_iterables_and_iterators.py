orders = ["AO12345", "AO33396", "AO45821"]

order_iterator = iter(orders)

try:
    print(next(order_iterator))
    print(next(order_iterator))
    print(next(order_iterator))
    print(next(order_iterator))

except StopIteration:
    print("No more orders available.")

services = [
    "Dry Cleaning",
    "Wash and Iron",
    "Steam Iron",
    "Wash and Fold"
]

services_iterator = iter(services)

try: 
    print(next(services_iterator))
    print(next(services_iterator))
    print(next(services_iterator))
    print(next(services_iterator))
    print(next(services_iterator))
 
except StopIteration:
        print("All services processed.")

    
