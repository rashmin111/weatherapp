import os
import requests
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

# Retrieve the API key securely
API_KEY = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter city: ")  # e.g., Ahmedabad,IN or Nadiād,IN
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f"Temp: {temp}°C, Description: {desc}")
else:
    print("City not found or API error!")
