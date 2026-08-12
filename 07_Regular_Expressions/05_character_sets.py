import re

text = "cat bat rat mat"

matches = re.findall(r"[cb]at", text)

print("Matches:", matches)

text = "KLYN Laundry 2026"

uppercase = re.findall(r"[A-Z]", text)       #only taking uppercase letters. if there is lowercase letter next to uppercase letter code stops there.
lowercase = re.findall(r"[a-z]", text)       #only taking lowercase letters. if there is uppercase letter before lowercase letter code stops after leaving uppercase letter.

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)


uppercase_words = re.findall(r"[A-Z]+", text)
lowercase_words = re.findall(r"[a-z]+", text)
numbers = re.findall(r"[0-9]+", text)                          

print("Uppercase groups:", uppercase_words)
print("Lowercase groups:", lowercase_words)
print("Number groups:", numbers)


order_id = "AO33396"

characters = re.findall(r"[A-Z0-9]+", order_id)                   #it is taking combined A-Z and 0-9 

print("Order ID:", characters)


order = re.search(r"\bAO[0-9]{5}\b", order_id)

if order:
    print("Valid format:", order.group())

    message = "Contact Ravi at 9876543210."

phone = re.search(r"\b[6-9]\d{9}\b", message)

if phone:
    print("Phone number:", phone.group())
else:
    print("Valid phone number not found")

invoice = "KLYN-2026-AO33396"

non_digits = re.findall(r"[^0-9]", invoice)

print("Non-digits:", non_digits)