from decimal import Decimal

import matplotlib.pyplot as plt
import base64
from io import BytesIO
import time

from .get_city_weather import get_hourly_forecast


# интерактивный вывод пирога
def get_pie():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph


# интерактивный вывод столбчатой диаграммы
def get_bar_chart(api_key):
    plt.switch_backend('AGG')
    chart_data = get_hourly_forecast(api_key)
    x = []
    y = []
    # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # y = [1000, 2000, 3000, 4000, 5000, 3000, 2000, 1500, 1000, 5000, 6000, 15]

    for i in chart_data:
        x.append(i['time'])
        y.append(int(i['temperature']))


    fig, ax = plt.subplots()

    ax.bar(x, y)
    ax.set_facecolor('seashell')
    fig.set_facecolor('#afeeee')  # color of the background
    bar_chart = get_pie()

    return bar_chart
