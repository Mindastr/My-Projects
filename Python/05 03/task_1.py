text = input("Enter text: ")
words = input("Enter reserved words: ").split()

for word in words:
    text = text.replace(word, word.upper())

print("Result:", text)

