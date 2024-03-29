import requests
import json

def getWeather(lat, lon):

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"lat":"{}".format(lat),"lon":"{}".format(lon),"lang":"en","units":"\"metric\"","mode":""}

    headers = {
        'x-rapidapi-key': "a6bf1992eamsh73f99bb10e52ff4p1f181djsnb1ae54ef1d78",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    responseWeather = requests.request("GET", url, headers=headers, params=querystring)

    if responseWeather.status_code == 200:
        responseWeather = json.loads(responseWeather.text)

    return responseWeather


def getLocation():

    url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

    querystring = {"apikey":"873dbe322aea47f89dcf729dcc8f60e8"}

    headers = {
        'x-rapidapi-key': "a6bf1992eamsh73f99bb10e52ff4p1f181djsnb1ae54ef1d78",
        'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
        }

    responseLocation = requests.request("GET", url, headers=headers, params=querystring)

    if responseLocation.status_code == 200:
        responseLocation = json.loads(responseLocation.text)

    return responseLocation
