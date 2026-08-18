from functools import wraps


def require_minimum_bill(minimum_amount):
    def decorator(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if args:
                amount = args[0]
            else:
                amount = kwargs.get("amount")

            if amount is None:
                print("Bill amount was not provided")
                return None

            if amount < minimum_amount:
                print(
                    f"Bill must be at least "
                    f"₹{minimum_amount}"
                )
                return None

            result = original_function(
                *args,
                **kwargs
            )

            return result

        return wrapper

    return decorator


@require_minimum_bill(500)
def apply_discount(
    amount,
    discount_percentage
):
    discount = (
        amount * discount_percentage / 100
    )

    final_amount = amount - discount

    return final_amount


print("=" * 40)
print("TEST 1: ACCEPTED BILL")
print("=" * 40)

result = apply_discount(1000, 10)

if result is not None:
    print("Final bill: ₹", result, sep="")
else:
    print("Discount rejected")


print()


print("=" * 40)
print("TEST 2: REJECTED BILL")
print("=" * 40)

result = apply_discount(400, 10)

if result is not None:
    print("Final bill: ₹", result, sep="")
else:
    print("Discount rejected")


print()


print("=" * 40)
print("TEST 3: KEYWORD ARGUMENTS")
print("=" * 40)

result = apply_discount(
    amount=1500,
    discount_percentage=20
)

if result is not None:
    print("Final bill: ₹", result, sep="")
else:
    print("Discount rejected")