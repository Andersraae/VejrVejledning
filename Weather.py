import Import as Import

def sortInfo():

    location = Import.getLocation()
    returnLocation = [location["longitude"], location["latitude"]]
    accuracyRadius = location["accuracyRadius"]

    weather = Import.getWeather(returnLocation[0],returnLocation[1])
    print(weather)

    return returnLocation

returnLocation = sortInfo()
print(returnLocation[0],returnLocation[1])
