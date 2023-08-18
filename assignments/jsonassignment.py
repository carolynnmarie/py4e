import urllib.request, urllib.parse, urllib.error
import ssl
import json

def parseJson():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter location: ')
    data = urllib.request.urlopen(url).read()

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

if __name__ == '__main__':
    parseJson()


