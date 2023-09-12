import json
import requests
import PySimpleGUI as sg

location = "indianapolis"
apikey = "9xi9ZXm6xNUKDVQDS6DQKsiwtuJMJb61"
units= "imperial"
calltype = "realtime"

#URL used to call the API
url = f'https://api.tomorrow.io/v4/weather/{calltype}?location={location}&units={units}&apikey={apikey}'

#Headers used for calling the API
headers = {"accept": "application/json"}

#Variable for holding the response recieved and the actual request to the API
response = requests.get(url, headers=headers)

print(response.text)
print()

wjson = response.text
wjdata = json.loads(wjson)

#Json probe tests
for i in wjdata:
    print(i)
    print(wjdata["data"]["values"][i])

"""
values returned in json format from the API

data:{
    time:
    values:{
        cloudBase:
        cloudCeiling:
        cloudCover:
        dewPoint:
        freezingRainIntensity:
        humidity:
        precipitationProbability:
        pressureSurfaceLevl:
        rainIntensity:
        sleetIntensity:
        snowIntensity:
        temperature:
        temeratureApparent:
        uvHealthConcern:
        uvIndex:
        visibility:
        weatherCode:
        windDirection:
        windGust:
        windSpeed:
    }
    location:{
        lat:
        lon:
        name:1,2,3,4
        type:
    }
}
"""