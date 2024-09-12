year = 7

### Need set Zero {0} For 2002..2009
new_file = "output_sermons0" + str(year) + ".txt"

# Открываем файл для чтения
with open(new_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Обрабатываем строки
processed_lines = []
for line in lines:
    # Удаляем символы """ и заменяем "" на "
    line = line.replace('"""', '').replace('""', '"')
    # Удаляем пробелы в начале и конце строки
    line = line.strip()
    
    # Добавляем непустую строку в список, исключая строки с только одним символом "
    if line and line != '"':
        processed_lines.append(line)

# Открываем файл для записи и сохраняем обработанные строки
with open(new_file, 'w', encoding='utf-8') as file:
    for line in processed_lines:
        file.write(line + '\n')

print("Файл ✅ успешно обработан.")