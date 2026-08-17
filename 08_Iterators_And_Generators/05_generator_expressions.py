order_ids = ["AO12345", "BO33396", "AO45821", "XX98765"]

valid_orders = (
    order_id
    for order_id in order_ids
    if order_id.startswith("AO")
)

for order_id in valid_orders:
    print("Valid order:", order_id)


amounts = [850, 1200, 450, 1750, 600]

large_bills = (
    amount
    for amount in amounts
    if amount >= 1000
)

for amount in large_bills:
    print("Large bill: ₹", amount, sep="")


services = [
    "dry cleaning",
    "wash and iron",
    "steam iron"
]

formatted_services = (
    service.title()
    for service in services
)

for service in formatted_services:
    print(service)


orders = [
    {"order_id": "AO11111", "amount": 500},
    {"order_id": "AO22222", "amount": 1500},
    {"order_id": "AO33333", "amount": 900},
    {"order_id": "AO44444", "amount": 2200}
]

premium_orders = (
    order["order_id"]
    for order in orders
    if order["amount"] >= 1000
)

for order_id in premium_orders:
    print("Premium order:", order_id)

services = ["Dry Cleaning", "Wash and Iron", "Steam Iron"]

service_generator = (
    service
    for service in services
)

for service in service_generator:
    print("First loop:", service)

for service in service_generator:
    print("Second loop:", service)

service_generator = (
    service
    for service in services
)

import sys

number_list = [number for number in range(1_000_000)]
number_generator = (number for number in range(1_000_000))

print("List size:", sys.getsizeof(number_list), "bytes")
print("Generator size:", sys.getsizeof(number_generator), "bytes")

orders = [
    {"order_id": "AO11111", "amount": 500},
    {"order_id": "AO22222", "amount": 1500},
    {"order_id": "AO33333", "amount": 900}
]

total_amount = sum(
    order["amount"]
    for order in orders
)

print("Total revenue: ₹", total_amount, sep="")


orders = [
    {"order_id": "AO11111", "status": "Ready", "amount": 800},
    {"order_id": "AO22222", "status": "Processing", "amount": 1400},
    {"order_id": "AO33333", "status": "Ready", "amount": 1750},
    {"order_id": "AO44444", "status": "Delivered", "amount": 600}
]



ready_orders = (
    order["order_id"]
    for order in orders
    if order["status"] == "Ready"
)

for order_id in ready_orders:
    print("Ready order:", order_id)


large_amounts = (
    order["amount"]
    for order in orders
    if order["amount"] > 800
)

for amount in large_amounts:
    print("Large amount: ₹", amount, sep="")


total_revenue = sum(
order["amount"]
for order in orders
)

print("Total revenue: ₹", total_revenue, sep="")