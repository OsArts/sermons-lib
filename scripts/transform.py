# transform.py
# v.0.3

def transform_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Разделяем содержимое на проповеди
    sermons = content.strip().split('\n\n')

    # Преобразуем каждую проповедь в нужный формат
    transformed_sermons = []
    for sermon in sermons:
        lines = sermon.strip().split('\n')
        # Объединяем строки и убираем лишние пробелы
        transformed_sermon = ','.join(line.strip() for line in lines)

        # line = line.replace('(', ',').replace(').', ',')  # Заменяем символы ( и )
        # transformed_sermon = lines.replace('(', ',').replace(').', ',')

        transformed_sermons.append(transformed_sermon)

    # Записываем результат в выходной файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for sermon in transformed_sermons:
            outfile.write(sermon + '\n')

# Укажите имена входного и выходного файлов
input_filename = './tmp/input.txt'
output_filename = './tmp/output.txt'

transform_file(input_filename, output_filename)
