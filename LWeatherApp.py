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
    cityName = StringVar()
    days = StringVar()

    IPcheck = Checkbutton(frame, text='Get weather via IP',fg='lime',bg='black', variable=UseIP, onvalue='True',offvalue='False', font=('Helvetica',12))
    
    cityLbl = Label(frame, text='City:', fg='lime', bg='black', font=('Helvetica',12))
    cityEntry = Entry(frame)

    dayLbl = Label(frame, text='Days:', fg='lime' ,bg='black', font=('Helvetica',12))
    dayEntry = Entry(frame)

    submitBtn = Button(frame, text='Submit',fg='lime',bg='black',padx=10,command=checkInput('blach',2))


    IPcheck.place(x=50,y=50)
    cityLbl.place(x=50,y=100)
    cityEntry.place(x=100,y=102)
    dayLbl.place(x=50,y=150)
    dayEntry.place(x=100,y=152)
    submitBtn.place(relx=.5,rely=.5,anchor=CENTER)
    

def checkInput(city,day=1):
    print(city, ' ', day)

def showWeather():
    pass

root = Tk()
root.title('LWeatherApp')
#lwa = LWeatherApp(root)
root.geometry('400x500')
root.attributes('-alpha', 1)

frame = Frame(root)
frame.configure(bg='black')
frame.pack(side="top",expand=True,fill='both')
getLocation()
root.mainloop()