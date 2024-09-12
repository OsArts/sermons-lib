# /scripts/space_cleaner.py
# v.0.2.0

import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {file_path} not found.")
    sys.exit(1)

# Удаляем пустые строки
filtered_lines = [line for line in lines if line.strip() != '']

# Обрабатываем строки
processed_lines = []
for i in range(len(filtered_lines)):
    line = filtered_lines[i]
    
    # Удаляем точку в конце чётных строк
    if (i + 1) % 2 == 0:  # чётные строки (индекс i + 1)
        line = line.rstrip('.')
        # Склеиваем с предыдущей строкой
        processed_lines[-1] += line
    else:
        processed_lines.append(line)

# Заменяем символы и записываем обратно в файл
final_lines = []
for line in processed_lines:
    line = line.replace('(', ',').replace(').', ',')  # Заменяем символы ( и )
    final_lines.append(line)

with open(file_path, 'w') as file:
    file.writelines(final_lines)

print(f"File {file_path} has been processed.")