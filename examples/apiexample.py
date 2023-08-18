import urllib.request, urllib.parse, urllib.error
import json
import ssl
import augment

def googleapiex():
    serviceUrl = 'http://maps,googleapis.com/maps/api/geocode/json?'
    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        url = serviceUrl + urllib.parse.urlencode({'address': address})
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

        print(json.dumps(js, indent=4))

        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('latitude', lat, 'longitude', lng)
        location = js['results'][0]['formatted address']
        print(location)


def oauth():
    return {"consumer_key": "h7Lu...Ng",
            "consumer_secret":"dNKenAC3New...mmn7Q",
            "token_key": "100185562...P4GEQQ005GI",
            "token_secret": "H0yCFemmC4wyf1...qoIqBo"}

def twitterapiex():
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'drchuck', 'count': '2'})
    print(url)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read
    print(data)

    headers = dict(connection.getheaders())
    print(headers)