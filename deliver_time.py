import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu
from PIL import Image

# Set Streamlit Page Config
st.set_page_config(page_title="Amazon Delivery Time Predictor", layout="wide")

# Load the trained model efficiently
try:
    model = joblib.load("random_forest_model.pkl", mmap_mode='r')
except Exception as e:
    st.error("Error loading model. Please check the file integrity.")
    st.stop()

# try:
#     model = joblib.load("Amazon_Deliver_Time.pkl", mmap_mode='r')
# except Exception as e:
#     st.error("Error loading model. Please check the file integrity.")
#     st.stop()

# Streamlit UI Layout
col1, col2 = st.columns([1, 3])

# Left-hand side: Menu
with col1:
    menu_option = option_menu(
        "Main Menu",
        options=["Delivery Time Prediction","EDA"],
        default_index=0
    )

# Function to convert date and time
def convert_to_datetime(date_str, time_str):
    date_time = pd.to_datetime(f"{date_str} {time_str}")
    return date_time.day, date_time.month, date_time.hour, date_time.minute

# Main section for Delivery Time Prediction
with col2:
    if menu_option == "Delivery Time Prediction":
        st.title("Amazon Delivery Time Prediction 🚚")
        st.markdown("### Enter delivery details to estimate time")

        # User Inputs
        order_date = st.date_input("Order Date")
        order_time = st.time_input("Order Time")
        pickup_time = st.time_input("Pickup Time")
        distance_km = st.number_input("Distance (in km)", min_value=0.1, step=0.1)
        agent_age = st.number_input("Delivery Agent Age", min_value=18, step=1)
        agent_rating = st.slider("Agent Rating (0-5)", min_value=0.0, max_value=5.0, step=0.1)

        # Categorical Inputs
        weather_options = ["Sunny", "Sandstorms", "Cloudy", "Fog", "Windy"]
        traffic_options = ["Low", "Medium", "Jam"]
        vehicle_options = ["scooter", "van"]
        area_options = ["Urban", "Other", "Semi-Urban"]
        category_options = [
            "Electronics", "Books", "Jewelry", "Toys", "Snacks", "Skincare",
            "Outdoors", "Sports", "Grocery", "Pet Supplies", "Home",
            "Cosmetics", "Kitchen", "Clothing", "Shoes"
        ]

        weather = st.selectbox("Weather Conditions", weather_options)
        traffic = st.selectbox("Traffic Conditions", traffic_options)
        vehicle = st.selectbox("Vehicle Type", vehicle_options)
        area = st.selectbox("Area Type", area_options)
        category = st.selectbox("Product Category", category_options)

        # Convert datetime inputs
        order_day, order_month, order_hour, order_minute = convert_to_datetime(order_date, order_time)
        pickup_hour, pickup_minute = convert_to_datetime(order_date, pickup_time)[2:]

        # Encoding Mappings (One-Hot Encoding)
        def one_hot_encode(value, options):
            return [1 if value == option else 0 for option in options]

        input_features = [
            agent_age, agent_rating, distance_km, 
            order_month, order_day, order_hour, order_minute, 
            pickup_hour, pickup_minute
        ] + one_hot_encode(weather, weather_options) \
          + one_hot_encode(traffic, traffic_options) \
          + one_hot_encode(vehicle, vehicle_options) \
          + one_hot_encode(area, area_options) \
          + one_hot_encode(category, category_options)

        # Prediction Button
        if st.button("Predict Delivery Time ⏳"):
            prediction = model.predict([input_features])[0]
            st.success(f"Estimated Delivery Time: {prediction:.2f} minutes")
    
    if menu_option == "EDA":
        st.title("Exploratory Data Analysis (EDA) 📊")

        st.subheader("Delivery Time Distibution over Data")
        image = Image.open("delivery_time.png")
        resized_image = image.resize((800, 400))
        st.image(resized_image)
        st.text("According to the histogram plot, delivery agents often take between 60 and 160 minutes for deliveries.")

        st.write("---")

        st.subheader("Average Delivery Time by Traffic Condition")
        image = Image.open("traffic.png")
        resized_image = image.resize((800, 400))
        st.image(resized_image)
        st.text("As expected, delivery agents take more time when traffic conditions are jammed. Additionally, medium and high traffic conditions show similar delivery times")

        st.write("---")

        st.subheader("Delivery Time Trend Over the Day")
        image = Image.open("hour.png")
        resized_image = image.resize((800, 400))
        st.image(resized_image)
        st.text("""According to the line plot, from the start of the day until 10 AM, delivery agents take between 50 to 105 minutes. However, after 10 AM, 
                there is a drastic increase, peaking at around 125 minutes by 11 AM. The delivery time then increases linearly until 2 PM. Afterward, 
                it follows a zigzag pattern for the rest of the day. Finally, between 7 to 9 PM, delivery agents take approximately 150 minutes for deliveries""")

        st.write("---")

        st.subheader("Number of Deliveries per Category")
        image = Image.open("category.png")
        resized_image = image.resize((800, 500))
        st.image(resized_image)
        st.text("According to the count plot, customer orders are highest for Electronics, Apparel, and Books.")

        st.write("---")