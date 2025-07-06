# weather_cli.py

import requests

def get_weather(city):
    api_key = "fe67724f1eae88b8f4c7d87ec2cabc7b"  
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def display_weather(data):
    if data and data["cod"] == 200:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)
