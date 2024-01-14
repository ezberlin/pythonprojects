import requests
import json
import access

accessId = access.password


latitude = input("Latitude ")
longitude = input("Longitude ")

api_url = "https://vbb.demo.hafas.de/fahrinfo/restproxy/2.32/location.nearbystops"
params = {"format": "json", "accessId":accessId, "originCoordLat":latitude, "originCoordLong":longitude, "maxNo":"1"}
response = requests.get(api_url, params=params)
response.encoding = 'utf-8'
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)
try:
    location = response.json()["stopLocationOrCoordLocation"][0]["StopLocation"]["name"]
    print(location)
except KeyError:
    print("Kein Bahnhof im 1km Radius lol")
