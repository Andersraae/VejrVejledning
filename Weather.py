import Import as Import

print(Import.getWeather().text)
print(Import.getLocation().text)

def sortInfo():

    weather = Import.getWeather().text
    location = Import.getLocation().text
    location = location["longitude","latitude","accuracyRadius"] #Hvorfor virker det her ikke?



    return location

sortInfo()
