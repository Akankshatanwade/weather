import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
        else:
            print(f"Error: {data['message']}")

    except requests.ConnectionError:
        print("Error: Unable to connect to the weather service.")

def main():
    api_key = "9e6fea3072425506e6c694675d4f3b81"
    location = input("Enter city name or ZIP code: ")
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
