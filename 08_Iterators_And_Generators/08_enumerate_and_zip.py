services = [
    "Dry Cleaning",
    "Wash and Iron",
    "Steam Iron"
]

service_iterator = enumerate(services, start=1)

print(next(service_iterator))
print(next(service_iterator))
print(next(service_iterator))

order_ids = [
    "AO10001",
    "AO10002",
    "AO10003"
]

customers = [
    "Ravi Kumar",
    "Suresh Babu",
    "Anjali Devi"
]

amounts = [
    850,
    1200,
    1750
]

combined_orders = zip(
    order_ids,
    customers,
    amounts
)

for order_id, customer, amount in combined_orders:
    print(
        f"{order_id} | "
        f"{customer} | "
        f"₹{amount}"
    )

combined_orders = zip(
    order_ids,
    customers,
    amounts
)

for order in combined_orders:
    print("First loop:", order)

for order in combined_orders:
    print("Second loop:", order)

order_ids = ["AO10001", "AO10002", "AO10003"]

customers = ["Ravi Kumar", "Suresh Babu"]

for order_id, customer in zip(order_ids, customers):
    print(order_id, customer)

try:
    for order_id, customer in zip(
        order_ids,
        customers,
        strict=True
    ):
        print(order_id, customer)

except ValueError as error:
    print("Data length error:", error)



# Combined Enumerators and Zip


order_ids = ["AO10001", "AO10002", "AO10003"]
customers = ["Ravi Kumar", "Suresh Babu", "Anjali Devi"]
amounts = [850, 1200, 1750]

combined_orders = zip(
    order_ids,
    customers,
    amounts,
    strict=True
)

for serial_number, order in enumerate(
    combined_orders,
    start=1
):
    order_id, customer, amount = order

    print(
        f"{serial_number}. "
        f"{order_id} | "
        f"{customer} | "
        f"₹{amount}"
    )


    