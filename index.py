import random
import requests
import csv
from bs4 import BeautifulSoup

http_proxy  = "222.74.202.239:8080"

proxyDict = { 
              "http"  : http_proxy
            }

http_prxies = [
    'http://77.50.104.110:3128',
    'http://45.79.223.43:9091',
]

URL = "https://thepersonage.com/actor/page/3/"

i = 0
with open('new_data.csv', 'w', newline='') as csvfile:
    data = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    while(URL != None):
        page = requests.get(URL, proxies={"http": random.choice(http_prxies)})

        soup = BeautifulSoup(page.content, "html.parser")

        mainPage = soup.find("div", {"class": "article-three-posts"})

        ariticle = mainPage.find_all("article")
        for single in ariticle :
            print('Start Article: '+ str(i+1))
            link = single.find('a', {"class": "post-image post-image-left"})
            singlePage = requests.get(link['href'], proxies={"http": random.choice(http_prxies)})
            singleContent = BeautifulSoup(singlePage.content, "html.parser")
            content = singleContent.find('article', {"class": "article"})
            # break
            
            
            tables = content.find_all('table')
            category = singleContent.find('span', {'class': 'thecategory'})
            figure = singleContent.find('figure')
            image = figure.find('img')
            # print(image['data-layzr'])
            headers = ['category', 'image']
            body = [category.text, image['data-layzr']]
            for table in tables :
                print('START TABLE')
                trs = table.find_all('tr')
                for tr in trs :
                    tds = tr.find_all('td')
                    # print(tds[0].text+ ': '+tds[1].text)
                    if(i == 0) :
                        headers.append(tds[0].text)
                    tdr = tds[1].text
                    tdres = tdr.replace('$', 'USD ')
                    tdres = tdres.replace('₹', 'INR ')
                    tdres = tdres.replace('″', '"')
                    tdres = tdres.replace('′', '"')
                    body.append(tdres)
                print('END TABLE')
            
            if(i==0):
                data.writerow(headers)
            data.writerow(body)
            i=i+1
            print("Number of Article: "+str(i))

        prev = soup.find('li', {'class': 'nav-previous'})
        prev_link = prev.find('a')
        if(prev_link == None):
            URL = None
        else:
            URL = prev_link['href']

# print(len(ariticle))

# results = soup.find(id="ResultsContainer")
# print(results.prettify())
