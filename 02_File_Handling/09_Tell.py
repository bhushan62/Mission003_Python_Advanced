with open("customer.txt", "r") as file:

    print(file.tell())

    data = file.read(4)

    print(data)

    print(file.tell())