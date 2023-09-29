import streamlit as st
import pandas as pd
import joblib


# model = joblib.load("best_model.pkl")


# Title and Introduction
st.markdown("<h1 style='color: blue;'>Gym Class Attendance Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: blue;'>Predict the number of attendees for gym classes.</h2>", unsafe_allow_html=True)

# Create a sidebar for user navigation
st.sidebar.header("Navigation")
option = st.sidebar.selectbox("Choose an option:", ["Batch Prediction", "Single Row Prediction"])


# Depending on the selected option, display the corresponding section
if option == "Batch Prediction":
    st.header("Batch Prediction")
    uploaded_file = st.file_uploader("Upload a CSV file for batch predictions:", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.write(data.head())

        # Perform batch predictions here if needed
        # You can loop through rows in the uploaded CSV and apply predict_attendance to each row

elif option == "Single Row Prediction":
    st.header("Single Row Prediction")
    date = st.date_input("Date:")
    time = st.time_input("Time:")
    temperature = st.number_input("Temperature (in degrees Celsius):")
    is_weekend = st.checkbox("Is Weekend?")
    is_holiday = st.checkbox("Is Holiday?")

    # Make Prediction Button for Single Row
    single_row_prediction_button = st.button("Predict Attendance (Single Row)")

    if single_row_prediction_button:
        input_data = {
            "date": date,
            "time": time,
            "temperature": temperature,
            "is_weekend": is_weekend,
            "is_holiday": is_holiday,
        }

        # prediction = predict_attendance(input_data)  # Adjust your prediction function accordingly

        # # Display the prediction
        # st.subheader("Prediction (Single Row):")
        # st.write(f"Predicted Attendance: {prediction}")
