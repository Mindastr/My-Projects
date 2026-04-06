import math

def task_7():
    # а) катети
    a = float(input("Катет a: "))
    b = float(input("Катет b: "))
    print(f"Площа (через катети): {0.5 * a * b}")
    # б) катет і гіпотенуза
    c = float(input("Гіпотенуза c: "))
    leg2 = math.sqrt(c**2 - a**2)
    print(f"Площа (через катет і гіпотенузу): {0.5 * a * leg2}")

task_7()

