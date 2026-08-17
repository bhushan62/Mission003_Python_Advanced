def generate_orders(orders):
    yield from orders


order_ids = ["AO12345", "AO33396", "AO45821"]

for order_id in generate_orders(order_ids):
    print(order_id)


def generate_all_orders(counter_orders, online_orders):
    yield from counter_orders
    yield from online_orders


counter_orders = [
    "AO12345",
    "AO33396"
]

online_orders = [
    "AO45821",
    "AO98765"
]

all_orders = generate_all_orders(
    counter_orders,
    online_orders
)

for order_id in all_orders:
    print("Order:", order_id)

def generate_ready_orders():
    yield "AO12345"
    yield "AO45821"


def generate_processing_orders():
    yield "AO33396"
    yield "AO98765"


def generate_all_active_orders():
    yield from generate_ready_orders()
    yield from generate_processing_orders()


for order_id in generate_all_active_orders():
    print("Active order:", order_id)


def generate_counter_orders():
    yield {
        "order_id": "AO11111",
        "source": "Counter"
    }

    yield {
        "order_id": "AO22222",
        "source": "Counter"
    }


def generate_online_orders():
    yield {
        "order_id": "AO33333",
        "source": "Website"
    }

    yield {
        "order_id": "AO44444",
        "source": "WhatsApp"
    }


def generate_whatsapp_orders():
    yield {
        "order_id": "AO34433",
        "source": "Website"
    }

    yield {
        "order_id": "AO65444",
        "source": "WhatsApp"
    }


def generate_all_orders():
    yield from generate_counter_orders()
    yield from generate_online_orders()
    yield from generate_whatsapp_orders()


for order in generate_all_orders():
    print(
        order["order_id"],
        "| Source:",
        order["source"]
    )


def generate_value():
    yield from "KLYN"


for value in generate_value():
    print(value)


def generate_all_orders():
    yield from generate_counter_orders()
    yield from generate_online_orders()
    yield from generate_whatsapp_orders()


for order in generate_all_orders():
    print(
        order["order_id"],
        "| Source:",
        order["source"]
    )


def generate_value():
    yield from "KLYN"


for value in generate_value():
    print(value)