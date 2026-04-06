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
