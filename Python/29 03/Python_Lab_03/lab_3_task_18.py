for n in range(2, 5):
    for x in range(10 ** (n - 1), 10 ** n):
        s = 0
        a = str(x)

        for d in a:
            s = s + int(d) ** n

        if s == x:
            print(x)
