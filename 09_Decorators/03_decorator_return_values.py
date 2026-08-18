def log_bill(original_function):
    def wrapper(*args, **kwargs):
        print("Calculating bill...")

        result = original_function(*args, **kwargs)

        print("Calculation completed")

        return result

    return wrapper


@log_bill
def calculate_bill(quantity, price):
    return quantity * price


total = calculate_bill(3, 100)

print("Total:", total)


def bill_logger(original_function):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("KLYN BILL CALCULATION STARTED")

        result = original_function(*args, **kwargs)

        print("KLYN BILL CALCULATION COMPLETED")
        print("=" * 40)

        return result

    return wrapper


@bill_logger
def calculate_laundry_bill(
    shirts,
    shirt_price,
    trousers,
    trouser_price
):
    shirt_total = shirts * shirt_price
    trouser_total = trousers * trouser_price

    return shirt_total + trouser_total


final_bill = calculate_laundry_bill(
    shirts=3,
    shirt_price=85,
    trousers=2,
    trouser_price=120
)

print("Final bill: ₹", final_bill, sep="")

def decorator_name(original_function):
    def wrapper(*args, **kwargs):
        # Before

        result = original_function(*args, **kwargs)

        # After

        return result

    return wrapper