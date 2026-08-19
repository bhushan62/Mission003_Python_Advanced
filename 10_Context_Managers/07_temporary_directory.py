from pathlib import Path
from tempfile import TemporaryDirectory


print("Starting temporary processing")


with TemporaryDirectory() as temporary_directory:
    temporary_path = Path(temporary_directory)

    report_path = temporary_path / "processed_orders.txt"

    report_path.write_text(
        "AO45821 | Ravi | Ready\n"
        "AO33396 | Suresh | Processing\n",
        encoding="utf-8"
    )

    print(
        "Temporary folder:",
        temporary_path
    )

    print(
        "File exists inside with block:",
        report_path.exists()
    )

    print("\nFILE CONTENT")

    print(
        report_path.read_text(
            encoding="utf-8"
        )
    )


print(
    "Folder exists after with block:",
    temporary_path.exists()
)

print("Temporary processing completed")