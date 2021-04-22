# Получаем категории и их код

import requests

url = 'https://5ka.ru/api/v2/categories/'
r = requests.get(url)
cat_and_code = r.json()
print(cat_and_code)
