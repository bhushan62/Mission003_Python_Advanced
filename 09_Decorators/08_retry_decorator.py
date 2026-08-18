import time
from functools import wraps


def retry(
    max_attempts=3,
    delay_seconds=1,
    exceptions=(ConnectionError, TimeoutError)
):
    def decorator(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(
                        f"Attempt {attempt} of {max_attempts}"
                    )

                    result = original_function(
                        *args,
                        **kwargs
                    )

                    print("Operation successful")

                    return result

                except exceptions as error:
                    print(
                        f"Attempt {attempt} failed: {error}"
                    )

                    if attempt == max_attempts:
                        print("Maximum attempts reached")
                        raise

                    print(
                        f"Retrying after "
                        f"{delay_seconds} second(s)..."
                    )

                    time.sleep(delay_seconds)

        return wrapper

    return decorator


attempt_state = {
    "count": 0
}


@retry(
    max_attempts=3,
    delay_seconds=1
)
def send_whatsapp_notification(
    phone,
    order_id
):
    attempt_state["count"] += 1

    if attempt_state["count"] < 3:
        raise ConnectionError(
            "WhatsApp service temporarily unavailable"
        )

    message = (
        f"Order {order_id} notification "
        f"sent to {phone}"
    )

    return message


result = send_whatsapp_notification(
    "9876543210",
    "AO45821"
)

print("Result:", result)



# ====================== SMALL CODE ON TIME DELAY ======================== #

import time

start_time = time.perf_counter()

print("Task started")

time.sleep(4)

print("Task completed")

end_time = time.perf_counter()

print(
    "Execution time:",
    end_time - start_time,
    "seconds"
)