import re

phone_pattern = re.compile(r"[6-9]\d{9}")

phones = [
    "9876543210",
    "8123456789",
    "5123456789",
    "987654321",
    "98A6543210"
]

for phone in phones:
    if phone_pattern.fullmatch(phone):
        print(phone, "→ Valid")
    else:
        print(phone, "→ Invalid")


order_pattern = re.compile(r"\bAO\d{5}\b")

messages = [
    "Order AO12345 is ready.",
    "AO33396 is processing.",
    "Invalid order AO1234.",
    "Orders AO45821 and AO98765 are delivered."
]

for message in messages:
    orders = order_pattern.findall(message)
    print("Message:", message)
    print("Orders:", orders)

service_pattern = re.compile(
    r"wash and iron|dry cleaning|steam iron",
    re.IGNORECASE
)

messages = [
    "Customer selected DRY CLEANING.",
    "Customer selected Wash and Iron.",
    "Customer selected steam iron.",
    "Customer selected shoe cleaning."
]

for message in messages:
    service = service_pattern.search(message)

    if service:
        print("Service:", service.group())
    else:
        print("Supported service not found")

space_pattern = re.compile(r"\s+")

message = "Customer      Ravi    ordered  3 shirts."

clean_message = space_pattern.sub(" ", message)

print(clean_message)