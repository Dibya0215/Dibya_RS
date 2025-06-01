#swap tuple
# List of tuples
tuples_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Swap elements inside each tuple
swapped_list = []

for t in tuples_list:
    swapped_list.append((t[1], t[0]))

print("Original list:", tuples_list)
print("Swapped list: ", swapped_list)
