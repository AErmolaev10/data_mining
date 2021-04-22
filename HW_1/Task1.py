# -*- coding: cp1251 -*-

import json
import time
from pathlib import Path
import requests


"""
��������: https://5ka.ru/special_offers/
������ ������������ ���� ������, ���������� ����� ����� ���������� ������ � .json �����
���������: ������ ����������� � ���������, ��� ������ ������/������� ���������� � ���� ��������� ������ ����������� � 
Json �����, ��� ������ ��������� ������� ������ ���� ������ ��������� ���� � ��������� ������ ������������� 
�������������� ������ ���������.
������ ��������� ������ ��� �����:
������� ������ ����� ������ �������� �� �������
{
"name": "��� ���������",
"code": "��� �������������� ��������� (������������ � ��������)",
"products": [{PRODUCT}, {PRODUCT}........] # ������ �������� ������� �������������� ������ ���������
}
"""

# https://5ka.ru/api/v2/categories/   ���������!!!!
# [{"parent_group_code":"959","parent_group_name":"������� �����"},{"parent_group_code":"956","parent_group_name":"8 �����"},{"parent_group_code":"940","parent_group_name":"14 �������"},{"parent_group_code":"698","parent_group_name":"�������� �������� � ����"},{"parent_group_code":"827","parent_group_name":"����� � ������"},{"parent_group_code":"888","parent_group_name":"���� � �������"},{"parent_group_code":"716","parent_group_name":"���� � �����"},{"parent_group_code":"628","parent_group_name":"������� � �������"},{"parent_group_code":"602","parent_group_name":"������������ ��������"},{"parent_group_code":"800","parent_group_name":"���� � ������������"},{"parent_group_code":"870","parent_group_name":"�������"},{"parent_group_code":"853","parent_group_name":"��������"},{"parent_group_code":"902","parent_group_name":"���, ���� � �����"},{"parent_group_code":"732","parent_group_name":"�������"},{"parent_group_code":"637","parent_group_name":"��������"},{"parent_group_code":"661","parent_group_name":"������� � ����"},{"parent_group_code":"575","parent_group_name":"������ ��� ��������"},{"parent_group_code":"523","parent_group_name":"������ ��� �����"},{"parent_group_code":"542","parent_group_name":"������ ��� ����"},{"parent_group_code":"941","parent_group_name":"8 �����"},{"parent_group_code":"443","parent_group_name":"��������"},{"parent_group_code":"938","parent_group_name":"������ �� �����"},{"parent_group_code":"939","parent_group_name":"������ ��������"},{"parent_group_code":"943","parent_group_name":"������ ����"},{"parent_group_code":"942","parent_group_name":"������ �������"},{"parent_group_code":"468","parent_group_name":"������� �������"},{"parent_group_code":"965","parent_group_name":"������� ���"},{"parent_group_code":"479","parent_group_name":"������� ����� � ���������"},{"parent_group_code":"621","parent_group_name":"���������� �����"},{"parent_group_code":"623","parent_group_name":"�����, �����, ������"},{"parent_group_code":"945","parent_group_name":"�������"},{"parent_group_code":"585","parent_group_name":"����� ���"},{"parent_group_code":"785","parent_group_name":"�����"},{"parent_group_code":"562","parent_group_name":"������"},{"parent_group_code":"925","parent_group_name":"�����"},{"parent_group_code":"879","parent_group_name":"�������� ������� � ����������"}]


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
