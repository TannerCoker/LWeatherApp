import requests
import json
import os
from tkinter import *

#base URL for API site
url = 'http://api.weatherapi.com/v1/current.json'

#retrieve the API_KEY from config file
'''with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    API_KEY = data['config']['API_KEY']'''



#dictionary to hold parameters for the search specification
'''params = {
    'key': API_KEY,
}'''

bgColor = 'royal blue'
letColor = 'mint cream'

def getLocation():
    UseIP = StringVar()
    cityName = StringVar()
    days = StringVar()

    IPcheck = Checkbutton(frame, text='Get weather via IP',fg=letColor,bg=bgColor, variable=UseIP, onvalue='True',offvalue='False', font=('Helvetica',12,'bold'))

    cityLbl = Label(frame, text='City:', fg=letColor, bg=bgColor, font=('Helvetica',12,'bold'))
    cityEntry = Entry(frame)

    dayLbl = Label(frame, text='Days:', fg=letColor ,bg=bgColor, font=('Helvetica',12,'bold'))
    dayEntry = Entry(frame)

    submitBtn = Button(frame, text='Submit',fg=letColor,bg=bgColor,padx=10,command=checkInput('blach',2))


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
frame.configure(bg=bgColor)
frame.pack(side="top",expand=True,fill='both')
getLocation()
root.mainloop()
