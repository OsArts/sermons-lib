import requests
from bs4 import BeautifulSoup

year = 7

###### Zero {0} need for 2002..2009
new_file = "output_sermons0" + str(year) + ".txt"
# new_file = "output_sermons.txt"
# URL для парсинга
# url = 'http://sdaprotvino.ru/sermons.htm' # for current 2024

url = 'http://sdaprotvino.ru/sermons' + str(year - 1) +'.htm'

print(f"Начинаем парсить заголовки проповедей ❤️ за 200{year}-й год.")
# Выполняем GET-запрос к URL
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Устанавливаем правильную кодировку
    response.encoding = response.apparent_encoding
    
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все теги <span> с нужным стилем
    ### For 2017-2024, 12b,
    # spans = soup.find_all('span', style='color: red;') # It works for 2017-2024
    
    ### For ...2016
    # spans = soup.find_all('span', style='color: rgb(255, 0, 0);') # For ...2016
    
    ### For 08a..2012_c
    ### https://stackoverflow.com/questions/16248723/how-to-find-spans-with-a-specific-class-containing-specific-text-using-beautiful
    # spans = soup.find_all('span', {'class' :'style1'}) # It works for 2008a..2012c
    
    ### For 2008b
    spans = soup.find_all('font', {'color':'#ff0000'})

    # Открываем файл для записи
    with open(new_file, 'w', encoding='utf-8') as file:
        for span in spans:
            # Получаем текст из тега и очищаем его
            text = span.get_text(strip=True)
            # Записываем текст в файл в нужном формате
            file.write(f'"{text}"\n')

    print(f"Данные успешно сохранены в {new_file}")
else:
    print(f"Ошибка при запросе: {response.status_code}")