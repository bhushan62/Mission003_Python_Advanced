# import math

# number = math.sqrt(100)

# print(number)
# print(math.ceil(10.2))
# print(math.floor(10.8))
# print(math.pi)


# import random

# number = random.randint(1, 10)

# print(number)

#--------------------------   random ---------------------#

# import random

# services = ["Wash & Fold", "Wash & Iron", "Dry Cleaning", "Steam Iron"]

# selected_service = random.choice(services)

# print(selected_service)

# random.shuffle(services)

# print(services)

#----------------------------  Date & Time --------------#

import datetime

now = datetime.datetime.now()

print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)

formatted_date = now.strftime("%d-%m-%Y")                    # formatted date as required

print(formatted_date)

full_date = now.strftime("%d %B %Y")                        # full date 
print(full_date)

current_time = now.strftime("%I:%M %p")                     # full time with am / pm

print(current_time)


full_date_time = now.strftime("%d %B %Y - %I:%M %p")

print(full_date_time)