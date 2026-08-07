print("=================================")
print("          KLYN LAUNDRY")
print("=================================")

customer_name = input("Enter Customer Name : ")

print("\n1. Wash & Fold")
print("2. Wash & Iron")

try:
    choice = int(input("\nEnter Service : "))
    weight = float(input("Enter Weight (kg) : "))

    if choice == 1:
        service = "Wash & Fold"
        rate = 100
        amount = weight * rate

    elif choice == 2:
        service = "Wash & Iron"
        rate = 150
        amount = weight * rate

    else:
        print("\nInvalid Service.")
        amount = None

except ValueError:
    print("\nPlease enter valid numbers.")

else:
    if amount is not None:
        print("\n==============================")
        print("          KLYN BILL")
        print("==============================")
        print(f"Customer : {customer_name}")
        print(f"Service  : {service}")
        print(f"Weight   : {weight} kg")
        print(f"Rate     : ₹{rate}/kg")
        print("------------------------------")
        print(f"Total    : ₹{amount}")
        print("==============================")

finally:
    print("\nThank you for choosing KLYN Laundry.")
    print("Visit Again!")