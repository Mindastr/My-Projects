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

print("=== TEST TASK 1 ===")
print()

print("Test 1 - Valid age (25):")
print("Result:", greet_v1('Ivan', '25'))
print()

print("Test 2 - Invalid age (-5):")
print("Result:", greet_v1('Maria', '-5'))
print()

print("Test 3 - Invalid age (150):")
print("Result:", greet_v1('Petro', '150'))
print()

print("Test 4 - V2 with valid input (30):")
print("Result:", greet_v2('Olga', '30'))
print()

print("Test 5 - V2 with invalid input (not a number):")
print("Result:", greet_v2('Sergiy', 'abc'))
print()

print("=== ANALYSIS ===")
print()
print("✓ V1 (greet_v1):")
print("  - Takes name and age as parameters")
print("  - Returns formatted string")
print("  - No try-except inside (validation outside)")
print("  - Checks: age < 0 or age > 130")
print()
print("✓ V2 (greet_v2):")
print("  - Takes name and age as parameters")
print("  - Returns formatted string")
print("  - Has try-except inside")
print("  - Checks: age < 0 or age > 130")
print("  - Handles ValueError")

