class LaundryOrderIterator:

    def __init__(self, orders):
        self.orders = orders
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.orders):
            raise StopIteration

        current_order = self.orders[self.position]
        self.position += 1

        return current_order


orders = ["AO12345", "AO33396", "AO45821"]

order_iterator = LaundryOrderIterator(orders)

print(next(order_iterator))
print(next(order_iterator))
print(next(order_iterator))

try:
    print(next(order_iterator))
except StopIteration:
    print("All laundry orders processed.")


laundry_orders = [
    {"order_id": "AO12345", "status": "Ready"},
    {"order_id": "AO33396", "status": "Processing"},
    {"order_id": "AO45821", "status": "Delivered"}
]

laundry_iterator = LaundryOrderIterator(laundry_orders)

for order in laundry_iterator:
    print(
        "Order:",
        order["order_id"],
        "| Status:",
        order["status"]
    ) 