# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 11:12:55 2025

@author: Krishna
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load trained model
w = pickle.load(open(r'C:\internship\sav\weather(logistic).sav', 'rb'))


def predict_weather(input_data):
    prediction = w.predict([input_data])[0]
    
    if prediction == 0:
        return "Cloudy"
    elif prediction == 1:
        return "Rainy"
    elif prediction == 2:
        return "Snowy"
    elif prediction == 3:
        return "Sunny"
    else:
        return "Unknown"


def main():
    st.title("🌤 Weather Data Prediction App")

    # Numeric inputs
    temperature = st.text_input("Temperature (°C)").strip()
    humidity = st.text_input("Humidity (%)").strip()
    wind_speed = st.text_input("Wind Speed (km/h)").strip()
    precipitation = st.text_input("Precipitation (%)").strip()
    pressure = st.text_input("Atmospheric Pressure (hPa)").strip()
    uv_index = st.text_input("UV Index").strip()
    visibility = st.text_input("Visibility (km)").strip()

    # Previously dropdowns — now numeric inputs
    cloud_cover_val = st.text_input("Cloud Cover (0=overcast, 1=partly cloudy, 2=clear, 3=cloudy)").strip()
    season_val = st.text_input("Season (0=Winter, 1=Spring, 2=Autumn, 3=Summer)").strip()
    location_val = st.text_input("Location (0=inland, 1=mountain, 2=coastal)").strip()

    if st.button("Get Weather Prediction"):
        try:
            # Convert inputs to floats
            input_list = [
                float(temperature),
                float(humidity),
                float(wind_speed),
                float(precipitation),
                float(pressure),
                float(uv_index),
                float(visibility),
                float(season_val),
                float(location_val),
                float(cloud_cover_val)
            ]

            st.write("🔍 Input to model:", input_list)

            prediction = predict_weather(input_list)
            diagnosis = f"✅ Weather prediction result: {prediction}"

        except Exception as e:
            st.error(f"❌ Error: {e}")
        else:
            st.success(diagnosis)

if __name__ == "__main__":
    main()
