import Import as Import

def sortInfo():

    location = Import.getLocation()
    city = location["countryCapital"]
    returnLocation = [round(location["longitude"],2), round(location["latitude"],2)]
    accuracyRadius = location["accuracyRadius"]

    weather = Import.getWeather(city, returnLocation[0], returnLocation[1])
    temp = weather["main"]["temp"] - 273,15
    visibility = weather["visibility"]
    wind = weather["wind"]["speed"]

    dict = {"city": city, "returnLocation": returnLocation, "accuracyRadius": accuracyRadius, "temp": temp, "visibility": visibility, "wind": wind}

    return dict

def dangerRating():

    dict = sortInfo()
    if dict["wind"] > 3:
        windDanger = 1
    elif dict["wind"] > 8:
        windDanger = 2
    elif dict["wind"] > 15:
        windDanger = 3
    elif dict["wind"] > 20:
        windDanger = 4
    elif dict["wind"] < 20:
        windDanger = 5
    else:
        print("ERROR: windDanger")

    if dict["visibility"] > 500:
        visibilityDanger = 5
    elif dict["visibility"] > 2000:
        visibilityDanger = 4
    elif dict["visibility"] > 5000:
        visibilityDanger = 3
    elif dict["visibility"] > 10000:
        visibilityDanger = 2
    elif dict["visibility"] < 10000:
        visibilityDanger = 1
    else:
        print("ERROR: visibilityDanger")

    return windDanger, visibilityDanger
