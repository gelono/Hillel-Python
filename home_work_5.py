import requests

# 1. Вивести список всіх астронавтів, що перебувають в даний момент на орбіті (http://api.open-notify.org/astros.json)

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
status = response.status_code
if status == 200:
    data = response.json()
    list_of_names = data['people']
    for i in range(len(list_of_names)):
        print(list_of_names[i]['name'])
else:
    print('The astronaut data not available')

# 2. Апі погоди. Роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране

city_name = input('Enter city, please: ')
url_new = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
response_new = requests.get(url_new)
status_new = response_new.status_code
if status_new == 200:
    data_new = response_new.json()
    temperature = data_new["main"]["temp"]
    wind_speed = data_new["wind"]["speed"]
    name_of_the_city = data_new["name"]
    print(f'At the moment, in {name_of_the_city} air temperature is {temperature} degrees Celsius, the wind speed is '
          f'{wind_speed} meters per second')
else:
    print('The city is not found')