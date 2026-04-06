def word(n):
    if n % 100 >= 11 and n % 100 <= 14:
        return "слоненят"
    if n % 10 == 1:
        return "слоненя"
    if n % 10 >= 2 and n % 10 <= 4:
        return "слоненяти"
    return "слоненят"


n = int(input())

for i in range(1, n + 1):
    print(i, word(i))
