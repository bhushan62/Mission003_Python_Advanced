from itertools import islice


orders = [
    {
        "order_id": "AO50001",
        "customer": "Ravi Kumar",
        "status": "Ready",
        "amount": 800
    },
    {
        "order_id": "AO50002",
        "customer": "Suresh Babu",
        "status": "Processing",
        "amount": 1500
    },
    {
        "order_id": "AO50003",
        "customer": "Anjali Devi",
        "status": "Ready",
        "amount": 2200
    },
    {
        "order_id": "AO50004",
        "customer": "Kiran Kumar",
        "status": "Delivered",
        "amount": 600
    },
    {
        "order_id": "AO50005",
        "customer": "Lakshmi Devi",
        "status": "Ready",
        "amount": 550
    }
]


print("=" * 50)
print("QUESTION 1: MANUAL ITERATOR")
print("=" * 50)

order_iterator = iter(orders)

first_order = next(order_iterator)
second_order = next(order_iterator)

print("First order:", first_order["order_id"])
print("Second order:", second_order["order_id"])


print("\n" + "=" * 50)
print("QUESTION 2: GENERATOR FUNCTION")
print("=" * 50)


def generate_ready_orders(order_records):
    for order in order_records:
        if order["status"].casefold() == "ready":
            yield order


ready_orders = generate_ready_orders(orders)

for order in ready_orders:
    print("Ready:", order["order_id"])


print("\n" + "=" * 50)
print("QUESTION 3: GENERATOR EXPRESSION")
print("=" * 50)

large_amounts = (
    order["amount"]
    for order in orders
    if order["amount"] > 1000
)

for amount in large_amounts:
    print("Large amount: ₹", amount, sep="")


print("\n" + "=" * 50)
print("QUESTION 4: GENERATOR WITH SUM")
print("=" * 50)

total_revenue = sum(
    order["amount"]
    for order in orders
)

print("Total revenue: ₹", total_revenue, sep="")


print("\n" + "=" * 50)
print("QUESTION 5: YIELD FROM")
print("=" * 50)

counter_orders = [
    "AO60001",
    "AO60002"
]

online_orders = [
    "AO70001",
    "AO70002"
]


def combine_orders(counter, online):
    yield from counter
    yield from online


combined_orders = combine_orders(
    counter_orders,
    online_orders
)

for order_id in combined_orders:
    print("Combined:", order_id)


print("\n" + "=" * 50)
print("QUESTION 6: ENUMERATE")
print("=" * 50)

# A fresh generator is required because the earlier one was consumed.
ready_orders = generate_ready_orders(orders)

for number, order in enumerate(
    ready_orders,
    start=1
):
    print(
        f'{number}. {order["order_id"]}'
    )


print("\n" + "=" * 50)
print("QUESTION 7: ZIP WITH STRICT")
print("=" * 50)

order_ids = [
    "AO80001",
    "AO80002",
    "AO80003"
]

customers = [
    "Ravi Kumar",
    "Suresh Babu",
    "Anjali Devi"
]

combined_records = zip(
    order_ids,
    customers,
    strict=True
)

for order_id, customer in combined_records:
    print(
        f"{order_id} | {customer}"
    )


print("\n" + "=" * 50)
print("QUESTION 8: ISLICE")
print("=" * 50)

# Create another fresh ready-order generator.
ready_orders = generate_ready_orders(orders)

first_two_ready_orders = islice(
    ready_orders,
    2
)

for order in first_two_ready_orders:
    print(
        "Selected:",
        order["order_id"]
    )


print("\n" + "=" * 50)
print("THEORY ANSWERS")
print("=" * 50)

# 1. An iterable is an object we can loop through.
#    Examples include lists, strings, tuples, dictionaries and files.
#    An iterator remembers its current position and provides the next value.

# 2. StopIteration means that an iterator or generator has no more
#    values available.

# 3. return provides a result and finishes the function.
#    yield provides one value, pauses the function and preserves its state.

# 4. Generators are memory-efficient because they produce one value
#    at a time instead of storing every result in memory.

# 5. A generator is a one-way iterator. After all its values have been
#    consumed, it is exhausted. We must create a fresh generator to
#    process the values again.

# 6. itertools.count() and itertools.cycle() produce infinite values.
#    Without break, islice() or another stopping condition, the loop
#    can continue indefinitely.


print("1. Iterable contains values; iterator delivers them one at a time.")

print("2. StopIteration means that no more values are available.")

print("3. return finishes; yield pauses and can continue later.")

print("4. Generators produce one value at a time and save memory.")

print("5. An exhausted generator cannot restart automatically.")

print("6. count() and cycle() can run forever without a stopping condition.")


print("\n" + "=" * 50)
print("FINAL TEST COMPLETED")
print("=" * 50)