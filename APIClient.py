import requests
from pprint import pprint

def main():
    city = 'Warsaw'
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=e4164bc6c9e7305bfecf321bfd6222b1&units=metric')
    weather = response.json()
    #pprint(weather)
    print('The weather for: ', weather['name'],' (', weather['coord']['lon'], ', ', weather['coord']['lat'], ')')
    print(weather['main']['temp'])
    print(weather['weather'][0]['description']) # zero, bo to 1 item na liście, która jest słownikiem

if __name__ == '__main__':
    main()