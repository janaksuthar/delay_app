import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('delivery_delay.sav')

st.title('Delivery Delay Prediction')

st.write('Enter the details below to predict if there will be a delivery delay:')

# Input fields for features, updated from sliders
delivery_distance = st.number_input('Delivery Distance (km)', min_value=0.0, max_value=100.0, value=20.0, step=0.1)
traffic_congestion = st.selectbox('Traffic Congestion (1-5)', options=[1, 2, 3, 4, 5], index=2)
weather_condition = st.selectbox('Weather Condition (1-5)', options=[1, 2, 3, 4, 5], index=2)
delivery_slot = st.selectbox('Delivery Slot (1-3)', options=[1, 2, 3], index=1)
driver_experience = st.number_input('Driver Experience (years)', min_value=0, max_value=20, value=5, step=1)
num_stops = st.number_input('Number of Stops', min_value=1, max_value=10, value=4, step=1)
vehicle_age = st.number_input('Vehicle Age (years)', min_value=0, max_value=15, value=3, step=1)
road_condition_score = st.selectbox('Road Condition Score (1-5)', options=[1, 2, 3, 4, 5], index=2)
package_weight = st.number_input('Package Weight (kg)', min_value=0.0, max_value=50.0, value=10.0, step=0.1)
fuel_efficiency = st.number_input('Fuel Efficiency (km/l)', min_value=5.0, max_value=25.0, value=15.0, step=0.1)
warehouse_processing_time = st.number_input('Warehouse Processing Time (minutes)', min_value=0, max_value=100, value=30, step=1)

# Create a DataFrame from inputs
input_data = pd.DataFrame([{
    'Delivery_Distance': delivery_distance,
    'Traffic_Congestion': traffic_congestion,
    'Weather_Condition': weather_condition,
    'Delivery_Slot': delivery_slot,
    'Driver_Experience': driver_experience,
    'Num_Stops': num_stops,
    'Vehicle_Age': vehicle_age,
    'Road_Condition_Score': road_condition_score,
    'Package_Weight': package_weight,
    'Fuel_Efficiency': fuel_efficiency,
    'Warehouse_Processing_Time': warehouse_processing_time
}])

if st.button('Predict Delivery Delay'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error('Prediction: \"Delivery Delay is likely!\"')
    else:
        st.success('Prediction: \"No Delivery Delay is expected.\"')
