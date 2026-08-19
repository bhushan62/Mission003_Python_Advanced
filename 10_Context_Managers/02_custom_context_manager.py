from pathlib import Path


class LaundryOrderFile:
    def __init__(self, file_name, mode):
        self.file_path = Path(__file__).with_name(
            file_name
        )

        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening order file")

        self.file = open(
            self.file_path,
            self.mode,
            encoding="utf-8"
        )

        return self.file

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback
    ):
        print("Closing order file")

        if self.file is not None:
            self.file.close()

        return False

with LaundryOrderFile(
    "custom_orders.txt",
    "w"
) as order_file:
    order_file.write(
        "AO45821 | Ravi | Ready\n"
    )

    order_file.write(
        "AO33396 | Suresh | Processing\n"
    )


print(
    "Is custom file closed?",
    order_file.closed
)