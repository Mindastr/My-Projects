n = int(input())
if n <= 36:
    print("Купе")
else:
    print("Бічне")
if n % 2 == 0:
    print("Верхнє")
else:
    print("Нижнє")

import math
d = float(input())
s = float(input())
side = math.sqrt(s)
if side * math.sqrt(2) <= d:
    print("Можна")
else:
    print("Ні")

s_zal = float(input())
r_scena = float(input())
k = float(input())
side_zal = math.sqrt(s_zal)
if r_scena + k <= side_zal / 2:
    print("Можна")
else:
    print("Ні")

a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    print("Існує")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Прямокутний")
else:
    print("Не існує")

a = float(input())
b = float(input())

if a < b:
    print(a, b)
else:
    print(b, a)

if a > b:
    print(a, b)
else:
    print(b, a)

a = float(input())
b = float(input())
c = float(input())

max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print(max_val)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if (x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0):
    print("YES")
elif (x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0):
    print("YES")
elif (x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0):
    print("YES")
elif (x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0):
    print("YES")
else:
    print("NO")

d = int(input())
m = int(input())
y = int(input())

days_in_month = 31
if m == 4 or m == 6 or m == 9 or m == 11:
    days_in_month = 30
elif m == 2:
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        days_in_month = 29
    else:
        days_in_month = 28

d = d + 1

if d > days_in_month:
    d = 1
    m = m + 1
    if m > 12:
        m = 1
        y = y + 1

print(d)
print(m)
print(y)

n = int(input())
if n % 10 == 1 and n % 100 != 11:
    print(n, "рік")
elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
    print(n, "роки")
else:
    print(n, "років")

summa = int(input())
for bill in [500, 200, 100, 50, 20, 10, 5, 2, 1]:
    count = summa // bill
    if count > 0:
        print(bill, ":", count)
        summa = summa % bill

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")

k = int(input())
if k == 0:
    print("YES")
elif k >= 4 and k % 4 == 0:
    print("YES")
else:
    print("NO")
