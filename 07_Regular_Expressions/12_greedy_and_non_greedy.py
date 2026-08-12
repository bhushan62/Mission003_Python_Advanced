import re 

text = "<order>AO12345</order><order>AO33396</order>"
result = re.findall( r"<order>.*</order>", text ) 
print("Greedy result:", result)

result = re.findall(
    r"<order>.*?</order>",
    text
)

print("Non-greedy result:", result)

orders = re.findall(
    r"<order>(.*?)</order>",
    text
)

print("Order IDs:", orders)