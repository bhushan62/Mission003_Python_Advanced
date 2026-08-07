# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))

# try:
#     result = num1 / num2
#     print("Answer :", result)

# except:
#     print("Cannot divide by zero.")

try:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))

    result = num1 / num2

    print("Answer :", result)

except:
    print("Invalid input or division by zero.")