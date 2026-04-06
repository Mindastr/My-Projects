import math

def task_14():
    s = float(input("Відстань S: "))
    v = float(input("Швидкість V (км/добу): "))
    print(f"Діб (цілим числом): {math.ceil(s / v)}")

task_14()

