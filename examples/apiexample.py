import urllib.request, urllib.parse, urllib.error
import json

def apiex():
    serviceUrl = 'http://maps,googleapis.com/maps/api/geocode/json?'
    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        url = serviceUrl + urllib.parse.urlencode({'address':address})
        print('Retrieving', url)
        urlHandle = urllib.request.urlopen(url)
        data = urlHandle.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==Failure to Retrieve==')
            print(data)
            continue

        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('latitude', lat, 'longitude', lng)
        location = js['results'][0]['formatted address']
        print(location)

