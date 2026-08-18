# def add_message(original_function):
#     def wrapper(order_id, customer):
#         print("KLYN Laundry Notification")

#         original_function(order_id, customer)

#         print("Thank you for choosing KLYN")

#     return wrapper


# @add_message
# def order_notification(order_id, customer):
#     print(f"Hello {customer}, order {order_id} is ready.")


# order_notification("AO45821", "Ravi")


def add_message(original_function):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        print("KLYN Laundry Notification")
        print("=" * 40)

        original_function(*args, **kwargs)

        print("Thank you for choosing KLYN")
        print("=" * 40)

    return wrapper


@add_message
def order_notification(order_id, customer):
    print(f"Hello {customer}")
    print(f"Your order {order_id} is ready.")


@add_message
def bill_notification(order_id, amount, status):
    print(f"Order ID: {order_id}")
    print(f"Amount: ₹{amount}")
    print(f"Status: {status}")


order_notification("AO45821", "Ravi")

print()

bill_notification(
    order_id="AO33396",
    amount=1750,
    status="Paid"
)