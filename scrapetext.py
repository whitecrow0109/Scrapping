import requests
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        page = requests.get(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title, soup


title, soup = getTitle('http://www.pythonscraping.com/pages/warandpeace.html')
if title == None:
    print("Title couldn't be found")
else:
    print(title)
    nameList = soup.find_all('span', class_="green")
    for name in nameList:
        print(name.text)