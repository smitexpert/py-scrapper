import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://thepersonage.com/amit-behl/'

page = requests.get(URL)

singleContent = BeautifulSoup(page.content, "html.parser")
content = singleContent.find('article', {"class": "article"})
tables = content.find_all('table')

with open('testnew_data.csv', 'w', newline='') as csvfile:
    data = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    for table in tables :
        trs = table.find_all('tr')
        body = []
        print("TR: "+ str(len(trs)))
        for tr in trs :
            tds = tr.find_all('td')
            print(tds[0].text+ ': '+tds[1].text)
            body.append(tds[1].text.replace('₹', ''))

    data.writerow(body)
