import re


# \s matches whitespace

customer_name = "Ravi     Kumar"

spaces = re.findall(r"\s+", customer_name)

print("Whitespace found:", spaces)

if spaces:
    print("Number of spaces:", len(spaces[0]))
else:
    print("No spaces found")


# Replace multiple spaces with one space

clean_name = re.sub(r"\s+", " ", customer_name)

print("Original name:", customer_name)
print("Clean name:", clean_name)


# \S matches non-whitespace characters

message = "KLYN Laundry"

characters = re.findall(r"\S", message)
words = re.findall(r"\S+", message)

print("Non-whitespace characters:", characters)
print("Non-whitespace groups:", words)


# Dot matches almost any one character

text = "cat cut cot c9t c@t"

matches = re.findall(r"c.t", text)

print("Dot matches:", matches)


# \. matches an actual dot

email = "customer@gmail.com"

domain = re.search(r"gmail\.com", email)

if domain:
    print("Domain found:", domain.group())
else:
    print("Domain not found")

address =  "12-5-30,   Powerpet,      Eluru"

re.sub(r"\s+", " ", address)


clean_name = re.sub(r"\s+", " ", address)

print("Clean name:", clean_name)
