import requests

site = requests.get('http://icanhazip.com/')

# soup = BeautifulSoup(site.content)

print(site.content)