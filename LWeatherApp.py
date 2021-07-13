import requests
import json
import os
from tkinter import *

#base URL for API site
url = 'http://api.weatherapi.com/v1/current.json'

#retrieve the API_KEY from config file
with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    API_KEY = data['config']['API_KEY']

#dictionary to hold parameters for the search specification
params = {
    'key': API_KEY,
}


def getLocation():
    pass

def showWeather():
    pass

root = Tk()
#lwa = LWeatherApp(root)
root.geometry('400x500')
frame = Frame(root)
frame.pack()
root.mainloop()