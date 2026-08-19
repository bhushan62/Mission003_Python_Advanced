from pathlib import Path


LOG_FILE = Path(__file__).with_name(
    "10.laundry_test.log"
)


class LaundryLog:
    def __enter__(self):
        self.file = open(
            LOG_FILE,
            "w",
            encoding="utf-8"
        )

        print("Log opened")

        return self.file

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback
    ):
        self.file.close()

        print("Log closed")

        if exception_type is not None:
            print(
                "Error:",
                exception_value
            )

        # Allow the exception to continue
        return False

log_manager = LaundryLog()


try:
    with log_manager as log:
        log.write(
            "AO45821 | Ravi | Ready\n"
        )

        raise ValueError(
            "Invalid test order"
        )

except ValueError:
    print(
        "Error handled by main program"
    )


print(
    "File closed:",
    log_manager.file.closed
)