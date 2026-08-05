# class Customer:
#     pass


# customer1 = Customer()
# customer2 = Customer()

# print(customer1)
# print(customer2)

# print(type(customer1))
# print(type(customer2))

class Customer:

    def __init__(self, name, phone, service):
        self.name = name
        self.phone = phone
        self.service = service

    def display(self):
        print(f"Name    : {self.name}")
        print(f"Phone   : {self.phone}")
        print(f"Service : {self.service}")


customer1 = Customer("Bhushan", "9876543210", "Dry Cleaning")
customer2 = Customer("Rahul", "9123456789", "Wash & Fold")

customer1.display()
customer2.display()