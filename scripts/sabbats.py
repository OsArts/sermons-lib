# 
# 2024-09-08 14:50
# 

import sys
from datetime import datetime, timedelta


""" 
# По указанному году формируется список дат(конкретно суббот),
# сохраняемый во временных файлах `./tmp/{year}_sabbats.txt`
# Это 2й фрагмент для скраппинга старого архива за период 2002-2024
# он необходим для формирования `./data/_pre/sermons{year}.csv`
# для финальной конвертации в `./data/sermons/{year.json}`
"""
def get_saturdays(year):
    saturdays = []
    # Начинаем с первого января указанного года
    date = datetime(year, 1, 1)
    
    # Ищем первую субботу
    while date.weekday() != 5:  # 5 соответствует субботе
        date += timedelta(days=1)

    # Добавляем все субботы в список до конца года
    while date.year == year:
        saturdays.append(date.strftime('%d.%m.%Y'))
        date += timedelta(days=7)

    return saturdays

def save_saturdays_to_file(year, saturdays):
    filename = f"./tmp/{year}_sabbats.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        for saturday in saturdays:
            file.write(saturday + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <год>")
        sys.exit(1)

    try:
        year = int(sys.argv[1])
        print(f"начинаем формировать список суббот 📜 {year}")
        
        saturdays = get_saturdays(year)
        save_saturdays_to_file(year, saturdays)
        print(f"Субботы {year} сохранены в файл ./tmp/{year}_sabbats.txt")
    except ValueError:
        print("Пожалуйста, введите корректный год.")