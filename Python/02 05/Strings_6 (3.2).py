text = input("Текст: ")
print(sum(1 for c in text if c in '.!?'))