# DEVELOPMENT PIPE

Use `/scripts/*` for get chunks by `parsing data`

## ШАГ 1. Получение списка заголовков проповедей

> `./scripts/get_2022.py`

- открыть `./scripts/get_2022.py` в редакторе, указать искомый год(если 2022 то присваиваем `year = 22`)
- открыть `./scripts/cleaner.py` в редакторе, указать искомый год(если 2022 то присваиваем `year = 22`)
- [x] `make data`

---
 
## ШАГ 2. Clean_breakspaces

- открыть терминал и задать значение переменной `$ export DATAFILE="./tmp/input.txt"` << тут буду данные за [2022] созданные на предыдущем шаге 1.
- Makefile имеет правило `sp:` - **space_cleaner**
- `$ make sp` или
    - `$ python3 ./scripts/space_cleaner.py ./tmp/input.txt`
    

## Prod_server

- [ ] наполнять каталог `/lib/{year}` от билда из `/dist/sermons/`

## Screapping Use Python3 inside

> [Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

### Prepare

- [x] Once create **ENV**: 

1. `$ python3 -m venv .venv`
2. `$ source .venv/bin/activate`
3. `$ which python3`
2. `$ pip3 install beautifulsoup4 requests html5lib`

```terminal
Installing collected packages: webencodings, urllib3, soupsieve, six, idna, charset-normalizer, certifi, requests, html5lib, beautifulsoup4
Successfully installed beautifulsoup4-4.12.3 certifi-2024.8.30 charset-normalizer-3.3.2 html5lib-1.1 idna-3.8 requests-2.32.3 six-1.16.0 soupsieve-2.6 urllib3-2.2.2 webencodings-0.5.1
```
---

### 🚀 Work flow

Start `.venv`
- `$ source .venv/bin/activate`

Finish(Exit from ENV)
- `$ deactivate`


## bat

> [bat rust tool](https://github.com/sharkdp/bat)

### CSV

- `$ bat --list-languages` comma separeted values: **csv** | **tsv**

При выводе текста файла "*.csv", ставил `;`-разделитель, есть проблема смещения цветовой подсветки синтаксиса по столбцам:
 - сбой происходит по запятым.
 