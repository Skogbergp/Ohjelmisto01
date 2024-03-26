import requests
from geopy.geocoders import Nominatim


try:
    geolocator = Nominatim(user_agent="Weather app")
    location = geolocator.geocode(input("Enter location: "))
    api = #your api key

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api}&units=metric"

    result = requests.get(url)
    if result.status_code == 200:
        result = result.json()
        print(f"{result["weather"][0]["description"]}")
        print(f"{result["main"]["temp"]}\xb0C")

except requests.exceptions.ConnectionError:
    print("request failed")
except Exception as e:
    print(e)