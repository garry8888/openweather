import requests
import time
import json


def get_hourly_forecast(api_key):
    url = "https://api.openweathermap.org/data/3.0/onecall?lat=51.1263106&" \
          "lon=16.97819633051261&exclude=minutely,daily&units=metric&"
    payload = {}
    headers = {}
    response = requests.request("GET", url + api_key, headers=headers, data=payload)
    json_data = json.loads(response.text)
    rough_hourly_data = json_data['hourly']
    filtered_data = []

    for i in rough_hourly_data:
        filtered_data.append(dict(date=time.strftime("%D %H:%M", time.localtime(int(i['dt']))),
                                  time=time.strftime("%H", time.localtime(int(i['dt']))),
                                  temperature=i['temp'],
                                  feels_like=i['feels_like'],
                                  wind_speed=i['wind_speed'],
                                  description=[x['description'] for x in i['weather']][0]
                                  ))

    return filtered_data
