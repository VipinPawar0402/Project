import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users = db["users"]

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = users.find_one({"username": username, "password": password})

        if user:
            st.success("Logged in as {}".format(username))
            return True
        else:
            st.error("Invalid username or password")
            return False

def register():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if users.find_one({"username": username}):
            st.error("Username already taken")
            return False
        else:
            users.insert_one({"username": username, "password": password})
            st.success("Registered successfully. Please login.")
            return True

def main():
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Login":
        if login():
            st.write("This is the homepage.")
    elif choice == "Register":
        if register():
            st.write("Please login.")

if _name_ == '_main_':
    main()
