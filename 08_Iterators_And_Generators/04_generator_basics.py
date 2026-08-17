def generate_orders():
    print("Generator started")

    yield "AO12345"
    print("First order completed")

    yield "AO33396"
    print("Second order completed")

    yield "AO45821"
    print("Third order completed")


orders = generate_orders()

print("Generator created")

print(next(orders))
print(next(orders))
print(next(orders))

try:
    print(next(orders))
except StopIteration:
    print("Generator exhausted")


def generate_services():
    
    yield "Dry Cleaning"
    yield "Wash and Iron"
    yield "Steam Iron"
    yield "Wash and Fold"


for service in generate_services():
    print("Service:", service)

def generate_ready_orders(orders):
    for order in orders:
        if order["status"] == "Ready":
            yield order["order_id"]


laundry_orders = [
    {"order_id": "AO12345", "status": "Ready"},
    {"order_id": "AO33396", "status": "Processing"},
    {"order_id": "AO45821", "status": "Ready"},
    {"order_id": "AO98765", "status": "Delivered"}
]

ready_orders = generate_ready_orders(laundry_orders)

for order_id in ready_orders:
    print("Ready order:", order_id)

def generate_pending_orders(orders):
    for order in orders:
        if order["status"] == "Pending":
            yield order["order_id"]


orders = [
    {"order_id": "AO11111", "status": "Pending"},
    {"order_id": "AO22222", "status": "Ready"},
    {"order_id": "AO33333", "status": "Pending"},
    {"order_id": "AO44444", "status": "Delivered"}
]

pending_orders = generate_pending_orders(orders)

for order_id in pending_orders:
    print("Pending order:", order_id)