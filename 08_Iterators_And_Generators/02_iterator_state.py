orders = ["AO12345", "AO33396", "AO45821"]

counter_iterator = iter(orders)
washing_iterator = iter(orders)

print("Counter:", next(counter_iterator))
print("Counter:", next(counter_iterator))

print("Washing:", next(washing_iterator))

print("Counter:", next(counter_iterator))
print("Washing:", next(washing_iterator))

