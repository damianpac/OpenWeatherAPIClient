import requests
from pprint import pprint

def main():
    city = 'Warsaw'
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=DEFAULTAPPID&units=metric')
    weather = response.json()
    #pprint(weather)
    print('The weather for: ', weather['name'],' (', weather['coord']['lon'], ', ', weather['coord']['lat'], ')')
    print(weather['main']['temp'])
    print(weather['weather'][0]['description'])

if __name__ == '__main__':
    main()
