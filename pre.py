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

URL = "https://thepersonage.com/post-sitemap5.xml"

i = 0
count_table = 0
count_tr = 0
with open('sitemap_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    data = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    while(URL != None):
        # page = requests.get(URL, proxies={"http": random.choice(http_prxies)})
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        mainPage = soup.find("div", {"class": "article-three-posts"})

        ariticle = mainPage.find_all("article")
        for single in ariticle :
            print('Start Article: '+ str(i+1))
            link = single.find('a', {"class": "post-image post-image-left"})
            # singlePage = requests.get(link['href'], proxies={"http": random.choice(http_prxies)})
            singlePage = requests.get(link['href'])
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

            print("Table Count: " + str(len(tables)))
            for table in tables :
                trs = table.find_all('tr')
                print("TR: "+ str(len(trs)))
                for tr in trs :
                    tds = tr.find_all('td')
                    # print(tds[0].text+ ': '+tds[1].text)
                    # if(i == 0) :
                    #     headers.append(tds[0].text)
                    if(tds[1].text == '') :
                        tdr = 'Not Found'
                    else:
                        tdr = tds[1].text
                    body.append(tds[0].text)
                    # tdres = tdr.replace('$', 'USD ')
                    # tdres = tdres.replace('₹', 'INR ')
                    # tdres = tdres.replace('″', '&rsquo;')
                    # tdres = tdres.replace('′', '&rsquo;')
                    body.append(tdr)
            
            # if(i==0):
            #     data.writerow(headers)
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
