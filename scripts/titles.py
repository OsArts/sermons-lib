#
# 2024-09-08 15:19
# 

import re

def extract_quotes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    quotes = []
    for line in lines:
        # Находим все подстроки, заключенные в кавычки
        found_quotes = re.findall(r'"(.*?)"', line)
        quotes.extend(found_quotes)

    # Записываем найденные подстроки в output.txt
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for quote in quotes:
            outfile.write(f'"{quote}"\n')

if __name__ == "__main__":
    input_filename = './tmp/output.txt'
    output_filename = './tmp/titles_2022.txt'
    
    extract_quotes(input_filename, output_filename)
    print(f'Подстроки сохранены в {output_filename}.')