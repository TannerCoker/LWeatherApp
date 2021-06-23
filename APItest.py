import requests
import json
import os

url = 'http://api.weatherapi.com/v1/current.json'
api_key = #WeatherAPI API-key goes here

#dictionary to hold parameters for the search specification
params = {
    'key': api_key
}

#shows the initial menu prompt to open app or exit it
def ShowMenu():
    os.system('cls')
    print('1. Get Weather\n2. Exit\n')

    #error checking to make sure they enter a valid int choice
    while True:
        try:
            inp = int(input('Selection: '))
            if type(inp) is not int:
                print('Invalid input\n')
            elif inp < 1 or inp > 2:
                print('Invalid input\n')
            else:
                break
        except ValueError:
            print('ERROR: Invalid type')
    if inp == 1:
        promptWeather()
    elif inp == 2:
        os.system('cls')
        exit()

#prompts them for if they want to get weather for current location, via IP, or search a city name
def promptWeather():
    os.system('cls')
    print('1. Get weather for current location?\n2. Search city?\n3. Exit\n')
    
    #Error checking for valid input
    while True:
        try:
            inp = int(input('Selection:'))
            if type(inp) is not int:
                print('Invalid input\n')
            elif inp < 1 or inp > 3:
                print('Invalid input\n')
            else:
                break
        except ValueError:
            print('ERROR: Invalid type\n')

    #setting parameters for what city to pull data from
    if inp == 1:
        #search based on IP
        params['q'] = 'auto:ip'
    elif inp == 2:
        os.system('cls')
        #get city name and set that to search parameter
        while True:
            City = input('City: ')
            if isinstance(City, str):
                params['q'] = City
                break
            else:
                print('Invalid type\n')
    elif inp == 3:
        os.system('cls')
        exit()

    showWeather()

#display the weather based on search conditions
def showWeather():
    os.system('cls')
    print('Getting weather...')
    
    #grabbing the JSON information from WeatherAPI
    response = requests.get(url, params=params)
    res = response.json()
    os.system('cls')

    #storing information into variables
    current = res['current']
    location = res['location']
    
    city = location['name']
    country = location['country']
    feelsTempF = current['feelslike_f']
    tempf = current['temp_f']
    windmph = current['wind_mph']
    humidity = current['humidity']

    #print information to console
    print('Location: ', city, '\nCountry: ', country)
    print('Temperature: ', tempf, '°F')
    print('Feels like', feelsTempF, '°F')
    print('Windspeed: ', windmph, 'mph')
    print('Humidity: ', humidity, '%\n\n')


    #prompt to search another city or to exit
    print('---------------------------------------------\n')
    print('1. Get weather for a new location?\n2. Exit\n')
    while True:
        try:
            inp = int(input('Selection:'))
            if type(inp) is not int:
                print('Invalid input\n')
            elif inp < 1 or inp > 2:
                print('Invalid input\n')
            else:
                break
        except ValueError:
            print('ERROR: Invalid type\n')
    if inp == 1:
        promptWeather()
    elif inp == 2:
        os.system('cls')
        exit()

#start prog
ShowMenu()
