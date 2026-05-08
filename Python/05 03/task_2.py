import random

l1 = [random.randint(1, 10) for _ in range(5)]
l2 = [random.randint(1, 10) for _ in range(5)]

print("L1:", l1)
print("L2:", l2)
print()

print("All:", l1 + l2)

no_repeat = []
for x in l1 + l2:
    if x not in no_repeat:
        no_repeat.append(x)
print("No repeat:", no_repeat)

same = []
for x in l1:
    if x in l2 and x not in same:
        same.append(x)
print("Same:", same)

unique = []
for x in l1 + l2:
    if (x in l1 and x not in l2) or (x in l2 and x not in l1):
        if x not in unique:
            unique.append(x)
print("Different:", unique)

print("Min max:", [min(l1), max(l1), min(l2), max(l2)])
