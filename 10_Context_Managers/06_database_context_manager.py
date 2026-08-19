import sqlite3
from contextlib import contextmanager
from pathlib import Path


DATABASE_PATH = Path(__file__).with_name(
    "klyn_orders.db"
)


@contextmanager
def database_transaction():
    print("Opening database connection")

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        yield connection

        connection.commit()
        print("Transaction committed")

    except Exception:
        connection.rollback()
        print("Transaction rolled back")

        # Send the error to the outer except block
        raise

    finally:
        connection.close()
        print("Database connection closed")


# Successful transaction
with database_transaction() as database:
    database.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer TEXT,
            status TEXT,
            amount REAL
        )
        """
    )

    # Keeps the practice output consistent on every run
    database.execute("DELETE FROM orders")

    database.execute(
        """
        INSERT INTO orders
        (order_id, customer, status, amount)
        VALUES (?, ?, ?, ?)
        """,
        ("AO45821", "Ravi", "Ready", 1750)
    )


# Failed transaction demonstration
try:
    with database_transaction() as database:
        database.execute(
            """
            INSERT INTO orders
            (order_id, customer, status, amount)
            VALUES (?, ?, ?, ?)
            """,
            ("AO33396", "Suresh", "Processing", 1200)
        )

        # Intentionally cause an error
        result = 10 / 0

except ZeroDivisionError:
    print("Order AO33396 was not saved")


# Read the final database contents
with database_transaction() as database:
    saved_orders = database.execute(
        """
        SELECT order_id, customer, status, amount
        FROM orders
        """
    ).fetchall()


print("\nSAVED ORDERS")

for order in saved_orders:
    print(order)