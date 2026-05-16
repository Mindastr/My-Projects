file_name = "text.txt"
new_file_name = "result1.txt"

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

chars = len(text)
lines = text.count("\n") + 1 if text else 0

vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
consonants = "бвгґджзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ"

count_vowels = 0
count_consonants = 0
count_digits = 0

for ch in text:
    if ch in vowels:
        count_vowels += 1
    elif ch in consonants:
        count_consonants += 1
    elif ch.isdigit():
        count_digits += 1

with open(new_file_name, "w", encoding="utf-8") as f:
    f.write("Статистика файлу:\n")
    f.write("Кількість символів: " + str(chars) + "\n")
    f.write("Кількість рядків: " + str(lines) + "\n")
    f.write("Кількість голосних: " + str(count_vowels) + "\n")
    f.write("Кількість приголосних: " + str(count_consonants) + "\n")
    f.write("Кількість цифр: " + str(count_digits) + "\n")

print("Готово")
