import requests
import random

http_prxies = [
    'http://47.242.31.180:59394',
    'http://47.241.163.216:59394',
    'http://47.243.60.6:59394',
    'http://47.241.126.153:59394',
    'http://47.242.83.137:59394',
    'http://47.243.184.160:59394',
]

# proxy = random.choice(http_prxies)

# print(proxy)

site = requests.get('http://icanhazip.com/', proxies={"http": 'http://47.243.184.160:59394'})

# soup = BeautifulSoup(site.content)

print(site.content)