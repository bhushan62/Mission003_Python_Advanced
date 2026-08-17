# 1. chain() — combine iterables

from itertools import chain


counter_orders = ["AO10001", "AO10002"]
website_orders = ["AO20001", "AO20002"]
whatsapp_orders = ["AO30001", "AO30002"]

all_orders = chain(
    counter_orders,
    website_orders,
    whatsapp_orders
)

for order_id in all_orders:
    print("Order:", order_id)

# 2. islice() — take part of an iterator

from itertools import islice


orders = (
    f"AO{number:05d}"
    for number in range(1, 101)
)

first_five_orders = islice(orders, 5)

for order_id in first_five_orders:
    print(order_id)

numbers = iter(range(1, 21))

selected_numbers = islice(numbers, 5, 10)

print(list(selected_numbers))

# 3. count() — generate an unlimited sequence

from itertools import count, islice


serial_numbers = count(start=1)

first_five = islice(serial_numbers, 5)

for number in first_five:
    print("Serial number:", number)

from itertools import count, islice

for number in count(start=1):
    print(number)

    if number == 5:
        break
# 4. cycle() — repeat values continuously


from itertools import cycle, islice


work_stages = cycle([
    "Washing",
    "Drying",
    "Ironing"
])

first_seven_stages = islice(work_stages, 7)

for stage in first_seven_stages:
    print(stage)

# 5. repeat() — repeat one value

from itertools import repeat


notifications = repeat(
    "Order ready for delivery",
    times=3
)

for message in notifications:
    print(message)

# Suppose we want to process only ten orders at a time: 

from itertools import islice


def generate_orders():
    for number in range(1, 101):
        yield {
            "order_id": f"AO{number:05d}",
            "status": "Pending"
        }


order_generator = generate_orders()

first_batch = islice(order_generator, 10)

for order in first_batch:
    print("Processing:", order["order_id"])


#  ------------------------------------------------------------------------------------------------------------------  #

 
# chain()  → combine iterables
# islice() → take a limited section
# count()  → infinite number sequence
# cycle()  → endlessly repeat multiple values
# repeat() → repeat one value