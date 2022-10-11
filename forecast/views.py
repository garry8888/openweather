from openweather_app.env import env
from django.shortcuts import render

from forecast.chart import get_bar_chart
from forecast.get_city_weather import get_hourly_forecast


def index(request):
    api_id = 'appid=' + env.str('API_KEY')
    gdansk_url = 'https://api.openweathermap.org/data/2.5/weather?q=Gdansk&mode=html&units=metric&{api_key}'\
        .format(api_key=api_id)
    wroclaw_url = 'https://api.openweathermap.org/data/2.5/weather?q=Wroclaw&mode=html&units=metric&{api_key}'\
        .format(api_key=api_id)
    rzeszow_url = 'https://api.openweathermap.org/data/2.5/weather?q=Rzeszow&mode=html&units=metric&{api_key}'\
        .format(api_key=api_id)
    warsaw_url = 'https://api.openweathermap.org/data/2.5/weather?q=Warsaw&mode=html&units=metric&{api_key}'\
        .format(api_key=api_id)
    krakow_url = 'https://api.openweathermap.org/data/2.5/weather?q=Krakow&mode=html&units=metric&{api_key}'\
        .format(api_key=api_id)
    zakopane_url = 'https://api.openweathermap.org/data/2.5/weather?q=Krakow&mode=html&units=metric&{api_key}'.\
        format(api_key=api_id)

    return render(request, 'forecast/city_weather.html', {'gdansk': gdansk_url,
                                                          'wroclaw': wroclaw_url,
                                                          'rzeszow': rzeszow_url,
                                                          'warsaw': warsaw_url,
                                                          'krakow': krakow_url,
                                                          'zakopane': zakopane_url
                                                          })


def hourly_weather(request):
    api_id = 'appid=' + env.str('API_KEY')
    bar_char = get_bar_chart(api_id)
    table_data = get_hourly_forecast(api_id)

    return render(request, 'forecast/hourly_weather.html', {'bar_char': bar_char,
                                                            'table_data': table_data
                                                            })
