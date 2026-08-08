# from klyn.laundry import wash_fold

# amount = wash_fold(5)

# print(amount)

from klyn.laundry import wash_fold
from klyn.billing import calculate_gst

amount = wash_fold(5)
gst = calculate_gst(amount)

print("Laundry Amount:", amount)
print("GST:", gst)
print("Total:", amount + gst)