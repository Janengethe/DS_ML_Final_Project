import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import matplotlib.pyplot as plt


model = joblib.load("big_model.pkl")


def load_model():
    model = joblib.load("best_model.pkl")
    return model

model = load_model()

# Streamlit app
def main():
    st.title("Gym Class Attendance Predictor")
    st.write("Enter the following details to predict attendance:")

    # Input fields for relevant features
    input_date = st.date_input("Date")
    input_time = st.time_input("Time")
    temperature = st.slider("Temperature (°F)", 38, 88, 58)
    is_weekend = st.checkbox("Is Weekend")
    is_holiday = st.checkbox("Is Holiday")
    is_start_of_semester = st.checkbox("Is Start of Semester")
    is_during_semester = st.checkbox("Is During Semester")

    # Extract year, month, date, day of the week, hour, and minutes from input
    datetime_input = datetime.combine(input_date, input_time)
    year = datetime_input.year
    month = datetime_input.month
    date = datetime_input.day
    day_of_week = datetime_input.weekday()
    hour = datetime_input.hour
    minutes = datetime_input.minute

    # Make a prediction when the user clicks the 'Predict' button
    if st.button("Predict"):
        # Prepare the input data as a DataFrame
        input_data = pd.DataFrame({
            "Year": [year],
            "Month": [month],
            "Date": [date],
            "Day_of_week": [day_of_week],
            "Hour": [hour],
            "Minutes": [minutes],
            "Temperature": [temperature],
            "Is_weekend": [is_weekend],
            "Is_holiday": [is_holiday],
            "Is_start_of_semester": [is_start_of_semester],
            "Is_during_semester": [is_during_semester]
        })

        # Use model to make predictions
        prediction = model.predict(input_data)

        rounded = str(np.round(prediction[0])).rstrip('.0')

        st.write(f"Predicted Attendance: {rounded} People")


        historical_data = pd.DataFrame({
            "Date": pd.date_range(start="2017-01-01", end="2017-12-31"),
            "Attendance": np.random.randint(20, 100, size=365)
            })
        # Sample temperature impact data
        temperature_impact_data = pd.DataFrame({
            "Temperature (°F)": np.arange(20, 100),
            "Attendance Impact": np.random.uniform(-10, 10, size=80)
            })
        st.subheader("Historical Attendance Data")
        # Plot historical attendance data
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(historical_data["Date"], historical_data["Attendance"])
        ax.set_xlabel("Date")
        ax.set_ylabel("Attendance")
        ax.set_title("Historical Attendance Trend")
        st.pyplot(fig)


if __name__ == "__main__":
    main()
