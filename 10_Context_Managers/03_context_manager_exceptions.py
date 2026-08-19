class LaundryMachine:
    def __enter__(self):
        print("Machine started")
        return self

    def wash_order(self, order_id):
        print(f"Washing order: {order_id}")

        # Creating an error for practice
        result = 10 / 0

        return result

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback
    ):
        print("Machine stopped safely")

        if exception_type is not None:
            print("An error occurred")
            print("Error type:", exception_type.__name__)
            print("Error message:", exception_value)

        return False                                                                    # return False   --- Means I have completed Cleanup


try:
    with LaundryMachine() as machine:
        machine.wash_order("AO45821")

except ZeroDivisionError:
    print("The main program handled the error")


print("Program continues running")

class SafeLaundryMachine:
    def __enter__(self):
        print("\nSafe machine started")
        return self

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback
    ):
        print("Safe machine stopped")

        if exception_type is not None:
            print("Error handled inside context manager")
            print("Error:", exception_value)

        return True


with SafeLaundryMachine() as machine:
    result = 10 / 0


print("Program continues without outer try-except")