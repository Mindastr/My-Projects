import random

lst = [random.randint(-10, 10) for _ in range(10)]
print("List:", lst)
print()

even = []
for x in lst:
    if x % 2 == 0:
        even.append(x)
print("Even:", even)

odd = []
for x in lst:
    if x % 2 != 0:
        odd.append(x)
print("Odd:", odd)

negative = []
for x in lst:
    if x < 0:
        negative.append(x)
print("Negative:", negative)

positive = []
for x in lst:
    if x > 0:
        positive.append(x)
print("Positive:", positive)
