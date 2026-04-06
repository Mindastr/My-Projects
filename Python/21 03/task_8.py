def task_8():
    t = float(input("Час t: "))
    s = 3*t**3 - 4*t**2 + 7
    v = 9*t**2 - 8*t  # Похідна S'(t)
    a = 18*t - 8     # Похідна V'(t)
    print(f"S={s}, V={v}, A={a}")

task_8()


