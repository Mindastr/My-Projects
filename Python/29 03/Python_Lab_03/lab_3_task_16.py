def elephant_word(n):
    if 11 <= n % 100 <= 14:
        return "слоненят"
    if n % 10 == 1:
        return "слоненя"
    if 2 <= n % 10 <= 4:
        return "слоненяти"
    return "слоненят"


def donkey_word(n):
    if 11 <= n % 100 <= 14:
        return "віслюків"
    if n % 10 == 1:
        return "віслюк"
    if 2 <= n % 10 <= 4:
        return "віслюки"
    return "віслюків"


m = input()
n = int(input())

if m == "1":
    for i in range(1, n + 1):
        print(i, elephant_word(i))
else:
    for i in range(1, n + 1):
        print(i, donkey_word(i))
