from contextlib import contextmanager
from pathlib import Path


@contextmanager
def open_laundry_report(file_name, mode):
    file_path = Path(__file__).with_name(file_name)

    print("Opening laundry report")

    report_file = open(
        file_path,
        mode,
        encoding="utf-8"
    )

    try:
        # This value is provided after "as"
        yield report_file

    finally:
        # This always runs during cleanup
        report_file.close()
        print("Closing laundry report")


with open_laundry_report(
    "laundry_report.txt",
    "w"
) as report:
    report.write("AO45821 | Ravi | Ready\n")
    report.write("AO33396 | Suresh | Processing\n")


print("Is report closed?", report.closed)

