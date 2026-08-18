# def order_notification():
#     print("Order AO45821 is ready")


# order_notification()

# notification = order_notification

# notification()

def add_message(function):
    def wrapper():
        print("=====================================")
        print("KLYN Laundry Notification")
        print("=====================================")
        function()
        print("\nThank you for choosing KLYN")
        print("Store Contact: 8008815840")
        print("=====================================")

    return wrapper


def order_notification():
    print("Order AO45821 is ready with us. Kindly collect your order.")


decorated_function = add_message(order_notification)

decorated_function()


def add_message(original_function):
    def wrapper():
        print("\nBefore original function")

        original_function()

        print("After original function")

    return wrapper


@add_message
def order_notification():
    print("Order AO45821 is ready")


order_notification()
