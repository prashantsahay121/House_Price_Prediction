import streamlit as st
import pandas as pd
import pickle

# Load the trained Ridge model and cleaned data
model = pickle.load(open('RidgeModel.pkl', 'rb'))
data = pd.read_csv('Cleaned_data.csv')

# App Title
# st.title("Bengaluru House Price Prediction")
# Add background image and customize text style
def set_custom_styles(image_url):
    """
    Set the background image for the Streamlit app.
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image URL
set_custom_styles("https://img.freepik.com/free-photo/abstract-textured-backgound_1258-30499.jpg?semt=ais_hybrid")  # Replace with your image URL

# App Title
st.title("Bengaluru House Price Prediction")

# CSS for custom styles
import streamlit as st

st.markdown(
    """
    <style>
    .stSelectbox, .stNumberInput {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 8px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
        background-color: #f9f9f9;
    }
    .stNumberInput label, .stSelectbox label {
        color: #4CAF50;
        font-weight: bold;
        font-size: 16px;
    }
    .stSelectbox select, .stNumberInput input {
        color: #333;
        font-size: 14px;
        padding: 6px;
    }

    .st-success .stMarkdown {
        color: white;
        background-color: blue;
        font-size: 20px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    """,
    unsafe_allow_html=True
)



# User Inputs
# Location dropdown populated dynamically from the data
locations = data['location'].unique()
location = st.selectbox("Select Location:", locations)

# Input fields for BHK, Bathrooms, and Square Feet
bhk = st.number_input("Enter BHK (Number of Bedrooms):", min_value=1, step=1, value=1)
bath = st.number_input("Enter Number of Bathrooms:", min_value=1, step=1, value=1)
total_sqft = st.number_input("Enter Total Square Feet:", min_value=1, step=1, value=1000)

# Button to Predict Price
if st.button("Predict Price"):
    # Prepare input data for the model
    input_data = pd.DataFrame({
        'location': [location],
        'total_sqft': [total_sqft],
        'bath': [bath],
        'bhk': [bhk]
    })

    # Make the prediction
    predicted_price = model.predict(input_data)[0]
    predicted_price=predicted_price*1e5

    # Display the predicted price
    st.success(f"The predicted price for the house is: ₹{predicted_price:,.2f}")
