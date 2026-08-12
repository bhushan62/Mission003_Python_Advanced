import re

message = "Customer requested dry cleaning for one saree."

service = re.search(r"wash|iron|dry cleaning", message)

if service:
    print("Service found:", service.group())
else:
    print("Service not found")


order_id = "AO33396"

order = re.search(r"(AO)(\d{5})", order_id)

if order:
    print("Complete match:", order.group())
    print("Prefix:", order.group(1))
    print("Number:", order.group(2))

    message = "Order AO33396 amount ₹1450"

details = re.search(
    r"Order\s+(AO\d{5})\s+amount\s+₹(\d+)",
    message
)

if details:
    print("Complete match:", details.group())
    print("Order ID:", details.group(1))
    print("Amount:", details.group(2))
else:
    print("Order details not found")

messages = [
    "Bill amount ₹1450",
    "Bill amount Rs 1450",
    "Bill amount Rs. 1450"
]

for message in messages:
    result = re.search(r"(?:₹|Rs\.?)\s*(\d+)", message)

    if result:
        print("Amount:", result.group(1))

message = "Pickup scheduled for 25-08-2026."

date = re.search(r"(\d{2})-(\d{2})-(\d{4})", message)

if date:
    print("Complete date:", date.group())
    print("Day:", date.group(1))
    print("Month:", date.group(2))
    print("Year:", date.group(3))

order_text = "AO33396"

order = re.fullmatch(
    r"(?P<prefix>AO)(?P<number>\d{5})",
    order_text
)

if order:
    print("Prefix:", order.group("prefix"))
    print("Number:", order.group("number"))