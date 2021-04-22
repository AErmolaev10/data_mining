# -*- coding: cp1251 -*-

import json
import time
from pathlib import Path
import requests


"""
Источник: https://5ka.ru/special_offers/
Задача организовать сбор данных, необходимо иметь метод сохранения данных в .json файлы
результат: Данные скачиваются с источника, при вызове метода/функции сохранения в файл скачанные данные сохраняются в 
Json файлы, для каждой категории товаров должен быть создан отдельный файл и содержать товары исключительно 
соответсвующие данной категории.
пример структуры данных для файла:
нейминг ключей можно делать отличным от примера
{
"name": "имя категории",
"code": "Код соответсвующий категории (используется в запросах)",
"products": [{PRODUCT}, {PRODUCT}........] # список словарей товаров соответсвующих данной категории
}
"""

# https://5ka.ru/api/v2/categories/   КАТЕГОРИИ!!!!
# [{"parent_group_code":"959","parent_group_name":"Горячая кухня"},{"parent_group_code":"956","parent_group_name":"8 марта"},{"parent_group_code":"940","parent_group_name":"14 февраля"},{"parent_group_code":"698","parent_group_name":"Молочные продукты и яйца"},{"parent_group_code":"827","parent_group_name":"Овощи и фрукты"},{"parent_group_code":"888","parent_group_name":"Хлеб и выпечка"},{"parent_group_code":"716","parent_group_name":"Мясо и птица"},{"parent_group_code":"628","parent_group_name":"Колбаса и сосиски"},{"parent_group_code":"602","parent_group_name":"Замороженные продукты"},{"parent_group_code":"800","parent_group_name":"Рыба и морепродукты"},{"parent_group_code":"870","parent_group_name":"Бакалея"},{"parent_group_code":"853","parent_group_name":"Сладости"},{"parent_group_code":"902","parent_group_name":"Чай, кофе и какао"},{"parent_group_code":"732","parent_group_name":"Напитки"},{"parent_group_code":"637","parent_group_name":"Консервы"},{"parent_group_code":"661","parent_group_name":"Красота и уход"},{"parent_group_code":"575","parent_group_name":"Товары для животных"},{"parent_group_code":"523","parent_group_name":"Товары для детей"},{"parent_group_code":"542","parent_group_name":"Товары для дома"},{"parent_group_code":"941","parent_group_name":"8 марта"},{"parent_group_code":"443","parent_group_name":"Алкоголь"},{"parent_group_code":"938","parent_group_name":"Лучшее по акции"},{"parent_group_code":"939","parent_group_name":"Лидеры рейтинга"},{"parent_group_code":"943","parent_group_name":"Уютный ужин"},{"parent_group_code":"942","parent_group_name":"Бодрый завтрак"},{"parent_group_code":"468","parent_group_name":"Бытовая техника"},{"parent_group_code":"965","parent_group_name":"Готовая еда"},{"parent_group_code":"479","parent_group_name":"Готовые блюда и кулинария"},{"parent_group_code":"621","parent_group_name":"Дисконтные карты"},{"parent_group_code":"623","parent_group_name":"Книги, диски, пресса"},{"parent_group_code":"945","parent_group_name":"Малышам"},{"parent_group_code":"585","parent_group_name":"Новый год"},{"parent_group_code":"785","parent_group_name":"Пасха"},{"parent_group_code":"562","parent_group_name":"Мебель"},{"parent_group_code":"925","parent_group_name":"Обувь"},{"parent_group_code":"879","parent_group_name":"Табачные изделия и аксессуары"}]


class Parse5ka:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
    }
    params = {
        "records_per_page": 20,
    }

# categories = {}

    def __init__(self, star_url: str, save_path: Path):
        self.star_url = star_url
        self.save_path = save_path

    def _get_response(self, url, *args, **kwargs):
        while True:
            response = requests.get(url, *args, **kwargs)
            if response.status_code == 200:
                return response
            time.sleep(0.1)

    def run(self):
        for product in self._parse(self.star_url):
            file_path = self.save_path.joinpath(f"{product['id']}.json")
            self._save(product, file_path)

    def _parse(self, url: str):
        while url:
            time.sleep(0.1)
            response = self._get_response(url, headers=self.headers, params=self.params)
            data = response.json()
            url = data["next"]
            for cat in data["results"]:
                yield cat

    def _save(self, data: dict, file_path):
        file_path.write_text(json.dumps(data, ensure_ascii=False))


def get_save_path(dir_name):
    save_path = Path(__file__).parent.joinpath(dir_name)
    if not save_path.exists():
        save_path.mkdir()
    return save_path


if __name__ == "__main__":
    save_path = get_save_path("products")
    url = "https://5ka.ru/api/v2/categories/"
    parser = Parse5ka(url, save_path)
    parser.run()
