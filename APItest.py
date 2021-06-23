import requests
import json
import os

url = 'http://api.weatherapi.com/v1/current.json'
api_key = 'fa7c0abb05f54f38a2832828212206'

params = {
    'key': api_key
}

#response = requests.get(url, params=params)
#res = response.json()

#print(response.url)
#print(response.status_code,'\n')
#res = response.json()
#print(json.dumps(res, indent=4, sort_keys=True))

'''res = response.json()
print(res,'\n')
x = res['location']
y = x['country']
print(y)'''

def ShowMenu():
    os.system('cls')
    print('1. Get Weather\n2. Exit\n')

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

def promptWeather():
    os.system('cls')
    print('1. Get weather for current location?\n2. Search city?\n3. Exit\n')
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

    if inp == 1:
        params['q'] = 'auto:ip'
    elif inp == 2:
        os.system('cls')
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

def showWeather():
    os.system('cls')
    print('Getting weather...')
    response = requests.get(url, params=params)
    res = response.json()
    os.system('cls')

    current = res['current']
    location = res['location']

    city = location['name']
    country = location['country']
    feelsTempF = current['feelslike_f']
    tempf = current['temp_f']
    windmph = current['wind_mph']
    humidity = current['humidity']

    print('Location: ', city, '\nCountry: ', country)
    print('Temperature: ', tempf, '°F')
    print('Feels like', feelsTempF, '°F')
    print('Windspeed: ', windmph, 'mph')
    print('Humidity: ', humidity, '%\n\n')


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


ShowMenu()
