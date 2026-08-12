import re


# ^ checks the beginning

message = "KLYN Laundry is in Eluru."

start_match = re.search(r"^KLYN", message)

if start_match:
    print("Message starts with KLYN")
else:
    print("Message does not start with KLYN")


# $ checks the end

message = "Welcome to KLYN"

end_match = re.search(r"KLYN$", message)

if end_match:
    print("Message ends with KLYN")
else:
    print("Message does not end with KLYN")


# Both anchors validate the entire structure

order_id = "AO33396"

order = re.search(r"^AO\d{5}$", order_id)

if order:
    print("Valid order ID:", order.group())
else:
    print("Invalid order ID")


# fullmatch is clearer for complete validation

phone = "9876543210"

phone_match = re.fullmatch(r"[6-9]\d{9}", phone)

if phone_match:
    print("Valid phone:", phone_match.group())
else:
    print("Invalid phone")


# Validate Indian pincode

pincode = "534002"

pincode_match = re.fullmatch(r"[1-9]\d{5}", pincode)

if pincode_match:
    print("Valid pincode:", pincode_match.group())
else:
    print("Invalid pincode")