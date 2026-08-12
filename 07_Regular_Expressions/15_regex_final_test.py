import re


print("=" * 50)
print("QUESTION 1: EXTRACT VALID ORDER IDs")
print("=" * 50)

message = """
AO12345 is ready.
AO45821 is processing.
Invalid order AO1234.
AO98765 is delivered.
"""

orders = re.findall(
    r"\bAO\d{5}\b",
    message
)

print("Valid orders:", orders)


print("\n" + "=" * 50)
print("QUESTION 2: VALIDATE PHONE NUMBERS")
print("=" * 50)

phones = [
    "9876543210",
    "5123456789",
    "8123456789",
    "987654321",
    "98A6543210"
]

phone_pattern = re.compile(
    r"[6-9]\d{9}"
)

for phone in phones:
    if phone_pattern.fullmatch(phone):
        print(phone, "→ Valid")
    else:
        print(phone, "→ Invalid")


print("\n" + "=" * 50)
print("QUESTION 3: CLEAN CUSTOMER NAME")
print("=" * 50)

customer = "   Ravi      Kumar   "

clean_customer = re.sub(
    r"\s+",
    " ",
    customer
).strip()

print("Original:", repr(customer))
print("Cleaned:", clean_customer)


print("\n" + "=" * 50)
print("QUESTION 4: CLEAN AND VALIDATE PHONE")
print("=" * 50)

phone = "+91-98765 43210"

# Remove everything except digits

clean_phone = re.sub(
    r"[^0-9]",
    "",
    phone
)

# Remove Indian country code

if (
    len(clean_phone) == 12
    and clean_phone.startswith("91")
):
    clean_phone = clean_phone[2:]

# Validate the cleaned number

if re.fullmatch(r"[6-9]\d{9}", clean_phone):
    print("Valid phone:", clean_phone)
else:
    print("Invalid phone number")


print("\n" + "=" * 50)
print("QUESTION 5: EXTRACT GARMENTS")
print("=" * 50)

order = "4 Shirts, 2 Trousers, 1 Saree, 3 Bedsheets"

item_pattern = re.compile(
    r"(\d+)\s+([A-Za-z]+)"
)

items = item_pattern.finditer(order)

total_garments = 0

for item in items:
    quantity = int(item.group(1))
    garment = item.group(2)

    total_garments += quantity

    print(f"{garment}: {quantity}")

print("Total garments:", total_garments)


print("\n" + "=" * 50)
print("QUESTION 6: EXTRACT ORDER AND AMOUNT")
print("=" * 50)

message = "Order AO45821 has a total bill of Rs. 1750"

details = re.search(
    r"Order\s+(AO\d{5}).*?"
    r"(?:₹|Rs\.?)\s*(\d+)",
    message,
    re.IGNORECASE
)

if details:
    order_id = details.group(1)
    amount = int(details.group(2))

    print("Order:", order_id)
    print("Amount:", amount)
else:
    print("Order details not found")


print("\n" + "=" * 50)
print("QUESTION 7: SPLIT CUSTOMER DATA")
print("=" * 50)

record = (
    "Ravi Kumar | 9876543210 ; "
    "Eluru, Dry Cleaning"
)

customer_parts = re.split(
    r"\s*[|;,]\s*",
    record
)

if len(customer_parts) == 4:
    name = customer_parts[0]
    phone = customer_parts[1]
    city = customer_parts[2]
    service = customer_parts[3]

    print("Name:", name)
    print("Phone:", phone)
    print("City:", city)
    print("Service:", service)
else:
    print("Invalid customer record")


print("\n" + "=" * 50)
print("QUESTION 8: CASE-INSENSITIVE SERVICE")
print("=" * 50)

message = "Customer selected PREMIUM DRY CLEANING."

service_pattern = re.compile(
    r"wash and iron|dry cleaning|"
    r"steam iron|wash and fold",
    re.IGNORECASE
)

service = service_pattern.search(message)

if service:
    print("Service found:", service.group())
else:
    print("Supported service not found")


print("\n" + "=" * 50)
print("QUESTION 9: READY ORDERS")
print("=" * 50)

report = """AO12345 Ready
AO45821 Processing
AO98765 Ready
AO33396 Delivered"""

ready_orders = re.findall(
    r"^(AO\d{5})\s+Ready$",
    report,
    re.MULTILINE | re.IGNORECASE
)

print("Ready orders:", ready_orders)


print("\n" + "=" * 50)
print("QUESTION 10: NON-GREEDY EXTRACTION")
print("=" * 50)

text = """
<customer>Ravi Kumar</customer>
<customer>Suresh Babu</customer>
"""

customers = re.findall(
    r"<customer>\s*(.*?)\s*</customer>",
    text,
    re.DOTALL
)

print("Customers:", customers)


print("\n" + "=" * 50)
print("BONUS: MASK PHONE NUMBER")
print("=" * 50)

phone = "9876543210"

masked_phone = re.sub(
    r"^[6-9]\d{5}(\d{4})$",
    r"******\1",
    phone
)

print("Original phone:", phone)
print("Masked phone:", masked_phone)