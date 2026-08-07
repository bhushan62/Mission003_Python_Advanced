# class InvalidWeightError(Exception):
#     pass


# weight = float(input("Enter Weight : "))

# if weight <= 0:
#     raise InvalidWeightError("Weight cannot be zero or negative.")

# print("Accepted")

#-----------------------------------------------------------------------------------------------------------

# class InvalidWeightError(Exception):
#     pass

# try:

#     weight = float(input("Enter Weight : "))

#     if weight <= 0:
#         raise InvalidWeightError("Weight cannot be zero or negative.")

#     print("Accepted")

# except InvalidWeightError as e:

#     print(e)

#---------------------------------------------------------------------------------------------------------------------------

class InvalidWeightError(Exception):
    pass

try:
    weight = float(input("Enter Weight : "))

    if weight <= 0:
        raise InvalidWeightError("Weight cannot be zero or negative.")

    amount = weight * 100

    print("Amount :", amount)

except InvalidWeightError as e:
    print(e)

    