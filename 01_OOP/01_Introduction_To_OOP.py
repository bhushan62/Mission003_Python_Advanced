customer_name = "Ravi"
service_type = "Dry Cleaning"
price = 250


def calculate_total(amount):
    return amount


def generate_bill(name, service, amount):
    print("Customer:", name)
    print("Service:", service)
    print("Total:", amount)


total_amount = calculate_total(price)
generate_bill(customer_name, service_type, total_amount)