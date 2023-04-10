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


soup = getSoup('https://www.pdfdrive.com/living-in-the-light-a-guide-to-personal-transformation-e10172273.html')
if soup == None:
    print("Page couldn't be found")
else:
    for link in soup.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])