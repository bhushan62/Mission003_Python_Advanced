import logging
import re
import time

from functools import wraps
from pathlib import Path


LOG_FILE = Path(__file__).with_name(
    "klyn_notifications.log"
)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)


logger = logging.getLogger(__name__)

# Execution-time decorator

def measure_time(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = original_function(*args, **kwargs)

        execution_time = (
            time.perf_counter() - start_time
        )

        print(
            f"Execution time: "
            f"{execution_time:.8f} seconds"
        )

        return result

    return wrapper

# Logging decorator

def log_activity(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logger.info(
            "%s started",
            original_function.__name__
        )

        try:
            result = original_function(
                *args,
                **kwargs
            )

            logger.info(
                "%s completed successfully",
                original_function.__name__
            )

            return result

        except Exception:
            logger.exception(
                "%s failed",
                original_function.__name__
            )

            raise

    return wrapper

#Error-handling decorator

def handle_errors(default_return=None):
    def decorator(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            try:
                return original_function(
                    *args,
                    **kwargs
                )

            except (
                KeyError,
                ValueError,
                TypeError
            ) as error:
                print("Notification rejected")
                print(
                    "Error:",
                    type(error).__name__
                )
                print("Reason:", error)

                return default_return

        return wrapper

    return decorator


# Order-validation decorator

def validate_order(original_function):
    @wraps(original_function)
    def wrapper(order, *args, **kwargs):
        if not isinstance(order, dict):
            raise TypeError(
                "Order must be a dictionary"
            )

        required_fields = (
            "order_id",
            "customer",
            "phone",
            "status",
            "amount"
        )

        for field in required_fields:
            if field not in order:
                raise KeyError(field)

        if not re.fullmatch(
            r"AO\d{5}",
            order["order_id"]
        ):
            raise ValueError(
                "Invalid order ID"
            )

        clean_phone = re.sub(
            r"[^0-9]",
            "",
            order["phone"]
        )

        if (
            len(clean_phone) == 12
            and clean_phone.startswith("91")
        ):
            clean_phone = clean_phone[2:]

        if not re.fullmatch(
            r"[6-9]\d{9}",
            clean_phone
        ):
            raise ValueError(
                "Invalid Indian mobile number"
            )

        if order["status"].casefold() != "ready":
            raise ValueError(
                "Order is not ready"
            )

        clean_order = order.copy()
        clean_order["phone"] = clean_phone

        return original_function(
            clean_order,
            *args,
            **kwargs
        )

    return wrapper


# Main business function

@measure_time
@handle_errors(default_return=None)
@log_activity
@validate_order
def prepare_whatsapp_message(order):
    message = (
        f"Dear {order['customer']},\n"
        f"your order {order['order_id']} "
        f"is ready for collection.\n"
        f"Amount: ₹{order['amount']}\n"
        f"Contact: {order['phone']}\n"
        f"Thank you for choosing KLYN."
    )

    return message


# Test Orders

orders = [
    {
        "order_id": "AO45821",
        "customer": "Ravi",
        "phone": "+91-98765 43210",
        "status": "Ready",
        "amount": 1750
    },
    {
        "order_id": "BO33396",
        "customer": "Suresh",
        "phone": "9876543210",
        "status": "Ready",
        "amount": 850
    },
    {
        "order_id": "AO98765",
        "customer": "Anjali",
        "phone": "9876543210",
        "status": "Processing",
        "amount": 1200
    }
]


# Process the orders

for order in orders:
    print("=" * 50)

    message = prepare_whatsapp_message(order)

    if message is not None:
        print(message)
    else:
        print(
            "Message was not prepared for",
            order.get("order_id", "Unknown")
        )

    print()