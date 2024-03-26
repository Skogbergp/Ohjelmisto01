import requests

try:
    request = "https://api.chucknorris.io/jokes/random"


    response = requests.get(request)
    if response.status_code == 200:
        print(response.json()["value"])
    else:
        print("No joke found")
except requests.exceptions.ConnectionError:
    print("Connection Failed")