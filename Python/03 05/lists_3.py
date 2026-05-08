import random

lst = [random.randint(-10, 10) for _ in range(10)]
print("List:", lst)
print()

neg = 0
for x in lst:
    if x < 0:
        neg += x
print("Negative:", neg)

par = 0
for x in lst:
    if x % 2 == 0:
        par += x
print("Even:", par)

nepar = 0
for x in lst:
    if x % 2 != 0:
        nepar += x
print("Odd:", nepar)

prod = 1
for i in range(len(lst)):
    if i % 3 == 0:
        prod *= lst[i]
print("Product index 3:", prod)

min_i = lst.index(min(lst))
max_i = lst.index(max(lst))
if min_i > max_i:
    min_i, max_i = max_i, min_i
prod2 = 1
for i in range(min_i + 1, max_i):
    prod2 *= lst[i]
print("Product between:", prod2)

first_p = -1
last_p = -1
for i in range(len(lst)):
    if lst[i] > 0:
        if first_p == -1:
            first_p = i
        last_p = i

if first_p != -1 and last_p != -1 and first_p < last_p:
    sum_bet = 0
    for i in range(first_p + 1, last_p):
        sum_bet += lst[i]
    print("Sum between positive:", sum_bet)
else:
    print("Sum between positive:", 0)
