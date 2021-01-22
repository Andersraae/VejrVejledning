import Import as Import

print(Import.getWeather())
print(Import.getLocation())

def sortInfo():

    weather = Import.getWeather()
    location = Import.getLocation()
    location = location["longitude"]

    print(location)

    return location

sortInfo()
