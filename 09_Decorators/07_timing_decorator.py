import time
from functools import wraps


def measure_time(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = original_function(*args, **kwargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(
            f"{original_function.__name__} completed "
            f"in {execution_time:.4f} seconds"
        )

        return result

    return wrapper

@measure_time
def process_laundry_orders(number_of_orders):
    print(f"Processing {number_of_orders} orders...")

    time.sleep(2)

    return number_of_orders


processed_orders = process_laundry_orders(100)

print("Processed orders:", processed_orders)

import time
from functools import wraps


def measure_time(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = original_function(*args, **kwargs)

        execution_time = time.perf_counter() - start_time

        print(
            f"Execution time: {execution_time:.8f} seconds"
        )

        return result

    return wrapper


@measure_time
def generate_customer_messages(orders):
    messages = []

    for order in orders:
        message = (
            f"Hello {order['customer']}, "
            f"order {order['order_id']} is {order['status']}."
        )

        messages.append(message)

    return messages


laundry_orders = [
    {
        "order_id": "AO45821",
        "customer": "Ravi",
        "status": "Ready"
    },
    {
        "order_id": "AO33396",
        "customer": "Suresh",
        "status": "Processing"
    },
    {
        "order_id": "AO98765",
        "customer": "Anjali",
        "status": "Delivered"
    }
]


messages = generate_customer_messages(laundry_orders)

for message in messages:
    print(message)