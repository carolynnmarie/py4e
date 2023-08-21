import urllib.request, urllib.parse, urllib.error
import json
import ssl

def getGeoJson():
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        params = dict()
        params['address'] = address
        params['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(params)
        print('Retrieving url:', url)

        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        print(js["results"][0]["place_id"])


if __name__ == '__main__':
    getGeoJson()

