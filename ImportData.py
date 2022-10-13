import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"London","days":"3"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
