## This is the syntax / structure of using try except else block:
# try:
#     ...
# except ZeroDivisionError:
#     ...

# except ValueError:
#     ...

# else:
#     print("Answer :", result)

# try → Try to execute the code.
# except → Runs only if an error occurs.
# else → Runs only if no error occurs.


try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot Divide by Zero.")

except ValueError:
    print("Please Enter Numbers Only")

else:
    print("Answer : ", result)