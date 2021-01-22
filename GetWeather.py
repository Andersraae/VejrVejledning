import Import as Import

print(Import.getWeather().text)
print(Import.getLocation().text)

def sortInfo():

    location = Import.getLocation().text
    location = location["longitude","latitude"]
    weather = Import.getWeather([]).text

    return location

sortInfo()
