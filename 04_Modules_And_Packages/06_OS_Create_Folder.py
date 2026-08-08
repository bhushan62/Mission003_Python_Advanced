# import os

# os.mkdir("KLYN_Orders")

# print("Folder created successfully")

import os

folder = "KLYN_Orders"

if os.path.exists(folder):
    print("Folder already exists")
else:
    os.mkdir(folder)
    print("Folder created successfully")