# 
# ./scripts/norm.py
# 

def transform_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    transformed_lines = []
    for line in lines:
        # Убираем лишние пробелы и символы новой строки
        line = line.strip()
        
        # Разбиваем строку на части
        parts = line.split('",')
        
        # Извлекаем нужные элементы
        if len(parts) == 2:
            sermon_title = parts[0].split('"')[1]  # Название проповеди
            other_info = parts[1].replace('(', '').replace(')', '')  # Остальная информация
            # Формируем новую строку
            new_line = f"Проповедь, {sermon_title}, {other_info.strip()}, ,"
            transformed_lines.append(new_line)

    # Записываем результат в выходной файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for transformed_line in transformed_lines:
            outfile.write(transformed_line + '\n')

# Укажите имена входного и выходного файлов
input_filename = 'input.txt'
output_filename = 'output.txt'

transform_file(input_filename, output_filename)