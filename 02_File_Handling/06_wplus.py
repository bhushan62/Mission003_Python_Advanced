with open("customer.txt","w+") as file:
    file.write("SODA")

    file.seek(0)

    print(file.read())