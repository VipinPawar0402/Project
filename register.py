import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["user_login"]
collection = db["users"]

# Define function to authenticate user
def authenticate_user(username, password):
    user = collection.find_one({"username": username, "password": password})
    if user:
        return True
    else:
        return False

# Define Streamlit app
def main():
    # Set app title
    st.title('Cotton Plant Disease Detection App')
    # Add login form for username and password
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        # Authenticate user
        if authenticate_user(username, password):
            st.success('You have successfully logged in!')
            # Add link to second page
            st.write('Go to the [disease detection page](/app?page=disease_detection)')
        else:
            st.error('Invalid username or password')

if _name_ == '_main_':
    main()
