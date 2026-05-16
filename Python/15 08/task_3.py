file_name = "text.txt"

search_word = input("Яке слово шукати: ")
replace_word = input("На яке замінити: ")

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(search_word, replace_word)

with open(file_name, "w", encoding="utf-8") as f:
    f.write(text)

print("Заміна виконана")
