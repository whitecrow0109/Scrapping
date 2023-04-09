from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        page = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(page.read(), 'html.parser')
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print("Title couldn't be found")
else:
    print(title)