# import re
# customer_message = """
# Hello, my KLYN order number is 472815.
# Please tell me when it will be delivered.
# """

# pattern = r"\d{6}"

# result = re.search(pattern, customer_message)

# if result:
#     print("Order number:", result.group())
# else:
#     print("Order number not found")


import re

customer_message = """
Hello, Your order number 3339 is ready with us.
Please Collect your order.
Fabo Laundry & Dry Cleaning
"""
pattern = r"\d{4}"

result = re.search(pattern, customer_message)

if result:
    print("Order number:", result.group())
else:
    print("Order number not found")