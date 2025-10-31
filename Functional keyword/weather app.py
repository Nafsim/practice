import requests
def weather(city):
    api_key = "fcc4b276c1ce223e5b528e14180770a5"  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Max Temperature: {main['temp_max']}°C")
        print(f"Min Temperature: {main['temp_min']}°C")
        print(f"Weather: {weather['main']} - {weather['description']}")
    else:
        print("Invalid city name.")

def main():
    while True:
        city = input("\nEnter city name : ")
        if city.lower() == "exit":
            print("Exiting this app.")
            break
        weather(city)

if __name__ == "__main__":
    main()
