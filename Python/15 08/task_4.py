file_name = "text.txt"
bad_words_file = "bad_words.txt"
new_file_name = "clean_text.txt"

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

with open(bad_words_file, "r", encoding="utf-8") as f:
    bad_words = f.read().split()

for word in bad_words:
    text = text.replace(word, "***")

with open(new_file_name, "w", encoding="utf-8") as f:
    f.write(text)

print("Готово")
