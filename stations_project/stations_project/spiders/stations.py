import scrapy
import pandas as pd

class StationsSpider(scrapy.Spider):
    name = "stations"
    allowed_domains = ["vagon1520.ru"]
    start_urls = [
        'https://vagon1520.ru/stations',
    ]

    def __init__(self):
        self.stations = []

    def parse(self, response):
        # Определение общего количества страниц
        total_pages = int(response.css('div.pageSelect.__page::attr(data-href)').re(r'/stations/(\d+)')[-1])
        self.log(f'Всего страниц {total_pages}')

        # Парсинг данных с текущей страницы
        self.parse_page(response)

        # Переход на следующие страницы
        for page in range(2, total_pages + 1):
            next_page_url = f'https://vagon1520.ru/stations/{page}'
            yield scrapy.Request(next_page_url, callback=self.parse_page)

    def parse_page(self, response):
        for row in response.css('table tr'):
            code = row.css('td:nth-child(1)::text').get()
            name = row.css('td:nth-child(2)::text').get()
            station_type = row.css('td:nth-child(3)::text').get()
            if code:
                self.stations.append({
                    'Код станции': code,
                    'Название станции': name,
                    'Тип станции': station_type
                })

        # Сохранение данных в таблицу после парсинга всех страниц
        df = pd.DataFrame(self.stations)
        df.to_csv('stations.csv', index=False, encoding='utf-8')
