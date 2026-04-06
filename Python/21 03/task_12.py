def task_12():
    l = float(input("Довжина кімнати: "))
    w = float(input("Ширина кімнати: "))
    h = float(input("Висота стін: "))
    rl = float(input("Довжина рулону: "))
    rw = float(input("Ширина рулону: "))
    room_s = 2 * h * (l + w)
    roll_s = rl * rw
    print(f"Потрібно рулонів: {math.ceil(room_s / roll_s)}")

task_12()

