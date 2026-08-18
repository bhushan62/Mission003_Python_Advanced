import time
from functools import wraps


def handle_timeout(default_return=None):
    def decorator(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            try:
                return original_function(
                    *args,
                    **kwargs
                )

            except TimeoutError as error:
                print("=" * 40)
                print("OPERATION TIMED OUT")
                print(
                    "Function:",
                    original_function.__name__
                )
                print("Reason:", error)
                print("=" * 40)

                return default_return

        return wrapper

    return decorator


@handle_timeout(default_return=None)
def fetch_order_status(
    order_id,
    response_time,
    timeout_seconds
):
    print(f"Requesting status for {order_id}...")

    if response_time > timeout_seconds:
        time.sleep(timeout_seconds)

        raise TimeoutError(
            f"Service did not respond within "
            f"{timeout_seconds} seconds"
        )

    time.sleep(response_time)

    return {
        "order_id": order_id,
        "status": "Ready"
    }


order = fetch_order_status(
    order_id="AO45821",
    response_time=1,
    timeout_seconds=3
)

if order is not None:
    print("Order status:", order["status"])
else:
    print("Could not retrieve order status")


print()

order = fetch_order_status(
    order_id="AO33396",
    response_time=5,
    timeout_seconds=2
)

if order is not None:
    print("Order status:", order["status"])
else:
    print("Could not retrieve order status")