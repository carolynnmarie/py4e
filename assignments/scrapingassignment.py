import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def scraping():

    ctx()
    soup = url()
    count = []
    tags = soup('span')
    for tag in tags:
        val = int(tag.get_text())
        count.append(val)
    total = sum(count)
    print(total)

def ctx():
    ctX = ssl.create_default_context()
    ctX.check_hostname = False
    ctX.verify_mode = ssl.CERT_NONE

def url():
    url = input('Enter - ')
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    scraping()
