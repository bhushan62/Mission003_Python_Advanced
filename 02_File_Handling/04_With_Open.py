# with open("customer.txt", "r") as file:
#     data = file.read()
#     print(data)


# with open("customers.txt", "r") as file:
#     data = file.read()
#     print(data)

file = open("customer.txt", "a")
file.write("Name    : SODA \n")
file.write("Phone   : 8185075896 \n")
file.write("Service : Dry Cleaning \n")

file.close()

print("Customer updated \n")

with open("customer.txt", "r") as file:
    data = file.read()
    print(data)