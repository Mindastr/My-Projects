counter = 0
for _ in range(5):
    word = input()
    if 'р' in word:
        counter = counter + 1

print(counter)