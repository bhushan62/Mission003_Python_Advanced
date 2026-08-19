from pathlib import Path


FILE_PATH = Path(__file__).with_name(
    "daily_orders.txt"
)


with open(
    FILE_PATH,
    "w",
    encoding="utf-8"
) as file:
    file.write("AO45821 | Ravi | Ready\n")
    file.write("AO33396 | Suresh | Processing\n")


print("Is file closed?", file.closed)