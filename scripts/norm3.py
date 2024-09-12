def transform_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        transformed_lines = []
        for line in lines:
            # Убираем лишние пробелы и символы новой строки
            line = line.strip()

            if line:  # Проверяем, что строка не пустая
                # Разбиваем строку на части
                parts = line.split('",')
                
                if len(parts) >= 2:
                    sermon_title = parts[0].split('"')[1]  # Название проповеди
                    date_info = parts[1].split('(')[0].strip()  # Дата
                    other_info = parts[1].replace('(', '').replace(')', '').strip()  # Остальная информация

                    # Формируем новую строку
                    new_line = f"Проповедь, {sermon_title}, {date_info}, {other_info},"
                    transformed_lines.append(new_line)

        # Записываем результат в выходной файл
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for transformed_line in transformed_lines:
                outfile.write(transformed_line + '\n')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Укажите имена входного и выходного файлов
d_file = 'input2022_c.txt'
input_filename = './tmp/' + d_file

o_file = 'output2022_c.txt'
output_filename = './tmp/' + o_file

print(f"Читаем данные из {d_file}")
print(f"Новый файл: ./tmp/{o_file}")


# transform_file(input_filename, output_filename)
transform_file(d_file, o_file)
