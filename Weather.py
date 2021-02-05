import Import as Import

def sortInfo():

    location = Import.getLocation()
    city = location["countryCapital"]
    returnLocation = [round(location["longitude"],2), round(location["latitude"],2)]
    accuracyRadius = location["accuracyRadius"]

    weather = Import.getWeather(city, returnLocation[0], returnLocation[1])
    print(weather)
    temp = weather["main"]["temp"] - 273,15
    visibility = weather["visibility"]
    wind = weather["wind"]["speed"]

    dict = {"city": city, "returnLocation": returnLocation, "accuracyRadius": accuracyRadius, "temp": temp, "visibility": visibility, "wind": wind}

    return dict
