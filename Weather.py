import Import as Import

print(Import.getLocation())

def sortInfo():

    location = Import.getLocation()
    returnLocation = [location["longitude"], location["latitude"]]
    accuracyRadius = location["accuracyRadius"]

    weather = Import.getWeather(returnLocation[0],returnLocation[1])

    return returnLocation

returnLocation = sortInfo()
print(returnLocation[0],returnLocation[1])
