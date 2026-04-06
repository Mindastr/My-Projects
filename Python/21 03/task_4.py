def task_4():
    n = int(input("Введіть двозначне число: "))
    d1 = n // 10
    d2 = n % 10
    print(f"Сума: {d1 + d2}, Частка: {d1 / d2 if d2 != 0 else 'на 0 не ділимо'}")
    print(f"Різниця: {d1 - d2} або {d2 - d1}")
    print(f"Добуток: {d1 * d2}")

task_4()

