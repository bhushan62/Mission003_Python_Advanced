# try:
#     num1 = int(input("Enter First Number : "))
#     num2 = int(input("Enter Second Number : "))

#     result = num1 / num2

#     print("Answer :", result)

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# except ValueError:
#     print("Please enter number only.")

try:
    weight = float(input("Enter Weight (kg): "))

    RATE_PER_KG = 100

    total_amount = weight * RATE_PER_KG

    print("-------------------------")
    print("Service : Wash & Fold")
    print("Weight  :", weight, "kg")
    print("Rate    : ₹", RATE_PER_KG, "/kg")
    print("Total   : ₹", total_amount)
    print("-------------------------")

except ValueError:
    print("Please enter a valid weight.")