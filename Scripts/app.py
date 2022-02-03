from flask import Flask, render_template
import json
import requests
import datetime


# Dictionary of cities available - city ID
city_list = {"Amsterdam": "2759794",
             "Berlin": "2950159",
             "Hong Kong": "1819729",
             "London": "2643743",
             "New York": "5128581",
             "Paris": "2988507",
             "Seoul": "1835848",
             "Shanghai": "1796236",
             "Singapore": "1880252",
             "Tokyo": "1850147"}


# Object for each cities weather information - goes to a list - class
class DailyWeather:
    def __init__(self, name, date, temp, fl_temp, min_temp, max_temp, main, description, icon):
        self.name = name
        self.date = date
        self.temp = temp
        self.fl_temp = fl_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.main = main
        self.description = description
        self.icon = icon

    # Returns the date formatted string
    def format_date(self):
        return str(datetime.datetime.fromtimestamp(self.date).strftime("%d %b %Y"))

    # Returns the day of the week string
    def day_of_week(self):
        return str(datetime.datetime.fromtimestamp(self.date).strftime("%A"))

    # Returns the completed icon url string
    def icon_url(self):
        return str("http://openweathermap.org/img/wn/" + self.icon + "@2x.png")


# Calls API and gets the weather data for specified city ID
def api_get(id_no):
    url = "https://api.openweathermap.org/data/2.5/forecast?id=" + id_no + "&units=metric&appid=13d9ee2004755a6ace5f0a696af3e351"
    api_call = requests.get(url).json()
    weather_list = []

    # Loop through every day - create object - add to list
    for i in range(len(api_call["list"])):
        weather_list.append(DailyWeather(api_call["city"]["name"],
                                         api_call["list"][i]["dt"],
                                         api_call["list"][i]["main"]["temp"],
                                         api_call["list"][i]["main"]["feels_like"],
                                         api_call["list"][i]["main"]["temp_min"],
                                         api_call["list"][i]["main"]["temp_max"],
                                         api_call["list"][i]["weather"][0]["main"],
                                         api_call["list"][i]["weather"][0]["description"],
                                         api_call["list"][i]["weather"][0]["icon"]))

    # Returns the list of classes
    return weather_list


# Create the Flask App
app = Flask(__name__, template_folder="templates", static_folder="static")


# Route with city ID passed in
@app.route("/weather/<location>", methods=["GET"])
def index(location):
    return render_template("index.html",
                           weather_data=api_get(location),
                           cities=city_list)
