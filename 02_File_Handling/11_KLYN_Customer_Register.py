while True:

    print("\n==============================")
    print("     KLYN CUSTOMER REGISTER")
    print("==============================")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\n----- Add Customer -----")

        name = input("Enter Name    : ")
        phone = input("Enter Phone   : ")
        service = input("Enter Service : ")

        with open("customers.txt", "a") as file:

            file.write("\n------------------------------\n")
            file.write(f"Name    : {name}\n")
            file.write(f"Phone   : {phone}\n")
            file.write(f"Service : {service}\n")

        print("\nCustomer Saved Successfully.")

    elif choice == "2":

        print("\n----- Customer List -----\n")

        with open("customers.txt", "r") as file:

            data = file.read()

        print(data)

    elif choice == "3":

        print("\nProgram Closed.")
        break

    else:

        print("\nInvalid Choice. Please Try Again.")