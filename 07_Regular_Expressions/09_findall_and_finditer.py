import re


message = "Orders AO12345, AO33396 and AO98765 are ready."


# findall returns all matches as a list

orders = re.findall(r"\bAO\d{5}\b", message)

print("Using findall:", orders)


# finditer returns match objects one at a time

orders = re.finditer(r"\bAO\d{5}\b", message)

for order in orders:
    print(
        "Order:", order.group(),
        "| Start:", order.start(),
        "| End:", order.end(),
        "| Span:", order.span()
    )
                                                  
order_data = """
Order AO12345 Amount ₹500
Order AO33396 Amount ₹1450
Order AO98765 Amount ₹800
"""
 
details = re.finditer(
    r"Order\s+(AO\d{5})\s+Amount\s+₹(\d+)",
    order_data
)

total = 0

for detail in details:
    order_id = detail.group(1)
    amount = int(detail.group(2))

    total += amount

    print("Order:", order_id, "| Amount:", amount)

print("Total amount:", total)
