import requests

def weather():
    api_key = "f58181550606418980f192251251611"
    city="solan"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(url)
    data = response.json()

    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    return f"{temp} °C {condition}"





