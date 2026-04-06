n = int(input())
d = [0] * (n + 1)
d[0] = 1

for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        d[j] = d[j] + d[j - i]

print(d[n])
