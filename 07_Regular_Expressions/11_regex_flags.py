import re

message = "Customer requested DRY CLEANING."

service = re.search(
    r"dry cleaning",
    message
)

if service:
    print("Service found:", service.group())
else:
    print("Service not found")

service = re.search(
    r"dry cleaning",
    message,
    re.IGNORECASE
)

if service:
    print("Service found:", service.group())
else:
    print("Service not found")




message = "Customer selected PREMIUM WASH AND IRON."

service = re.search(
    r"wash and iron|dry cleaning|steam iron",
    message,
    re.IGNORECASE
)

if service:
    print("Selected service:", service.group())
else:
    print("Service not found")

report = """AO12345 Ready
AO33396 Processing
AO98765 Delivered"""

orders = re.findall(
    r"^AO\d{5}",
    report
)

print("Without MULTILINE:", orders)


orders = re.findall(
    r"^AO\d{5}",
    report,
    re.MULTILINE
)

print("With MULTILINE:", orders)

report = """AO12345 Ready
AO33396 Processing
AO98765 Ready
AO45821 Delivered"""


ready_orders = re.findall(
    r"^(AO\d{5})\s+Ready$",
    report,
    re.MULTILINE
)

print("Ready orders:", ready_orders)

ready_lines = re.findall(
    r"^AO\d{5}\s+Ready$",
    report,
    re.MULTILINE
)

print("Ready lines:", ready_lines)