import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Simple Weather Prediction App
# -----------------------------

st.set_page_config(page_title="Weather Prediction App", page_icon="🌦️", layout="centered")

st.title("🌦️ Weather Prediction App")
st.write("A simple machine learning app to predict weather conditions (Sunny, Rainy, Cloudy).")

# Load a sample model or simulate one
try:
    model = pickle.load(open("weather_model.pkl", "rb"))
except:
    model = None

# User input
st.subheader("Enter Weather Parameters:")

temp = st.slider("Temperature (°C)", -10, 45, 25)
humidity = st.slider("Humidity (%)", 0, 100, 60)
pressure = st.slider("Pressure (hPa)", 950, 1050, 1013)
wind_speed = st.slider("Wind Speed (km/h)", 0, 50, 10)

# Prediction logic
def predict_weather(temp, humidity, pressure, wind_speed):
    """
    Simple rule-based or ML-based prediction
    """
    if model:
        data = np.array([[temp, humidity, pressure, wind_speed]])
        prediction = model.predict(data)[0]
        return prediction
    else:
        # Rule-based fallback
        if humidity > 80 and temp < 25:
            return "Rainy 🌧️"
        elif temp > 30 and humidity < 60:
            return "Sunny ☀️"
        else:
            return "Cloudy ⛅"

if st.button("Predict Weather"):
    result = predict_weather(temp, humidity, pressure, wind_speed)
    st.success(f"Predicted Weather: **{result}**")

st.markdown("---")
st.caption("Created with ❤️ using Streamlit | Example by Sahil")
