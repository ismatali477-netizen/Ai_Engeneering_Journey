import os
import requests
from tkinter import *

base_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(base_dir, "secret_api")

keys = {}
if os.path.exists(key_path):
    with open(key_path, "r") as file:
        for line in file:
            if "=" in line:
                name, value = line.strip().split("=", 1)
                keys[name.strip()] = value.strip().strip('"').strip("'")

WEATHER_API_KEY = keys.get("WEATHER_API_KEY","")

class WeatherApp:
    def __init__(self):
        self.load_gui()
        self.root.mainloop()

    def load_gui(self):
        self.root = Tk()
        self.root.title("Weather App")
        self.root.geometry("300x400")
        self.root.resizable(0, 0)
        self.root.configure(bg="#7ce1f0")

        # City Input Label
        self.input_city_label = Label(self.root, text="Enter City Name:",  bg="#7ce1f0", fg="black", font=("verdana", 10, "bold"))
        self.input_city_label.pack(pady=(20, 10))

        # City Input Entry Box
        self.input_city_entry = Entry(self.root, width=25)
        self.input_city_entry.pack(pady=(0, 20))

        # Get Weather Button
        self.input_city_btn = Button(self.root, text="Get Weather", bg="#f9e720", fg="black", font=("verdana", 10, "bold"), command=self.on_get_weather)
        self.input_city_btn.pack(pady=(0, 20))

        # Weather Information Display Label
        self.weather_info_label = Label(self.root, text="", bg="#7ce1f0", fg="black", font=("verdana", 10), wraplength=250, justify="center")
        self.weather_info_label.pack(pady=(0, 20))

    def get_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        try:
            response = requests.get(url, timeout=5)
            return response.json()
        except Exception:
            return None

    def on_get_weather(self):
        city = self.input_city_entry.get().strip()
        
        if not city:
            self.weather_info_label.config(text="Please enter a city name.")
            return

        weather_data = self.get_weather(city)

        if weather_data and weather_data.get("cod") == 200:
            temp = weather_data['main']['temp']
            desc = weather_data['weather'][0]['description'].title()
            weather_info = f"Temperature: {temp}°C\nDescription: {desc}"
            self.weather_info_label.config(text=weather_info)
        elif weather_data and weather_data.get("message"):
            self.weather_info_label.config(text=weather_data['message'].title())
        else:
            self.weather_info_label.config(text="Unable to fetch weather data.")


if __name__ == "__main__":
    app = WeatherApp()