import requests
import json
def cutLocation(location):
    percent = False
    newLocation = ""
    for character in location:
        if percent:
            newLocation += character
        if character == "%":
            percent = True
    return newLocation.strip()


latitude = input("Latitude ")
longitude = input("Longitude ")

api_url = "https://vbb.demo.hafas.de/fahrinfo/restproxy/2.32/location.nearbystops"
params = {"format": "json", "accessId":"accesId", "originCoordLat":latitude, "originCoordLong":longitude, "maxNo":"1"}
response = requests.get(api_url, params=params)
response.encoding = 'utf-8'
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)
try:
    location = cutLocation(response.json()["stopLocationOrCoordLocation"][0]["StopLocation"]["LocationNotes"]["LocationNote"][-1]["value"])
    print(location)
except KeyError:
    print("Kein Bahnhof im 1km Radius lol")
