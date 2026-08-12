import re


order_message = """
ORDER START
Order ID: AO45821
Customer: Ravi Kumar
Phone: +91-98765 43210
Service: Dry Cleaning
Items: 3 Shirts, 2 Trousers, 1 Saree
Amount: Rs. 1750
Status: READY
ORDER END
"""


# Reusable compiled patterns

ORDER_PATTERN = re.compile(r"AO\d{5}")

PHONE_PATTERN = re.compile(r"[6-9]\d{9}")

SERVICE_PATTERN = re.compile(
    r"wash and iron|dry cleaning|steam iron|wash and fold",
    re.IGNORECASE
)

ITEM_PATTERN = re.compile(
    r"(\d+)\s+([A-Za-z]+)"
)

AMOUNT_PATTERN = re.compile(
    r"(?:₹|Rs\.?)\s*(\d+)"
)

STATUS_PATTERN = re.compile(
    r"ready|processing|delivered|pending",
    re.IGNORECASE
)


# Extract everything inside the order block

order_block = re.search(
    r"ORDER START\s*(.*?)\s*ORDER END",
    order_message,
    re.DOTALL
)

if not order_block:
    print("Order block not found")
    raise SystemExit

order_text = order_block.group(1)

print("Order block found")


# Extract individual lines

order_match = re.search(
    r"Order ID:\s*(AO\d{5})",
    order_text
)

customer_match = re.search(
    r"Customer:\s*([A-Za-z ]+)",
    order_text
)

phone_line = re.search(
    r"Phone:\s*(.+)",
    order_text
)

service_match = re.search(
    r"Service:\s*(.+)",
    order_text
)

items_line = re.search(
    r"Items:\s*(.+)",
    order_text
)

amount_line = re.search(
    r"Amount:\s*(.+)",
    order_text
)

status_match = re.search(
    r"Status:\s*(\w+)",
    order_text
)


# Extract and validate order ID

order_id = (
    order_match.group(1)
    if order_match
    else ""
)

order_is_valid = bool(
    ORDER_PATTERN.fullmatch(order_id)
)


# Extract customer name

customer = (
    customer_match.group(1).strip()
    if customer_match
    else ""
)


# Clean and validate phone number

phone = ""

if phone_line:
    phone = re.sub(
        r"[^0-9]",
        "",
        phone_line.group(1)
    )

    if len(phone) == 12 and phone.startswith("91"):
        phone = phone[2:]

phone_is_valid = bool(
    PHONE_PATTERN.fullmatch(phone)
)


# Extract and validate service

service = (
    service_match.group(1).strip()
    if service_match
    else ""
)

service_is_valid = bool(
    SERVICE_PATTERN.fullmatch(service)
)


# Extract garments and quantities

garments = []
total_garments = 0

if items_line:
    items = ITEM_PATTERN.finditer(
        items_line.group(1)
    )

    for item in items:
        quantity = int(item.group(1))
        garment = item.group(2)

        garments.append({
            "garment": garment,
            "quantity": quantity
        })

        total_garments += quantity


# Extract amount

amount = 0

if amount_line:
    amount_match = AMOUNT_PATTERN.search(
        amount_line.group(1)
    )

    if amount_match:
        amount = int(amount_match.group(1))


# Extract and validate status

status = (
    status_match.group(1).strip()
    if status_match
    else ""
)

status_is_valid = bool(
    STATUS_PATTERN.fullmatch(status)
)


# Create structured order dictionary

order = {
    "order_id": order_id if order_is_valid else None,
    "customer": customer or None,
    "phone": phone if phone_is_valid else None,
    "service": (
        service.title()
        if service_is_valid
        else None
    ),
    "garments": garments,
    "total_garments": total_garments,
    "amount": amount,
    "status": (
        status.title()
        if status_is_valid
        else "Unknown"
    )
}


# Display processed order

print("\nPROCESSED LAUNDRY ORDER")
print("-" * 35)

print("Order ID:", order["order_id"])
print("Customer:", order["customer"])
print("Phone:", order["phone"])
print("Service:", order["service"])
print("Status:", order["status"])
print("Total garments:", order["total_garments"])
print("Bill amount: ₹", order["amount"], sep="")

print("\nGARMENTS")

for item in order["garments"]:
    print(
        "-",
        item["quantity"],
        item["garment"]
    )