import urllib.request, urllib.parse, urllib.error
import ssl
import json

def parseJson():

    data = url()
    try:
        js = json.loads(data)
    except:
        js = None

    counts = []
    lst = js["comments"]
    for item in lst:
        counts.append(int(item["count"]))
    total = sum(counts)
    print(total)

def url():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter location: ')
    return urllib.request.urlopen(url).read()

if __name__ == '__main__':
    parseJson()


