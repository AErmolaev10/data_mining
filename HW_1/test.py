import requests

# Получаем категории и их код
"""url = 'https://5ka.ru/api/v2/categories/'
r = requests.get(url)
data = r.json()"""

#print(data[0])

#for i in data:
#   print(i)

#print(data[0]['parent_group_code'])

""" next: https://5ka.ru/api/v2/special_offers/?categories=698&ordering=&page=2&price_promo__gte=&price_promo__lte=&records_per_page=12&search=&store="""


url2 = 'https://5ka.ru/api/v2/special_offers/?categories=698&ordering=&page=2&price_promo__gte=&price_promo__lte=&records_per_page=12&search=&store='
"""r2 = requests.get(url2)
data2 = r2.json()

print(data2)"""

while url2:
    r2 = requests.get(url2)
    data2 = r2.json()
    url = data2["next"]
    for name in data2["results"]:
        print(name)
