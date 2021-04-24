# -*- coding: utf-8 -*-


import json
import time
from pathlib import Path
import requests

"""
Задача организовать сбор данных, необходимо иметь метод сохранения данных в .json файлы
результат: Данные скачиваются с источника, при вызове метода/функции сохранения в файл скачанные данные сохраняются в 
Json вайлы, для каждой категории товаров должен быть создан отдельный файл и содержать товары исключительно 
соответсвующие данной категории.
пример структуры данных для файла:
нейминг ключей можно делать отличным от примера
{
"name": "имя категории",
"code": "Код соответсвующий категории (используется в запросах)",
"products": [{PRODUCT}, {PRODUCT}........] # список словарей товаров соответсвующих данной категории
}
"""


class Parse5ka:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
    }

    def __init__(self, url_prod: str, url_cat: str, save_path: Path):
        self.url_prod = url_prod + "?page=1&records_per_page=20"
        self.url_cat = url_cat
        self.save_path = save_path

    def _get_response(self, url, *args, **kwargs):
        while True:
            response = requests.get(url, *args, **kwargs)
            if response.status_code == 200:
                return response
            time.sleep(1)

    def run(self):

        for cat in self._get_response(self.url_cat, headers=self.headers).json():

            print(f'Загрузка данных по категории  {cat["parent_group_name"]}')
            prod = []
            for product in self._parse(self.url_prod + f'&categories={cat["parent_group_code"]}'):
                prod.append(product)
            file_path = self.save_path.joinpath(f'{cat["parent_group_name"]}.json')
            self._save(cat, prod, file_path)

    def _parse(self, url: str):
        while url:
            time.sleep(0.1)
            response = self._get_response(url, headers=self.headers)
            data = response.json()
            if data["next"]:
                url = data["next"]
                url = url.replace('monolith', '5ka.ru')
            else:
                url = None
            for product in data["results"]:
                yield product

    def _save(self, cat: dict, prod: list, file_path):
        data = dict()
        data["name"] = cat["parent_group_name"]
        data["code"] = cat["parent_group_code"]
        data["products"] = prod
        file_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def get_save_path(dir_name):
    save_path = Path(__file__).parent.joinpath(dir_name)
    if not save_path.exists():
        save_path.mkdir()
    return save_path


if __name__ == "__main__":
    save_path = get_save_path("products")
    url_prod = "https://5ka.ru/api/v2/special_offers/"
    url_cat = "https://5ka.ru/api/v2/categories/"
    parser = Parse5ka(url_prod, url_cat, save_path)
    parser.run()
