file_lines = []
with open("airtravel.csv") as file:
    for line in file:
        file_lines.append(line)
print(file_lines)
