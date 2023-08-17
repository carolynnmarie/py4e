import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

def xmlCount():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL: ')
    data = urllib.request.urlopen(url).read()

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    listTwo = []
    for item in counts:
        x = item.text
        listTwo.append(int(x))
    total = sum(listTwo)
    print(total)

if __name__ == '__main__':
    xmlCount()

