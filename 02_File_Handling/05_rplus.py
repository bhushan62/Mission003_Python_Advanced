with open("customer.txt", "r+") as file:
    print(file.read())

    file.write("\nService : Steam Iron")

    file.write("\nSODA")