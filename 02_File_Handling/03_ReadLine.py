# file = open("customers.txt", "r")

# line1 = file.readline()

# print(line1)

# file.close()

# file = open("customers.txt", "r")

# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()

# print(line1)
# print(line2)
# print(line3)

# file.close()


file = open("customer.txt", "w")

file.write("Name    :  suneetha   \n")
file.write("Email   :  suneetha.62@gmail.com  \n")
file.write("Address :  Eluru  \n")

file.close()

print("New Data Updated  \n")


file = open("customer.txt", "r")

data = file.read()

print(type(data))

print(data)

file.close()


file = open("customer.txt", "r")

line2 = file.readline()

print(line2)

file.close()


file = open("customer.txt", "r")

readlines = file.readlines()

print(readlines)

file.close()