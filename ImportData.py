import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"London","days":"3"}

headers = {
    'x-rapidapi-key': "a6bf1992eamsh73f99bb10e52ff4p1f181djsnb1ae54ef1d78",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
