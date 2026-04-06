def word(n):
    if 11 <= n % 100 <= 14:
        return "слоненят"
    if n % 10 == 1:
        return "слоненя"
    if 2 <= n % 10 <= 4:
        return "слоненяти"
    return "слоненят"


while True:
    print("1 - task 11")
    print("2 - task 12")
    print("3 - task 13")
    print("4 - task 14")
    print("5 - task 15")
    print("6 - task 16")
    print("0 - exit")
    m = input()

    if m == "0":
        break

    if m == "1":
        for i in range(1, 11):
            print(i)

    elif m == "2":
        n = int(input())
        for i in range(1, n + 1):
            print(i)

    elif m == "3":
        n = int(input())
        for i in range(1, n + 1):
            print(i)
            print("  /\\  ___  /\\\\")
            print(" (  o   o  )")
            print("  \\   ^   /")
            print("   |||||")
            print("   || ||")

    elif m == "4":
        n = int(input())
        for i in range(1, n + 1):
            print(i, word(i))

    elif m == "5":
        n = int(input())
        for i in range(1, n + 1):
            print(i, "слоненя")
            print("  /\\  ___  /\\\\")
            print(" (  o   o  )")
            print("  \\   ^   /")
            print(" /|       |\\\\")
            print("/_|_______|_\\\\")
            print("  /_/   \\_\\\\")

    elif m == "6":
        t = input()
        n = int(input())
        if t == "1":
            for i in range(1, n + 1):
                print(i, word(i))
        else:
            for i in range(1, n + 1):
                print(i, "віслюк")
