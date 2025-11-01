import requests
try:
    a = "yes" 
    def weather_app():
        api_key = "3a0e27b3c1aebc319b169d9ccd3c03b3"

        city_name = input("Enter city name : ")

        url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}"
        
        info = requests.get(url)
        data = info.json()
        
        if info.status_code == 200 :
            weather = data["weather"][0]["main"]
            temperature_1 = data["main"]["temp"]
            temperature_2 = int(temperature_1) - 273
            humid = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            print(f'''Weather in {city_name} 🌞 
Condition : {weather}
Temperature : {temperature_2}°C
Humidity : {humid}%
Wind Speed: {wind} m/s
''')
        else:
            print("Soory i cant find you city please check you spelling ")
        global a 
        a = input("Want to check weather of another place (yes/no) ").lower()
    while a =="yes" :
        weather_app()
    else :
        print("Good bye ")

except Exception as e :
    print("something went wrong ")