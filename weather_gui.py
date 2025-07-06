from tkinter import *
import requests

def get_weather(city):
    api_key = "fe67724f1eae88b8f4c7d87ec2cabc7b"  
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

from datetime import datetime

def fetch_weather():
    city = city_entry.get()
    data = get_weather(city)
    
    
    if "error" in data:
        result.set(f"Error: {data['error']}")
    elif data["cod"] == 200:
        # Extract weather details
        city_name = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        # Convert UNIX time to readable time
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

        # Display results
        result.set(f"City: {city_name}\n"
                   f"Temp: {temp}°C\n"
                   f"Humidity: {humidity}%\n"
                   f"Weather: {description}\n"
                   f"Wind: {wind_speed} m/s\n"
                   f"Sunrise: {sunrise}\n"
                   f"Sunset: {sunset}")
    else:
        result.set("City not found.")

# GUI setup
app = Tk()
app.title("Weather App")
app.geometry("300x250")

Label(app, text="Enter City Name:").pack(pady=10)
city_entry = Entry(app)
city_entry.pack()

Button(app, text="Get Weather", command=fetch_weather).pack(pady=10)

result = StringVar()
Label(app, textvariable=result, wraplength=250).pack(pady=10)

app.mainloop()
