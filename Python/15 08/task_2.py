file_name = "text.txt"

with open(file_name, "r", encoding="utf-8") as f:
    lines = f.readlines()

max_len = 0

for line in lines:
    line = line.rstrip("\n")
    if len(line) > max_len:
        max_len = len(line)

print("Довжина найдовшого рядка:", max_len)