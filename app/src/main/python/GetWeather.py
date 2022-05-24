'''
This file will just be hardcoded to sunnyvale at the moment. Full functionality will be made sooner or later
'''

import requests
import json

def main():
    API_key = "Your API key goes here"
    CITY = "Sunnyvale"

    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_key}&q={CITY}&days=3&aqi=no&alerts=no"

    re = requests.get(url)

    page = json.loads(re.text)

    retVal = (f"Current Weather: {page['current']['temp_f']} degrees F\nChance of rain: {page['forecast']['forecastday'][0]['day']['daily_chance_of_rain']} percent\nTomorrows chance of rain: {page['forecast']['forecastday'][1]['day']['daily_chance_of_rain']} percent\nTwo days from now chance of rain: {page['forecast']['forecastday'][2]['day']['daily_chance_of_rain']}")

    return retVal

'''
todays date: "Current Weather: ", page["current"]["temp_f"], "degrees F\nChance of rain:", page["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]

tommorrow: "Tomorrow's chance of rain:", page["forecast"]["forecastday"][1]["day"]["daily_chance_of_rain"]

The day after: "Two days from now chance of rain:", page["forecast"]["forecastday"][2]["day"]["daily_chance_of_rain"]
'''

