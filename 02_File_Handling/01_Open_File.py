file = open("customers.txt", "w")                         # Create the file if it doesn't exist and write the first customer.

file.write("Name    : Bhushan\n")
file.write("Phone   : 9876543210\n")    
file.write("Service : Dry Cleaning\n")  

file.close()

print("1st Customer saved successfully.")

file = open("customers.txt", "a")                          # # Append another customer to the existing file without deleting previous data.

file.write("Name : Rahul \n")
file.write("Phone : 8008825850 \n")
file.write("Service : Wash & Iron \n")

file.close()

print("2nd Customer saved successfully.")

