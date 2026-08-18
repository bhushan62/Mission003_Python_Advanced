from functools import wraps


def log_activity(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        print("Function started")

        result = original_function(*args, **kwargs)

        print("Function completed")

        return result

    return wrapper


@log_activity
def send_ready_message(order_id):
    """Send a notification when an order is ready."""

    print(f"Order {order_id} is ready.")


send_ready_message("AO45821")

print("Function name:", send_ready_message.__name__)
print("Documentation:", send_ready_message.__doc__)