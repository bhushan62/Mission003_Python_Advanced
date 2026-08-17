def order_processor():
    order_id = yield "Processor ready"

    while True:
        print("Processing:", order_id)

        order_id = yield f"{order_id} completed"


processor = order_processor()

message = next(processor)
print(message)

result = processor.send("AO10001")
print(result)

result = processor.send("AO10002")
print(result)

# Closing a generator:

def generate_orders():
    yield "AO10001"
    yield "AO10002"
    yield "AO10003"


orders = generate_orders()

print(next(orders))

orders.close()

try:
    print(next(orders))
except StopIteration:
    print("Generator has been closed.")

# Cleaning Resource with finally:

def process_orders(orders):
    print("Order processor opened")

    try:
        for order in orders:
            yield order

    finally:
        print("Order processor closed")


order_ids = [
    "AO10001",
    "AO10002",
    "AO10003"
]

processor = process_orders(order_ids)

print(next(processor))
print(next(processor))

processor.close()


#3. Sending an exception with throw()

def receive_orders():
    while True:
        try:
            order_id = yield "Waiting for order"
            print("Received:", order_id)

        except ValueError as error:
            print("Rejected:", error)


receiver = receive_orders()

print(next(receiver))

print(receiver.send("AO10001"))

print(
    receiver.throw(
        ValueError("Invalid order ID: BO123")
    )
)

print(receiver.send("AO10002"))

receiver.close()

from inspect import getgeneratorstate


def sample_generator():
    yield "First"
    yield "Second"


generator = sample_generator()

print(getgeneratorstate(generator))

print(next(generator))

print(getgeneratorstate(generator))

generator.close()

print(getgeneratorstate(generator))


