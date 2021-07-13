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
    UseIP = StringVar()
    IPcheck = Checkbutton(frame, text='Get weather via IP', variable=UseIP, onvalue='True',offvalue='False', font=('Helvetica',12))
    
    cityLbl = Label(frame, text='City:', fg='black', font=('Helvetica',12))
    IPcheck.place(x=50,y=50)
    cityLbl.place(x=50,y=100)

def checkInput():
    pass

def showWeather():
    pass

root = Tk()
root.title('LWeatherApp')
#lwa = LWeatherApp(root)
root.geometry('400x500')
frame = Frame(root)
frame.pack(side="top",expand=True,fill='both')
getLocation()
root.mainloop()