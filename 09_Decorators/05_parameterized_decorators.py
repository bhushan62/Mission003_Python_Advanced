# def notification_header(title):
#     def decorator(original_function):
#         def wrapper(*args, **kwargs):
#             print("=" * 40)
#             print(title)
#             print("=" * 40)

#             result = original_function(*args, **kwargs)

#             print("=" * 40)

#             return result

#         return wrapper

#     return decorator
# @notification_header("KLYN ORDER NOTIFICATION")
# def order_ready(order_id, customer):
#     message = f"Hello {customer}, order {order_id} is ready."

#     print(message)

#     return message


# order_ready("AO45821", "Ravi")


#=============================   PRACTICAL USAGE ==================================#

def require_order_status(required_status):
    def decorator(original_function):
        def wrapper(order, *args, **kwargs):
            actual_status = order.get("status")

            if actual_status != required_status:
                print(
                    f"Action rejected: order status must be "
                    f"{required_status}"
                )
                return None

            return original_function(order, *args, **kwargs)

        return wrapper

    return decorator

@require_order_status("Ready")
def send_collection_message(order):
    message = (
        f"Hello {order['customer']}, "
        f"order {order['order_id']} is ready for collection."
    )

    print(message)

    return message

ready_order = {
    "order_id": "AO45821",
    "customer": "Ravi",
    "status": "Ready"
}

processing_order = {
    "order_id": "AO33396",
    "customer": "Suresh",
    "status": "Processing"
}


send_collection_message(ready_order)

print()

send_collection_message(processing_order)