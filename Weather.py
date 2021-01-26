import Import as Import

def sortInfo():

    location = Import.getLocation()
    print(location)
    city = location["countryCapital"]
    returnLocation = [round(location["longitude"],2), round(location["latitude"],2)]
    accuracyRadius = location["accuracyRadius"]

    weather = Import.getWeather(city, returnLocation[0], returnLocation[1])
    print(weather)

    return returnLocation

returnLocation = sortInfo()
print(returnLocation[0],returnLocation[1])
