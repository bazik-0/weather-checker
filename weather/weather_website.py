import streamlit as st
import requests

try:
    st.title("🌤️ Weather App")

    api_key = "3a0e27b3c1aebc319b169d9ccd3c03b3"


    city_name = st.text_input("Enter city name:")


    if st.button("Get Weather"):
        if city_name.strip() == "":
            st.warning("Please enter a city name!")
        else:
            url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}&units=metric"
            info = requests.get(url)
            data = info.json()

            if info.status_code == 200:
                weather = data["weather"][0]["main"]
                temp = round(data["main"]["temp"], 1)
                humidity = data["main"]["humidity"]
                country = data["sys"]["country"]
                wind = data["wind"]["speed"]

                st.success(f"Weather in {city_name}, {country}:")
                st.write(f"Condition: {weather}")
                st.write(f"Temperature: {temp}°C")
                st.write(f"Humidity: {humidity}%")
                st.write(f"Wind Speed: {wind} m/s")
            else:
                st.error("City not found 😢 Please check spelling!")

except Exception as e :
    print ("something went wrong ", e )