with open("customer.txt","a+") as file:

    file.write("\nNew Customer")

    file.seek(0)

    print(file.read())