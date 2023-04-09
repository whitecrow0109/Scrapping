import requests
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

def getSoup(url):
    try:
        page = requests.get(url)
    except HTTPError as e:
        return None
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


soup = getSoup('https://pythonscraping.com/pages/page3.html')
if soup == None:
    print("Page couldn't be found")
else:
    for img in soup.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')}):
        print(img['src'])