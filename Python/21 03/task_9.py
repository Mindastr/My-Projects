import math

def task_9():
    a = float(input("Сторона квадрата a: "))
    r_in = a / 2
    r_out = (a * math.sqrt(2)) / 2
    print(f"Вписаний R: {r_in}, Описаний R: {r_out}")

task_9()

