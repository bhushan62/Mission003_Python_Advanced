from contextlib import ExitStack
from pathlib import Path


FOLDER = Path(__file__).parent

ORDER_FILES = [
    FOLDER / "08.morning_orders.txt",
    FOLDER / "08.afternoon_orders.txt",
    FOLDER / "08.evening_orders.txt"
]

COMBINED_FILE = FOLDER / "08.combined_orders.txt"


# Create practice order files
ORDER_FILES[0].write_text(
    "AO10001 | Ravi | Ready\n",
    encoding="utf-8"
)

ORDER_FILES[1].write_text(
    "AO10002 | Suresh | Processing\n",
    encoding="utf-8"
)

ORDER_FILES[2].write_text(
    "AO10003 | Anjali | Ready\n",
    encoding="utf-8"
)


with ExitStack() as stack:
    opened_files = []

    # Open any number of input files
    for file_path in ORDER_FILES:
        order_file = stack.enter_context(
            open(
                file_path,
                "r",
                encoding="utf-8"
            )
        )

        opened_files.append(order_file)

    # Open the output file
    combined_file = stack.enter_context(
        open(
            COMBINED_FILE,
            "w",
            encoding="utf-8"
        )
    )

    # Combine the contents
    for order_file in opened_files:
        for order_line in order_file:
            combined_file.write(order_line)

            print(
                "Order combined:",
                order_line.strip()
            )


print(
    "All input files closed:",
    all(file.closed for file in opened_files)
)

print(
    "Combined file closed:",
    combined_file.closed
)