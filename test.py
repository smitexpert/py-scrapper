import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://thepersonage.com/andrew-antoniolli/'

page = requests.get(URL)

singleContent = BeautifulSoup(page.content, "html.parser")
content = singleContent.find('article', {"class": "article"})
# tables = content.find_all('table')

figure = singleContent.find('figure')
# image = figure.find('img')

print(figure)

# if(figure == None):
#     print('Nai')
# else:
#     print(image)