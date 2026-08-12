import re


# + means one or more

text = "Order amounts are 5, 50, 500 and 5000."

numbers = re.findall(r"\d+", text)

print("Numbers:", numbers)


# * means zero or more

text = "ac abc abbc abbbc"

matches = re.findall(r"ab*c", text)

print("Star matches:", matches)


# ? means zero or one

text = "color colour"

matches = re.findall(r"colou?r", text)

print("Optional-character matches:", matches)


# {n} means exactly n

text = "Codes: 123, 1234, 12345"

matches = re.findall(r"\b\d{4}\b", text)

print("Exactly four digits:", matches)


# {n,} means at least n

text = "Codes: 12 123 1234 12345 123456"

matches = re.findall(r"\b\d{4,}\b", text)

print("Four or more digits:", matches)


# {n,m} means between n and m

text = "Codes: 1 12 123 1234 12345 123456"

matches = re.findall(r"\b\d{2,4}\b", text)

print("Two to four digits:", matches)