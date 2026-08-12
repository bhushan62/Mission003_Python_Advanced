# import re

# message = "Please call the customer at 9876543210."

# pattern = r"\d{10}"

# result = re.search(pattern, message)

# print(result)

# print(result.group())


# import re 

# message = "Please Call at 8008013930"

# pattern = r"\d{10}"

# result = re.search(pattern, message)

# print(result)

# print(result.group())


import re

message = "Please call the customer tomorrow."

pattern = r"\d{10}"

result = re.search(pattern, message)

if result:
    print("Phone number found:", result.group())
else:
    print("Phone number not found")