import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

def xmlCount():
    ctx()
    data = url()

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    listTwo = []
    for item in counts:
        x = item.text
        listTwo.append(int(x))
    total = sum(listTwo)
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
    xmlCount()

