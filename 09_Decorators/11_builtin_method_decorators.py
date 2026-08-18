class LaundryOrder:
    store_name = "KLYN Laundry"

    def __init__(
        self,
        order_id,
        customer,
        quantity,
        price_per_item
    ):
        self.order_id = order_id
        self.customer = customer
        self.quantity = quantity
        self.price_per_item = price_per_item

    def show_order(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Store:", self.store_name)

    @staticmethod
    def validate_order_id(order_id):
        return (
            len(order_id) == 7
            and order_id.startswith("AO")
            and order_id[2:].isdigit()
        )

    @classmethod
    def change_store_name(cls, new_name):
        cls.store_name = new_name

    @property
    def total_amount(self):
        return self.quantity * self.price_per_item


order = LaundryOrder(
    order_id="AO45821",
    customer="Ravi",
    quantity=3,
    price_per_item=85
)

order.show_order()

print("\nSTATIC METHOD")

print(
    "AO45821:",
    LaundryOrder.validate_order_id("AO45821")
)

print(
    "BO12345:",
    LaundryOrder.validate_order_id("BO12345")
)

print(
    "AO1234A:",
    LaundryOrder.validate_order_id("AO1234A")
)


print("\nCLASS METHOD")

LaundryOrder.change_store_name(
    "KLYN Laundry & Dry Cleaning"
)

order.show_order()


print("\nPROPERTY")

print(
    "Total amount: ₹",
    order.total_amount,
    sep=""
)