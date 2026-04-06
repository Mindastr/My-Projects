total = 0
counter = 0
even = 0
greater_than_6 = 0

for i in range(10, 4, -1):
    total = total + i
    counter = counter + 1
    last = i

    if i % 2 == 0:
        even = even + 1
    if i > 6:
        greater_than_6 = greater_than_6 + 1

print("Total:", total)
print("Counter:", counter)
print("Even:", even)
print("Greater than 6:", greater_than_6)
