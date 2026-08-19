from pathlib import Path


SOURCE_FILE = Path(__file__).with_name(
    "laundry_report.txt"
)

READY_FILE = Path(__file__).with_name(
    "ready_orders.txt"
)


with (
    open(
        SOURCE_FILE,
        "r",
        encoding="utf-8"
    ) as source_file,

    open(
        READY_FILE,
        "w",
        encoding="utf-8"
    ) as ready_file
):
    for order_line in source_file:
        if "ready" in order_line.casefold():
            ready_file.write(order_line)

            print(
                "Ready order copied:",
                order_line.strip()
            )


print("Source file closed:", source_file.closed)
print("Ready file closed:", ready_file.closed)