def greet_v1(name, age):
    age = int(age)
    if age < 0 or age > 130:
        return "Error"
    msg = "Привіт, " + name + "! Твій вік - " + str(age)
    return msg

def greet_v2(name, age):
    try:
        age = int(age)
        if age < 0 or age > 130:
            return "Error"
        msg = "Привіт, " + name + "! Твій вік - " + str(age)
        return msg
    except:
        return "Error"

print("V1:")
try:
    name = input("Ім'я: ")
    age = input("Вік: ")
    print(greet_v1(name, age))
except:
    print("Error")

print()
print("V2:")
name = input("Ім'я: ")
age = input("Вік: ")
print(greet_v2(name, age))
