import random

l1 = [random.randint(1, 10) for _ in range(5)]
l2 = [random.randint(1, 10) for _ in range(5)]

print("L1:", l1)
print("L2:", l2)
print("Union:", l1 + l2)

without = []
for x in l1 + l2:
    if x not in without:
        without.append(x)
print("No repeat:", without)

common = []
for x in l1:
    if x in l2 and x not in common:
        common.append(x)
print("Same:", common)

unique = []
for x in l1 + l2:
    if (x in l1 and x not in l2) or (x in l2 and x not in l1):
        if x not in unique:
            unique.append(x)
print("Different:", unique)

minmax = [min(l1), max(l1), min(l2), max(l2)]
print("Min max:", minmax)