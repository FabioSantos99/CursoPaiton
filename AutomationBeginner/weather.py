import requests

API_KEY = "cca7198fc5eb0b143055b5c6a6994d23"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")


