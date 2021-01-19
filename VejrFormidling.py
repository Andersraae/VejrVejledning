import ImportWeather as Import

print(Import.getWeather().text)
print(Import.getLocation().text)

def sortInfo():

    location = Import.getLocation(["longitude","latitude"]).text

    return location

sortInfo()
