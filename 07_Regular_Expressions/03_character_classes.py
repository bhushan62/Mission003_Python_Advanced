import re

message = "Order 5821 has a total bill of 1450 rupees."

numbers = re.findall(r"\d+", message)                                        # re.findall finds all matching numbers in the message. 

print("Numbers found:", numbers)

message = "Customer Ravi_2026 placed an order."

words = re.findall(r"\w+", message)

print("Words found:", words)                                      #\w+ finds all words that are in the message


message = "Your Order AO3339 is Ready with us."

order = re.search(r"\bAO\d{4}\b", message)

if order:
    print("Order number:", order.group())
else:
    print("Order number not found")