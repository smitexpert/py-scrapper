import random
import requests
import csv
from csv import writer
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

filename = 'post-sitemap11'

http_prxies = [
    'http://47.242.31.180:59394',
    'http://47.241.163.216:59394',
    'http://47.243.60.6:59394',
    'http://47.241.126.153:59394',
    'http://47.242.83.137:59394',
    'http://47.243.184.160:59394',
]

def loadRSS():
  
    # url of rss feed
    url = 'https://thepersonage.com/'+filename+'.xml'
  
    # creating HTTP response object from given url
    # resp = requests.get(url, proxies={"http": random.choice(http_prxies)})
    resp = requests.get(url)
  
    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)

def parseXML(xmlfile):
  
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
    i=1
    for x in root:
        link = x[0].text
        if(link == 'https://thepersonage.com/') :
            continue
        
        print(str(i)+ ' - '+link)
        i = i+1
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        content = soup.find('article', {"class": "article"})
        tables = content.find_all('table')
        category = soup.find('span', {'class': 'thecategory'})
        figure = soup.find('figure')

        print(category.text)

        if(category.text == 'NEWS'):
            continue

        if(figure == None):
            image_data = ''
        else :
            image = figure.find('img')
            if(image == None):
                image_data = ''
            else:
                image_data = image['data-layzr']


        body = [category.text, image_data]

        for table in tables :
            trs = table.find_all('tr')
            for tr in trs :
                tds = tr.find_all('td')
                
                # if(tds[1].text == '') :
                #     tdr = 'Not Found'
                # else:

                if(len(tds) > 1) :
                    tdr = tds[1].text
                else:
                    tdr = 'Not Found'

                if(len(tds) > 1) :
                    tdl = tds[0].text
                else:
                    tdl = ''
                    
                body.append(tdl)
                body.append(tdr)
        
        

        savetoCSV(body)


def savetoCSV(data):
  with open('xml_'+filename+'.csv', 'a', newline='', encoding='utf-8') as csvfile:
        write_object = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        write_object.writerow(data)

        csvfile.close()
  
      
def main():
    # load rss from web to update existing xml file
    loadRSS()
  
    # parse xml file
    parseXML('topnewsfeed.xml')
  
    # store news items in a csv file
    # savetoCSV(data)
      
      
if __name__ == "__main__":
  
    # calling main function
    main()