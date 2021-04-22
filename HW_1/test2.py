import requests

url = 'https://5ka.ru/api/v2/categories/'
r = requests.get(url)
data2 = r.json()
