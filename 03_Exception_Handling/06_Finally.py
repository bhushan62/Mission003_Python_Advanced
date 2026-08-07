# try:
#     num1 = int(input("Enter First Number : "))
#     num2 = int(input("Enter Second Number : "))

#     result = num1 / num2

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# except ValueError:
#     print("Please enter valid numbers.")

# else:
#     print("Answer :", result)

# finally:
#     print("Program Finished.")

try:
    file = open("customers.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    file.close()
    print("File Closed.")