import json
import requests
import datetime


class DailyWeather:
    def __init__(self, date, temp, fl_temp, min_temp, max_temp, main, description, icon):
        self.date = date
        self.temp = temp
        self.fl_temp = fl_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.main = main
        self.description = description
        self.icon = icon

    def format_date(self):
        return str(datetime.datetime.fromtimestamp(self.date).strftime("%A %d %B %Y %X"))

    def icon_url(self):
        return str("http://openweathermap.org/img/wn/" + self.icon + "@2x.png")


url = "https://api.openweathermap.org/data/2.5/forecast?id=5128581&units=metric&appid=13d9ee2004755a6ace5f0a696af3e351"
api_call = requests.get(url).json()

weather_list = []

for i in range(len(api_call["list"])):
    weather_list.append(DailyWeather(api_call["list"][i]["dt"],
                        api_call["list"][i]["main"]["temp"],
                        api_call["list"][i]["main"]["feels_like"],
                        api_call["list"][i]["main"]["temp_min"],
                        api_call["list"][i]["main"]["temp_max"],
                        api_call["list"][i]["weather"][0]["main"],
                        api_call["list"][i]["weather"][0]["description"],
                        api_call["list"][i]["weather"][0]["icon"]))

for data in weather_list:
    print(data.format_date(), " - ", data.temp, " - ", data.main)



# print(datetime.datetime.fromtimestamp(api_call["list"][i]["dt"]).strftime("%A %d %B %Y - %X"))

# print(api_call["list"][0]["weather"][0]["icon"])
