def task_10():
    r1, r2, r3 = map(float, input("Введіть R1, R2, R3 через пробіл: ").split())
    print(f"Послідовно: {r1 + r2 + r3}")
    r_par = 1 / (1/r1 + 1/r2 + 1/r3)
    print(f"Паралельно: {r_par}")

task_10()

