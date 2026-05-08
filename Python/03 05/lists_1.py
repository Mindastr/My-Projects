text = input("Введіть текст: ")
reserved = input("Зарезервовані слова: ").split()

words = text.split()
for i in range(len(words)):
    if words[i] in reserved:
        words[i] = words[i].upper()

print(" ".join(words))
