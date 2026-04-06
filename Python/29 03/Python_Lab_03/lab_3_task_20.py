n = input()
a = []

for x in n:
    a.append(x)

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

if a[0] == "0":
    for i in range(1, len(a)):
        if a[i] != "0":
            a[0], a[i] = a[i], a[0]
            break

mn = ""
mx = ""

for x in a:
    mn = mn + x

for i in range(len(a) - 1, -1, -1):
    mx = mx + a[i]

print(mn, mx)
