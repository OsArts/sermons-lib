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
input_filename = './tmp/output.txt'
output_filename = './tmp/output22_b.txt'

transform_file(input_filename, output_filename)