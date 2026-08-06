with open("customer.txt", "r") as file:

    print(file.read(4))

    file.seek(0)

    print(file.read(4))