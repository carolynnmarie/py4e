import urllib.error
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def urlLinks():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL: ')
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    x = 0

    lastNames = []
    while x < count:
        tags = soup('a')
        y = 1
        for tag in tags:
            if y == position:
                lastNames.append(tag.get_text())
                #print(tag.get_text())
                url = tag.get('href', None)
                #print(url)
                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, 'html.parser')
            y = y + 1
        x = x + 1
    print(lastNames[count-1])



if __name__ == '__main__':
    urlLinks()



