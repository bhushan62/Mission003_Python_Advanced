import re

message = "Customer requested DRY CLEANING."

service = re.search(r"dry cleaning", message)

print(service)

customer_name = "Ravi       Kumar"

clean_name = re.sub(r"\s+", " ", customer_name)

print("Original:", customer_name)
print("Cleaned:", clean_name)

phone = "+91-98765 43210"

clean_phone = re.sub(r"[^0-9]", "", phone)                #Here, ^ inside [ ] means NOT. So [^0-9] matches everything that is not a digit. re.sub() then replaces those matches with "", which removes them.


print("Clean phone:", clean_phone)

if len(clean_phone) == 12 and clean_phone.startswith("91"):      # Here 91 country code is removed 
    clean_phone = clean_phone[2:]

print("Mobile number:", clean_phone)


#Masking numbers
phone = "9876543210"

masked_phone = re.sub(
    r"^[6-9]\d{5}(\d{4})$",
    r"******\1",
    phone
)

print("Original phone:", phone)
print("Masked phone:", masked_phone)

message = "Customer selected Wash and Iron service."


updated_message = re.sub(
    r"Wash and Iron",
    "Premium Wash & Iron",
    message
)

print(updated_message)


message = "urgent urgent urgent"

result = re.sub(r"urgent", "priority", message)

print(result)

result = re.sub(
    r"urgent",
    "priority",
    message,
    count=1
)

print(result)


order_id = "AO33396"

formatted_order = re.sub(
    r"^(AO)(\d{5})$",
    r"\1-\2",
    order_id
)

print("Formatted order:", formatted_order)



message = "  Customer    Ravi   ordered    3    shirts.  "

clean_message = re.sub(r"\s+", " ", message).strip()

print("Clean message:", clean_message)

services = "Wash,Iron,Dry Cleaning,Steam Iron"

service_list = re.split(r",", services)

print("Services:", service_list)

services = "Wash,Iron;Dry Cleaning|Steam Iron"

service_list = re.split(r"[,;|]", services)

print("Services:", service_list)

services = "Wash, Iron ; Dry Cleaning | Steam Iron"

service_list = re.split(r"\s*[,;|]\s*", services)

print("Clean services:", service_list)


customer_data = "Ravi Kumar | 9876543210 | Eluru | Dry Cleaning"

customer = re.split(r"\s*\|\s*", customer_data)

print("Name:", customer[0])
print("Phone:", customer[1])
print("City:", customer[2])
print("Service:", customer[3])

[
    "Ravi Kumar",
    "9876543210",
    "Eluru",
    "Dry Cleaning"
]

order_note = "AO33396:Shirt:Oil stain:Urgent delivery"

parts = re.split(r":", order_note, maxsplit=2)

print("Limited split:", parts)

parts = re.split(r":", order_note)


customer_record = (
    "  Ravi Kumar , +91-98765 43210 ; "
    "Eluru | Dry Cleaning  "
)

customer_record = customer_record.strip()

parts = re.split(r"\s*[,;|]\s*", customer_record)

name = parts[0]
phone = re.sub(r"[^0-9]", "", parts[1])
city = parts[2]
service = parts[3]

if len(phone) == 12 and phone.startswith("91"):
    phone = phone[2:]

print("Customer name:", name)
print("Phone:", phone)
print("City:", city)
print("Service:", service)


customer_record = customer_record.strip()

parts = re.split(r"\s*[,;|]\s*", customer_record)

name = parts[0]
phone = re.sub(r"[^0-9]", "", parts[1])
city = parts[2]
service = parts[3]

if len(phone) == 12 and phone.startswith("91"):
    phone = phone[2:]

print("Customer name:", name)
print("Phone:", phone)
print("City:", city)
print("Service:", service)


order_record = "AO45821 | 3 Shirts ; 2 Trousers, ₹1250"


parts = re.split(r"\s*[|;,]\s*", order_record)
print(parts)


