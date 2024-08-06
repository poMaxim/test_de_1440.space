# Stations Project

Этот проект использует Scrapy для парсинга данных о станциях с сайта `vagon1520.ru` и сохранения их в CSV файл.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/poMaxim/test_de_1440.space.git
    cd test_de_1440.space
    cd stations_project
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск

Для запуска паука используйте следующую команду:
```bash
scrapy crawl stations


Данные будут сохранены в файл stations.csv
Время парсинга ≈ 8 сек.
