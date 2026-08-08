from klyn import wash_fold, calculate_gst

amount = wash_fold(10)
gst = calculate_gst(amount)

print("Amount:", amount)
print("GST:", gst)
print("Total:", amount + gst)
