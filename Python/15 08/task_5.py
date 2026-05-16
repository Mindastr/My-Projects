file_name = "students.txt"


def load_students():
    students = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(";")
                    students.append(parts)
    except:
        pass
    return students


def save_students(students):
    with open(file_name, "w", encoding="utf-8") as f:
        for st in students:
            f.write(";".join(st) + "\n")


def show_all(students):
    if len(students) == 0:
        print("Список порожній")
        return

    for st in students:
        print(st)


def add_student(students):
    surname = input("Прізвище: ")
    name = input("Ім'я: ")
    group = input("Група: ")
    marks = input("Оцінки через пробіл: ")

    students.append([surname, name, group, marks])
    save_students(students)
    print("Студента додано")


def delete_student(students):
    surname = input("Введіть прізвище для видалення: ")
    new_students = []

    for st in students:
        if st[0] != surname:
            new_students.append(st)

    save_students(new_students)
    print("Видалення виконано")


def edit_student(students):
    surname = input("Введіть прізвище для зміни: ")

    for st in students:
        if st[0] == surname:
            st[0] = input("Нове прізвище: ")
            st[1] = input("Нове ім'я: ")
            st[2] = input("Нова група: ")
            st[3] = input("Нові оцінки: ")
            save_students(students)
            print("Інформацію змінено")
            return

    print("Студента не знайдено")


def search_student(students):
    param = input("Введіть значення для пошуку: ")

    found = False
    for st in students:
        if param in st:
            print(st)
            found = True

    if not found:
        print("Нічого не знайдено")


def average_mark(marks_text):
    marks = marks_text.split()
    total = 0
    count = 0
    for m in marks:
        if m.isdigit():
            total += int(m)
            count += 1
    if count == 0:
        return 0
    return total / count


def sort_students(students):
    print("1 - за алфавітом")
    print("2 - за середнім балом")
    choice = input("Ваш вибір: ")

    if choice == "1":
        students.sort()
    elif choice == "2":
        students.sort(key=lambda x: average_mark(x[3]), reverse=True)

    show_all(students)


def excellent_students(students):
    for st in students:
        if average_mark(st[3]) >= 10:
            print(st)


students = load_students()

while True:
    print("\nМеню:")
    print("1 - Додати студента")
    print("2 - Видалити студента")
    print("3 - Змінити інформацію")
    print("4 - Показати всіх студентів")
    print("5 - Пошук студента")
    print("6 - Вивести в певному порядку")
    print("7 - Відмінники")
    print("0 - Вихід")

    choice = input("Оберіть пункт: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        delete_student(students)
        students = load_students()
    elif choice == "3":
        edit_student(students)
        students = load_students()
    elif choice == "4":
        show_all(students)
    elif choice == "5":
        search_student(students)
    elif choice == "6":
        sort_students(students)
    elif choice == "7":
        excellent_students(students)
    elif choice == "0":
        break
    else:
        print("Невірний вибір")
