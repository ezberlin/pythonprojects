import requests
import json
import access

accessId = access.password



api_url = "https://vbb.demo.hafas.de/fahrinfo/restproxy/2.32/departureBoard"
params = {"format": "json", "accessId":accessId, "id":"A=1@O=Lehniner Platz/Schaubühne (Berlin)@X=13301806@Y=52498927@U=86@L=900040151@"}
response = requests.get(api_url, params=params)
response.encoding = 'utf-8'
print(response.url)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

