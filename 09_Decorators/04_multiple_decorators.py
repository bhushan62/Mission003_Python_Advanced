# def log_activity(original_function):
#     def wrapper(*args, **kwargs):
#         print("LOG: Function started")

#         result = original_function(*args, **kwargs)

#         print("LOG: Function completed")

#         return result

#     return wrapper


# def add_notification_header(original_function):
#     def wrapper(*args, **kwargs):
#         print("=" * 40)
#         print("KLYN LAUNDRY NOTIFICATION")
#         print("=" * 40)

#         result = original_function(*args, **kwargs)

#         print("=" * 40)

#         return result

#     return wrapper


# @log_activity
# @add_notification_header
# def order_notification(order_id, customer):
#     print(f"Hello {customer}")
#     print(f"Your order {order_id} is ready.")

#     return "Message prepared successfully"


# result = order_notification("AO45821", "Ravi")

# print("Result:", result)

# ===============================================================================================   #
# notification starts before wrapper starts

def log_activity(original_function):
    def wrapper(*args, **kwargs):
        print("LOG: Notification processing started")

        result = original_function(*args, **kwargs)

        print("LOG: Notification processing finished")

        return result

    return wrapper


def validate_order(original_function):
    def wrapper(*args, **kwargs):
        order_id = kwargs.get("order_id")

        if order_id is None and args:
            order_id = args[0]

        if not order_id or not order_id.startswith("AO"):
            print("Invalid order ID")
            return None

        return original_function(*args, **kwargs)

    return wrapper


@log_activity
@validate_order
def send_ready_message(order_id, customer):
    message = f"Hello {customer}, order {order_id} is ready."

    print(message)

    return message


send_ready_message("AO45821", "Ravi")

print()

send_ready_message("BO12345", "Suresh")