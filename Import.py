import requests

def getWeather():

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"en","units":"\"metric\"","mode":"xml, html"}

    headers = {
        'x-rapidapi-key': "a6bf1992eamsh73f99bb10e52ff4p1f181djsnb1ae54ef1d78",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    responseWeather = requests.request("GET", url, headers=headers, params=querystring)

    return responseWeather

def getLocation():

    url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

    querystring = {"apikey":"873dbe322aea47f89dcf729dcc8f60e8"}

    headers = {
        'x-rapidapi-key': "a6bf1992eamsh73f99bb10e52ff4p1f181djsnb1ae54ef1d78",
        'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
        }

    responseLocation = requests.request("GET", url, headers=headers, params=querystring)

    return responseLocation
