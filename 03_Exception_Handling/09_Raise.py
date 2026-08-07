# age = int(input("Enter Age : "))

# if age < 18:
#     raise Exception("Age must be 18 or above.")

# print("Welcome")



salary = int(input("Enter Salary : "))

if salary < 5000:
    raise Exception("Salary is too low to tax.")

elif salary > 25000:
    raise Exception("Salary is high and must be taxed.")

else:
    print("Employee is eligible for Tax Exemption")